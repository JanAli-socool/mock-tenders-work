import streamlit as st
import pandas as pd
from extract_fields import extract_fields_from_tender
from match_refreneces import match_references
import json

with open("data/mock_tenders_raw.txt", "r") as f:
    raw_tenders = f.read().split("\n\n")

tenders = [extract_fields_from_tender(t) for t in raw_tenders]
tenders = [
    result if isinstance(result := extract_fields_from_tender(t), dict) else json.loads(result)
    for t in raw_tenders
]

df_tenders = pd.DataFrame(tenders)
ref_df = pd.read_excel("data/refrences.xlsx")

st.title("Mini TED Tender Parser")

filter_location = st.selectbox("Filter by Location", options=["All"] + list(df_tenders["location"].unique()))
filter_type = st.selectbox("Filter by Project Type", options=["All"] + list(df_tenders["Project type"].unique()))

filtered = df_tenders.copy()
if filter_location != "All":
    filtered = filtered[filtered["location"] == filter_location]
if filter_type != "All":
    filtered = filtered[filtered["Project type"] == filter_type]

st.dataframe(filtered)

selected = st.selectbox("Select a Tender", options=filtered["Project name"])
#tender = df_tenders[df_tenders["Project name"] == selected].iloc[0].to_dict()
#tender = next(t for t in tenders if t["Project name"] == selected)
selected_df = df_tenders[df_tenders["Project name"] == selected]

if selected_df.empty:
    st.warning("Selected tender not found in dataset.")
    st.stop()

tender = selected_df.iloc[0].to_dict()


matches = match_references(tender, ref_df)

st.subheader("Tender Details")
st.json(tender)

st.subheader("Top 3 Matching References")
for m in matches:
    st.write(f"**Score**: {m['score']} — {m['reference']['project_type']}")
    st.write(f"*Reasoning*: {m['reasoning']}")

st.download_button("Download as CSV", filtered.to_csv(index=False), file_name="tenders.csv")
