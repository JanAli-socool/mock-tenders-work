import json
import os

def extract_fields_from_tender(tender_text, model="mock"):
    if model == "mock":
        data = {}
        if "Berlin" in tender_text:
            data = {
                "Project name": "Municipal Library Construction",
                "location": "Berlin",
                "Budget": 2500000,
                "Project type": "Library Construction",
                "Phases": "Planning, Execution, Commissioning",
                "Submission deadline": "2025-06-15"
            }
        elif "Munich" in tender_text:
            data = {
                "Project name": "Healthcare Facility in Munich",
                "location": "Munich",
                "Budget": 3100000,
                "Project type": "Hospital",
                "Phases": "Phase 1 to Phase 5",
                "Submission deadline": "2025-07-30"
            }
        elif "Stuttgart" in tender_text:
            data = {
                "Project name": "Refurbishment of Historic Theatre",
                "location": "Stuttgart",
                "Budget": 1800000,
                "Project type": "Theatre Refurbishment",
                "Phases": "Planning, Interior Remodeling, Electrical Upgrades",
                "Submission deadline": "2025-08-10"
            }
        elif "Hamburg" in tender_text:
            data = {
                "Project name": "Hamburg School Modernization",
                "location": "Hamburg",
                "Budget": 1500000,
                "Project type": "School Renovation",
                "Phases": "Execution, Interior Updates",
                "Submission deadline": "2025-09-15"
            }
        elif "Frankfurt" in tender_text:
            data = {
                "Project name": "Frankfurt Urban Park Development",
                "location": "Frankfurt",
                "Budget": 2000000,
                "Project type": "Urban Park",
                "Phases": "Design, Construction",
                "Submission deadline": "2025-09-30"
            }
        elif "Düsseldorf" in tender_text:
            data = {
                "Project name": "Düsseldorf Residential Complex",
                "location": "Düsseldorf",
                "Budget": 4000000,
                "Project type": "Residential Complex",
                "Phases": "Phase 1 to Phase 3",
                "Submission deadline": "2025-10-15"
            }
        elif "Cologne" in tender_text:
            data = {
                "Project name": "Cologne Office Complex Development",
                "location": "Cologne",
                "Budget": 3500000,
                "Project type": "Office Complex",
                "Phases": "Phase 1 to Phase 4",
                "Submission deadline": "2025-10-01"
            }

        return json.dumps(data)
    else:
        raise NotImplementedError("Only mock mode supported without API key")

# import json
# import os

# def extract_fields_from_tender(tender_text, model="mock"):
#     if model == "mock":
#         if "Berlin" in tender_text:
#             return json.dumps({
#                 "Project name": "Municipal Library Construction",
#                 "location": "Berlin",
#                 "Budget": 2500000,
#                 "Project type": "Library Construction",
#                 "Phases": "Planning, Execution, Commissioning",
#                 "Submission deadline": "2025-06-15"
#             })
#         elif "Munich" in tender_text:
#             return json.dumps({
#                 "Project name": "Healthcare Facility in Munich",
#                 "location": "Munich",
#                 "Budget": 3100000,
#                 "Project type": "Hospital",
#                 "Phases": "Phase 1 to Phase 5",
#                 "Submission deadline": "2025-07-30"
#             })
#         elif "Stuttgart" in tender_text:
#             return json.dumps({
#                 "Project name": "Refurbishment of Historic Theatre",
#                 "location": "Stuttgart",
#                 "Budget": 1800000,
#                 "Project type": "Theatre Refurbishment",
#                 "Phases": "Planning, Interior Remodeling, Electrical Upgrades",
#                 "Submission deadline": "2025-08-10"
#             })
#         elif "Hamburg" in tender_text:
#             return {
#                 "Project name": "Hamburg School Modernization",
#                 "location": "Hamburg",
#                 "Budget": 1500000,
#                 "Project type": "School Renovation",
#                 "Phases": "Execution, Interior Updates",
#                 "Submission deadline": "2025-09-15"
#             }
#         elif "Frankfurt" in tender_text:
#             return {
#                 "Project name": "Frankfurt Urban Park Development",
#                 "location": "Frankfurt",
#                 "Budget": 2000000,
#                 "Project type": "Urban Park",
#                 "Phases": "Design, Construction",
#                 "Submission deadline": "2025-09-30"
#             }
#         elif "Düsseldorf" in tender_text:
#             return {
#                 "Project name": "Düsseldorf Residential Complex",
#                 "location": "Düsseldorf",
#                 "Budget": 4000000,
#                 "Project type": "Residential Complex",
#                 "Phases": "Phase 1 to Phase 3",
#                 "Submission deadline": "2025-10-15"
#             }
#         elif "Cologne" in tender_text:
#             return {
#                 "Project name": "Cologne Office Complex Development",
#                 "location": "Cologne",
#                 "Budget": 3500000,
#                 "Project type": "Office Complex",
#                 "Phases": "Phase 1 to Phase 4",
#                 "Submission deadline": "2025-10-01"
#             }
#         else:
#             return json.dumps({})
#     else:
#         raise NotImplementedError("Only mock mode supported without API key")
