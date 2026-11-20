const form = document.getElementById("career-form");
const questionGroups = document.getElementById("question-groups");
const resultsSection = document.getElementById("results-section");
const resultsList = document.getElementById("results-list");
const resultsSummary = document.getElementById("results-summary");
const statusMessage = document.getElementById("status-message");
const submitButton = document.getElementById("submit-button");

function humanize(value) {
  return value.replaceAll("_", " ").replace(/\b\w/g, character => character.toUpperCase());
}

function showError(message) {
  statusMessage.textContent = message;
  statusMessage.hidden = false;
}

function clearError() {
  statusMessage.textContent = "";
  statusMessage.hidden = true;
}

function createOption(field, value) {
  const label = document.createElement("label");
  label.className = "option";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.name = field;
  checkbox.value = value;

  const text = document.createElement("span");
  text.textContent = humanize(value);

  label.append(checkbox, text);
  return label;
}

async function loadOptions() {
  try {
    const response = await fetch("/api/options");
    if (!response.ok) throw new Error("Unable to load the knowledgebase options.");

    const data = await response.json();
    questionGroups.replaceChildren();

    for (const [field, values] of Object.entries(data.options)) {
      const section = document.createElement("section");
      section.className = "question-group";

      const heading = document.createElement("h3");
      heading.textContent = data.categories[field] || humanize(field);

      const options = document.createElement("div");
      options.className = "option-list";
      values.forEach(value => options.appendChild(createOption(field, value)));

      section.append(heading, options);
      questionGroups.appendChild(section);
    }
  } catch (error) {
    questionGroups.textContent = "Could not load answer choices. Check that the Flask server is running.";
    showError(error.message);
  }
}

function collectProfile() {
  const profile = {};
  for (const field of ["interests", "skills", "work_preferences", "personality", "work_nature"]) {
    profile[field] = Array.from(
      form.querySelectorAll(`input[name="${field}"]:checked`),
      checkbox => checkbox.value
    );
  }
  return profile;
}

function addText(parent, tagName, className, text) {
  const element = document.createElement(tagName);
  if (className) element.className = className;
  element.textContent = text;
  parent.appendChild(element);
  return element;
}

function renderRecommendations(data) {
  resultsList.replaceChildren();
  resultsSection.hidden = false;
  resultsSummary.textContent = `${data.recommendations.length} top recommendation(s) shown from ${data.total_matches} matching career(s).`;

  if (!data.recommendations.length) {
    addText(resultsList, "p", "muted", "No matching careers were found. Try selecting more attributes.");
    return;
  }

  data.recommendations.forEach((career, index) => {
    const card = document.createElement("article");
    card.className = "result-card";

    const top = document.createElement("div");
    top.className = "result-top";
    const titleBlock = document.createElement("div");
    addText(titleBlock, "h3", "result-title", `${index + 1}. ${career.career}`);
    addText(titleBlock, "p", "result-category", career.category);
    top.appendChild(titleBlock);
    addText(top, "div", "score", `${career.score.toFixed(2)}%`);
    card.appendChild(top);

    const track = document.createElement("div");
    track.className = "score-track";
    const fill = document.createElement("div");
    fill.className = "score-fill";
    fill.style.width = `${Math.max(0, Math.min(100, career.score))}%`;
    track.appendChild(fill);
    card.appendChild(track);

    addText(card, "h4", "match-heading", "Matching attributes");
    const tags = document.createElement("div");
    tags.className = "tags";
    for (const [category, facts] of Object.entries(career.matched_facts)) {
      facts.forEach(fact => {
        const tag = document.createElement("span");
        tag.className = "tag";
        tag.textContent = `${humanize(category)}: ${humanize(fact)}`;
        tags.appendChild(tag);
      });
    }
    card.appendChild(tags);

    const details = document.createElement("details");
    const summary = document.createElement("summary");
    summary.textContent = `View activated rules (${career.fired_rules.length})`;
    const rules = document.createElement("ul");
    rules.className = "rule-list";
    career.fired_rules.forEach(rule => addText(rules, "li", "", rule));
    details.append(summary, rules);
    card.appendChild(details);

    resultsList.appendChild(card);
  });
}

form.addEventListener("submit", async event => {
  event.preventDefault();
  clearError();
  resultsSection.hidden = true;

  const profile = collectProfile();
  const hasSelection = Object.values(profile).some(values => values.length > 0);
  if (!hasSelection) {
    showError("Please select at least one answer before requesting recommendations.");
    return;
  }

  submitButton.disabled = true;
  submitButton.textContent = "Analyzing your answers…";

  try {
    const response = await fetch("/api/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ profile })
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "The recommendation request failed.");
    renderRecommendations(data);
    resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (error) {
    showError(error.message);
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = "Find my career matches";
  }
});

form.addEventListener("reset", () => {
  clearError();
  resultsSection.hidden = true;
});

loadOptions();