import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(tender, reference_row):
    tender_text = f"{tender['location']} {tender['Budget']} {tender['Project type']} {tender['Phases']}"
    ref_text = f"{reference_row['location']} {reference_row['budget']} {reference_row['project_type']} {reference_row['phases']}"
    vectorizer = TfidfVectorizer().fit([tender_text, ref_text])
    tfidf_matrix = vectorizer.transform([tender_text, ref_text])
    return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

def match_references(tender, references_df):
    matches = []
    for _, ref in references_df.iterrows():
        score = compute_similarity(tender, ref)
        matches.append({
            "reference": ref.to_dict(),
            "score": round(score, 2),
            "reasoning": f"Similarity between tender '{tender['Project name']}' and reference '{ref['project_type']}' is based on budget, location, and phase alignment."
        })
    return sorted(matches, key=lambda x: x["score"], reverse=True)[:3]
