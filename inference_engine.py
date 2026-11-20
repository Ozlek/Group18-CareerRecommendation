# Forward Chaining Rule-based inference engine for career recommendations

RULE_WEIGHTS = {
    "interests": 0.30,
    "skills": 0.25,
    "work_preferences": 0.20,
    "personality": 0.15,
    "work_nature": 0.10,
}

# Compare user facts with each career and return ranked recommendations. The score is a weighted matching score
# Categories the user leaves blank are excluded from the calculation

def infer_careers(user_profile, knowledge_base):

    recommendations = []

    # Loop through each career in the knowledge base and calculate a matching score based on user profile
    for career_id, career in knowledge_base.items():
        earned_score = 0.0
        active_weight = 0.0
        matched_facts = {}
        fired_rules = []

        # Loop through each category and compare user facts with career facts
        # For each category, if the user has provided facts, calculate the match ratio and update the earned score and active weight
        for category, weight in RULE_WEIGHTS.items():
            user_facts = set(user_profile.get(category, []))
            career_facts = set(career.get(category, []))

            if not user_facts:
                continue

            active_weight += weight
            matches = user_facts.intersection(career_facts)
            match_ratio = len(matches) / len(user_facts)
            earned_score += match_ratio * weight

            if matches:
                matched_facts[category] = sorted(matches)
                for fact in sorted(matches):
                    fired_rules.append(
                        f"IF '{fact}' matches '{category}' THEN "
                        f"increase the {career['career']} match score."
                    )

        if active_weight == 0:
            continue

        final_score = (earned_score / active_weight) * 100

        # Only include careers with at least one matched fact in the recommendations
        # If a career has no matched facts, it is excluded from the recommendations list. This ensures that the user only sees relevant career suggestions based on their provided profile
        if matched_facts:
            recommendations.append({
                "career_id": career_id,
                "career": career["career"],
                "category": career["category"],
                "score": round(final_score, 2),
                "matched_facts": matched_facts,
                "fired_rules": fired_rules,
            })

    # Sort recommendations by score in descending order and return the list
    recommendations.sort(key=lambda item: item["score"], reverse=True)
    return recommendations