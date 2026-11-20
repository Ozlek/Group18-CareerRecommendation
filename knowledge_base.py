# Knowledge base for career recommendations. Each career has associated interests, skills, work preferences, personality traits, and work nature
# Scalable to add more careers and categories. The inference engine uses this data to match user profiles with suitable careers
# Can transform into a database or external file for larger datasets. Currently, it's a Python dictionary for simplicity and easy testing

knowledge_base = {

    # ==========================================
    # TECHNOLOGY AND INFORMATION TECHNOLOGY
    # ==========================================

    "C01": {
        "career": "Software Developer",
        "category": "Technology and IT",
        "interests": [
            "programming", "technology", "problem_solving",
            "software_development"
        ],
        "skills": [
            "programming", "logical_thinking",
            "debugging", "critical_thinking"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "office_work", "remote_work"
        ],
        "personality": [
            "analytical", "patient", "detail_oriented",
            "curious"
        ],
        "work_nature": [
            "mental_work", "technical_work"
        ]
    },

    "C02": {
        "career": "Data Analyst",
        "category": "Technology and IT",
        "interests": [
            "data_analysis", "mathematics",
            "technology", "business"
        ],
        "skills": [
            "analytical_thinking", "sql",
            "spreadsheet_management", "critical_thinking"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "office_work", "remote_work"
        ],
        "personality": [
            "analytical", "curious",
            "detail_oriented", "logical"
        ],
        "work_nature": [
            "mental_work", "technical_work"
        ]
    },

    "C03": {
        "career": "Cybersecurity Analyst",
        "category": "Technology and IT",
        "interests": [
            "technology", "cybersecurity",
            "investigation", "problem_solving"
        ],
        "skills": [
            "networking", "risk_assessment",
            "analytical_thinking", "technical_troubleshooting"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "office_work", "remote_work"
        ],
        "personality": [
            "analytical", "investigative",
            "detail_oriented", "curious"
        ],
        "work_nature": [
            "mental_work", "technical_work"
        ]
    },

    "C04": {
        "career": "Database Administrator",
        "category": "Technology and IT",
        "interests": [
            "databases", "technology",
            "information_management", "problem_solving"
        ],
        "skills": [
            "sql", "database_management",
            "technical_troubleshooting", "organization"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "office_work", "remote_work"
        ],
        "personality": [
            "analytical", "organized",
            "detail_oriented", "patient"
        ],
        "work_nature": [
            "mental_work", "technical_work"
        ]
    },

    # ==========================================
    # BUSINESS AND FINANCE
    # ==========================================

    "C05": {
        "career": "Accountant",
        "category": "Business and Finance",
        "interests": [
            "finance", "mathematics",
            "business", "record_management"
        ],
        "skills": [
            "accounting", "numerical_analysis",
            "spreadsheet_management", "organization"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "office_work"
        ],
        "personality": [
            "analytical", "organized",
            "detail_oriented", "responsible"
        ],
        "work_nature": [
            "mental_work", "technical_work"
        ]
    },

    "C06": {
        "career": "Financial Analyst",
        "category": "Business and Finance",
        "interests": [
            "finance", "investments",
            "economics", "business"
        ],
        "skills": [
            "financial_analysis", "numerical_analysis",
            "research", "critical_thinking"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "office_work"
        ],
        "personality": [
            "analytical", "logical",
            "detail_oriented", "curious"
        ],
        "work_nature": [
            "mental_work", "technical_work"
        ]
    },

    "C07": {
        "career": "Business Analyst",
        "category": "Business and Finance",
        "interests": [
            "business", "problem_solving",
            "process_improvement", "technology"
        ],
        "skills": [
            "analytical_thinking", "communication",
            "research", "documentation",
            "critical_thinking"
        ],
        "work_preferences": [
            "teamwork", "client_interaction",
            "office_work", "remote_work"
        ],
        "personality": [
            "analytical", "organized",
            "adaptable", "curious"
        ],
        "work_nature": [
            "mental_work", "interpersonal_work"
        ]
    },

    "C08": {
        "career": "Human Resources Specialist",
        "category": "Business and Finance",
        "interests": [
            "human_resources", "business",
            "helping_people", "workplace_management"
        ],
        "skills": [
            "communication", "organization",
            "conflict_resolution", "interpersonal_skills"
        ],
        "work_preferences": [
            "teamwork", "client_interaction",
            "office_work"
        ],
        "personality": [
            "empathetic", "organized",
            "patient", "adaptable"
        ],
        "work_nature": [
            "mental_work", "interpersonal_work"
        ]
    },

    # ==========================================
    # CREATIVE AND ARTS
    # ==========================================

    "C09": {
        "career": "Graphic Designer",
        "category": "Creative and Arts",
        "interests": [
            "visual_arts", "design",
            "visual_communication", "creativity"
        ],
        "skills": [
            "visual_design", "drawing",
            "creativity", "visual_composition"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "studio_work", "remote_work",
            "client_interaction"
        ],
        "personality": [
            "imaginative", "artistic",
            "detail_oriented", "adaptable"
        ],
        "work_nature": [
            "creative_work", "mental_work"
        ]
    },

    "C10": {
        "career": "Photographer",
        "category": "Creative and Arts",
        "interests": [
            "photography", "visual_arts",
            "storytelling", "creativity"
        ],
        "skills": [
            "photography", "visual_composition",
            "photo_editing", "creativity"
        ],
        "work_preferences": [
            "independent_work", "client_interaction",
            "outdoor_work", "studio_work"
        ],
        "personality": [
            "artistic", "observant",
            "imaginative", "adaptable"
        ],
        "work_nature": [
            "creative_work", "technical_work"
        ]
    },

    "C11": {
        "career": "Animator",
        "category": "Creative and Arts",
        "interests": [
            "animation", "visual_arts",
            "storytelling", "digital_media"
        ],
        "skills": [
            "animation", "drawing",
            "visual_design", "creativity",
            "attention_to_detail"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "studio_work", "remote_work"
        ],
        "personality": [
            "imaginative", "artistic",
            "patient", "detail_oriented"
        ],
        "work_nature": [
            "creative_work", "technical_work"
        ]
    },

    "C12": {
        "career": "Fashion Designer",
        "category": "Creative and Arts",
        "interests": [
            "fashion", "design",
            "visual_arts", "craftsmanship"
        ],
        "skills": [
            "fashion_design", "drawing",
            "sewing", "creativity"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "studio_work", "hands_on_work"
        ],
        "personality": [
            "artistic", "imaginative",
            "resourceful", "detail_oriented"
        ],
        "work_nature": [
            "creative_work", "physical_work"
        ]
    },

    # ==========================================
    # HEALTHCARE AND SOCIAL SERVICES
    # ==========================================

    "C13": {
        "career": "Nurse",
        "category": "Healthcare and Social Services",
        "interests": [
            "healthcare", "helping_people",
            "biology", "patient_care"
        ],
        "skills": [
            "caregiving", "communication",
            "medical_knowledge", "critical_thinking"
        ],
        "work_preferences": [
            "teamwork", "patient_interaction",
            "hands_on_work"
        ],
        "personality": [
            "empathetic", "compassionate",
            "patient", "responsible"
        ],
        "work_nature": [
            "physical_work", "interpersonal_work",
            "technical_work"
        ]
    },

    "C14": {
        "career": "Psychologist",
        "category": "Healthcare and Social Services",
        "interests": [
            "psychology", "human_behavior",
            "mental_health", "helping_people"
        ],
        "skills": [
            "active_listening", "research",
            "communication", "critical_thinking"
        ],
        "work_preferences": [
            "independent_work", "teamwork",
            "client_interaction", "office_work"
        ],
        "personality": [
            "empathetic", "patient",
            "analytical", "observant"
        ],
        "work_nature": [
            "mental_work", "interpersonal_work"
        ]
    },

    "C15": {
        "career": "Social Worker",
        "category": "Healthcare and Social Services",
        "interests": [
            "helping_people", "community_service",
            "social_issues", "human_behavior"
        ],
        "skills": [
            "communication", "active_listening",
            "problem_solving", "conflict_resolution"
        ],
        "work_preferences": [
            "teamwork", "client_interaction",
            "field_work"
        ],
        "personality": [
            "empathetic", "compassionate",
            "adaptable", "patient"
        ],
        "work_nature": [
            "interpersonal_work", "mental_work"
        ]
    },

    # ==========================================
    # VOCATIONAL AND SKILLED TRADES
    # ==========================================

    "C16": {
        "career": "Electrician",
        "category": "Vocational and Skilled Trades",
        "interests": [
            "electronics", "construction",
            "problem_solving", "craftsmanship"
        ],
        "skills": [
            "electrical_repair", "technical_troubleshooting",
            "manual_dexterity", "critical_thinking"
        ],
        "work_preferences": [
            "hands_on_work", "field_work",
            "independent_work", "teamwork"
        ],
        "personality": [
            "practical", "detail_oriented",
            "resourceful", "patient"
        ],
        "work_nature": [
            "physical_work", "technical_work"
        ]
    },

    "C17": {
        "career": "Automotive Mechanic",
        "category": "Vocational and Skilled Trades",
        "interests": [
            "vehicles", "mechanics",
            "technology", "problem_solving"
        ],
        "skills": [
            "mechanical_repair", "diagnostics",
            "technical_troubleshooting", "manual_dexterity"
        ],
        "work_preferences": [
            "hands_on_work", "workshop_work",
            "independent_work", "teamwork"
        ],
        "personality": [
            "practical", "resourceful",
            "patient", "observant"
        ],
        "work_nature": [
            "physical_work", "technical_work"
        ]
    },

    "C18": {
        "career": "Welder",
        "category": "Vocational and Skilled Trades",
        "interests": [
            "metalworking", "construction",
            "craftsmanship", "manufacturing"
        ],
        "skills": [
            "welding", "manual_dexterity",
            "technical_drawing", "attention_to_detail"
        ],
        "work_preferences": [
            "hands_on_work", "workshop_work",
            "field_work", "teamwork"
        ],
        "personality": [
            "practical", "patient",
            "detail_oriented", "resourceful"
        ],
        "work_nature": [
            "physical_work", "technical_work"
        ]
    },

    # ==========================================
    # EDUCATION AND AGRICULTURE
    # ==========================================

    "C19": {
        "career": "Teacher",
        "category": "Education and Outdoor Professions",
        "interests": [
            "education", "teaching",
            "helping_people", "learning"
        ],
        "skills": [
            "communication", "instruction",
            "organization", "public_speaking"
        ],
        "work_preferences": [
            "teamwork", "group_interaction",
            "classroom_work"
        ],
        "personality": [
            "patient", "empathetic",
            "adaptable", "responsible"
        ],
        "work_nature": [
            "mental_work", "interpersonal_work"
        ]
    },

    "C20": {
        "career": "Agricultural Technician",
        "category": "Education and Outdoor Professions",
        "interests": [
            "agriculture", "nature",
            "plants", "science"
        ],
        "skills": [
            "plant_cultivation", "research",
            "observation", "technical_knowledge"
        ],
        "work_preferences": [
            "outdoor_work", "field_work",
            "hands_on_work", "teamwork"
        ],
        "personality": [
            "practical", "observant",
            "patient", "resourceful"
        ],
        "work_nature": [
            "physical_work", "technical_work"
        ]
    }
}