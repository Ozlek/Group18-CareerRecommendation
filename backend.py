from inference_engine import infer_careers

"""Flask backend: serves the frontend and recommendation API."""

from flask import Flask, jsonify, render_template, request

from inference_engine import RULE_WEIGHTS, infer_careers
from knowledge_base import knowledge_base

app = Flask(__name__)

CATEGORY_LABELS = {
    "interests": "Interests",
    "skills": "Skills",
    "work_preferences": "Work Preferences",
    "personality": "Personality",
    "work_nature": "Work Nature",
}

def get_available_options():
    """Build the selectable values from all career profiles."""
    options = {}
    for field in RULE_WEIGHTS:
        values = set()
        for career in knowledge_base.values():
            values.update(career.get(field, []))
        options[field] = sorted(values)
    return options

@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/options")
def api_options():
    """Return valid answer choices for the frontend."""
    return jsonify({
        "categories": CATEGORY_LABELS,
        "options": get_available_options(),
    })

@app.post("/api/recommend")
def api_recommend():
    """Receive a user profile, run the inference engine, and return results."""
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "Please submit your answers in JSON format."}), 400

    submitted_profile = payload.get("profile", {})
    if not isinstance(submitted_profile, dict):
        return jsonify({"error": "The profile must be an object of selected answers."}), 400

    available_options = get_available_options()
    user_profile = {}

    # Keep only recognized categories and values from the knowledgebase.
    for field in RULE_WEIGHTS:
        raw_values = submitted_profile.get(field, [])
        if not isinstance(raw_values, list):
            return jsonify({"error": f"'{CATEGORY_LABELS[field]}' must be a list."}), 400

        allowed = set(available_options[field])
        cleaned = {
            value.strip()
            for value in raw_values
            if isinstance(value, str) and value.strip() in allowed
        }
        user_profile[field] = sorted(cleaned)

    if not any(user_profile.values()):
        return jsonify({"error": "Select at least one answer before requesting recommendations."}), 400

    try:
        results = infer_careers(user_profile, knowledge_base)
        return jsonify({
            "recommendations": results[:5],
            "total_matches": len(results),
            "message": "Recommendations are ranked by weighted attribute matches.",
        })
    except Exception:
        # Keep technical details in the server log, not in the user response.
        app.logger.exception("Failed to generate career recommendations")
        return jsonify({
            "error": "Unable to generate recommendations. Please try again."
        }), 500