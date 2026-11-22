const form = document.getElementById("career-form");
const questionGroups = document.getElementById("question-groups");
const resultsSection = document.getElementById("results-section");
const resultsTitle = document.getElementById("results-title");
const resultsList = document.getElementById("results-list");
const resultsSummary = document.getElementById("results-summary");
const statusMessage = document.getElementById("status-message");
const submitButton = document.getElementById("submit-button");
const selectedCount = document.getElementById("selected-count");
const weightNote = document.getElementById("weight-note");

let categoryLabels = {};
let fieldNames = [];

const ACRONYMS = { sql: "SQL" };
const SEARCH_THRESHOLD = 12;

function humanize(value) {
  return value
    .split("_")
    .map(word => ACRONYMS[word] || word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

function categoryLabel(field) {
  return categoryLabels[field] || humanize(field);
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

function createGroup(field, values, weight, openByDefault) {
  const group = document.createElement("details");
  group.className = "question-group";
  group.dataset.field = field;
  group.open = openByDefault;

  const summary = document.createElement("summary");
  const title = document.createElement("span");
  title.className = "group-title";
  title.textContent = categoryLabel(field);
  summary.appendChild(title);

  if (typeof weight === "number") {
    const weightTag = document.createElement("span");
    weightTag.className = "group-weight";
    weightTag.textContent = `${Math.round(weight * 100)}% weight`;
    summary.appendChild(weightTag);
  }

  const badge = document.createElement("span");
  badge.className = "group-badge";
  badge.hidden = true;
  summary.appendChild(badge);
  group.appendChild(summary);

  const fieldset = document.createElement("fieldset");
  const legend = document.createElement("legend");
  legend.className = "sr-only";
  legend.textContent = categoryLabel(field);
  fieldset.appendChild(legend);

  const list = document.createElement("div");
  list.className = "option-list";
  values.forEach(value => list.appendChild(createOption(field, value)));

  if (values.length > SEARCH_THRESHOLD) {
    const search = document.createElement("input");
    search.type = "search";
    search.className = "group-search";
    search.placeholder = `Search ${categoryLabel(field).toLowerCase()}…`;
    search.setAttribute("aria-label", `Search ${categoryLabel(field)}`);
    search.addEventListener("input", () => filterOptions(list, search.value));
    search.addEventListener("keydown", event => { if (event.key === "Enter") event.preventDefault(); });
    fieldset.appendChild(search);
  }

  fieldset.appendChild(list);
  group.appendChild(fieldset);
  return group;
}

function filterOptions(list, query) {
  const needle = query.trim().toLowerCase();
  list.querySelectorAll(".option").forEach(option => {
    option.hidden = needle !== "" && !option.textContent.toLowerCase().includes(needle);
  });
}

function updateCounts() {
  let total = 0;
  questionGroups.querySelectorAll(".question-group").forEach(group => {
    const count = group.querySelectorAll("input[type=checkbox]:checked").length;
    const badge = group.querySelector(".group-badge");
    badge.textContent = `${count} selected`;
    badge.hidden = count === 0;
    total += count;
  });
  selectedCount.textContent = total === 1 ? "1 selected" : `${total} selected`;
}

async function loadOptions() {
  try {
    const response = await fetch("/api/options");
    if (!response.ok) throw new Error("Unable to load the knowledgebase options.");

    const data = await response.json();
    categoryLabels = data.categories || {};
    const weights = data.weights || {};

    fieldNames = Object.keys(data.options).sort(
      (a, b) => (weights[b] ?? 0) - (weights[a] ?? 0)
    );

    if (Object.keys(weights).length) {
      weightNote.textContent = "Matching weights: " + fieldNames
        .map(field => `${categoryLabel(field)} ${Math.round((weights[field] ?? 0) * 100)}%`)
        .join(" · ");
      weightNote.hidden = false;
    }

    questionGroups.replaceChildren();
    fieldNames.forEach((field, index) => {
      questionGroups.appendChild(createGroup(field, data.options[field], weights[field], index === 0));
    });
    updateCounts();
  } catch (error) {
    questionGroups.textContent = "Could not load answer choices. Check that the Flask server is running.";
    showError(error.message);
  }
}

function collectProfile() {
  const profile = {};
  for (const field of fieldNames) {
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

function humanizeRule(rule) {
  return rule.replace(/'([^']+)'/g, (_, token) => `'${categoryLabels[token] || humanize(token)}'`);
}

function countValues(groupedFacts) {
  return Object.values(groupedFacts).reduce((sum, facts) => sum + facts.length, 0);
}

function renderRecommendations(data, profile) {
  resultsList.replaceChildren();
  resultsSection.hidden = false;

  const shown = data.recommendations.length;
  let summary = `${shown} top recommendation(s) shown from ${data.total_matches} matching career(s).`;
  const topScore = shown ? data.recommendations[0].score : null;
  const tiedAtTop = data.recommendations.filter(career => career.score === topScore).length;
  if (tiedAtTop > 1) {
    summary += " Several careers share the top score. Select more attributes to separate them.";
  }
  resultsSummary.textContent = summary;

  if (!shown) {
    addText(resultsList, "p", "muted", "No matching careers were found. Try selecting more attributes.");
    return;
  }

  const selectedTotal = countValues(profile);

  data.recommendations.forEach((career, index) => {
    const card = document.createElement("article");
    card.className = "result-card";

    const top = document.createElement("div");
    top.className = "result-top";
    const titleBlock = document.createElement("div");
    addText(titleBlock, "h3", "result-title", `${index + 1}. ${career.career}`);
    addText(titleBlock, "p", "result-category", career.category);
    top.appendChild(titleBlock);
    const scoreBlock = document.createElement("div");
    scoreBlock.className = "score-block";
    addText(scoreBlock, "div", "score", `${career.score.toFixed(2)}%`);
    addText(scoreBlock, "div", "score-meta", `${countValues(career.matched_facts)} of ${selectedTotal} selected matched`);
    top.appendChild(scoreBlock);
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
        tag.textContent = `${categoryLabel(category)}: ${humanize(fact)}`;
        tags.appendChild(tag);
      });
    }
    card.appendChild(tags);

    const details = document.createElement("details");
    const summaryEl = document.createElement("summary");
    summaryEl.textContent = `View activated rules (${career.fired_rules.length})`;
    const rules = document.createElement("ul");
    rules.className = "rule-list";
    career.fired_rules.forEach(rule => addText(rules, "li", "", humanizeRule(rule)));
    details.append(summaryEl, rules);
    card.appendChild(details);

    resultsList.appendChild(card);
  });
}

form.addEventListener("change", updateCounts);

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
    renderRecommendations(data, profile);
    resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
    resultsTitle.focus({ preventScroll: true });
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
  setTimeout(() => {
    questionGroups.querySelectorAll(".option").forEach(option => { option.hidden = false; });
    updateCounts();
  }, 0);
});

loadOptions();