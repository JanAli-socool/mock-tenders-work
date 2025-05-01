from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compute_similarity(tender, reference_row):
    text1 = f"{tender['location']} {tender['Budget']} {tender['Project type']} {tender['Phases']}"
    text2 = f"{reference_row['location']} {reference_row['budget']} {reference_row['project_type']} {reference_row['phases']}"
    return text1, text2

def rank_references(tender, reference_df):
    scores = []
    tfidf = TfidfVectorizer().fit([f"{tender['location']} {tender['Project type']} {tender['Phases']}"] +
                                  reference_df.apply(lambda x: f"{x['location']} {x['project_type']} {x['phases']}", axis=1).tolist())
    for _, ref in reference_df.iterrows():
        t1, t2 = compute_similarity(tender, ref)
        vecs = tfidf.transform([t1, t2])
        score = cosine_similarity(vecs[0], vecs[1])[0][0]
        scores.append((ref, score))
    ranked = sorted(scores, key=lambda x: x[1], reverse=True)
    return ranked[:3]
