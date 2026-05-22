import pandas as pd
import numpy as np
import faiss
import joblib
from sentence_transformers import SentenceTransformer
from collections import Counter
import re

# Load saved assets
df = joblib.load("legal_dataset.pkl")
index = joblib.load("faiss_index.pkl")

# Load embedding model
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

# -------------------------------
# Extract legal sections
# -------------------------------

def extract_sections(section_text):

    if pd.isna(section_text):
        return []

    text = str(section_text)

    extracted = []

    ipc_matches = re.findall(
        r'IPC Sections? ([0-9A-Za-z(), ]+)',
        text
    )

    for match in ipc_matches:

        nums = match.split(',')

        for num in nums:

            num = num.strip()

            if num:
                extracted.append(f"IPC {num}")

    return extracted

# -------------------------------
# Similar case retrieval
# -------------------------------

def retrieve_similar_cases(query, top_k=5):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype('float32'),
        k=top_k
    )

    results = []

    for idx in I[0]:

        results.append({

            "case_title":
                df.iloc[idx]["case_title"],

            "case_type":
                df.iloc[idx]["case_type"],

            "legal_sections":
                df.iloc[idx]["legal_sections"],

            "judgment_outcome":
                df.iloc[idx]["judgment_outcome"]

        })

    return results

# -------------------------------
# Predict legal sections
# -------------------------------

def predict_legal_sections(query, top_k=5):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype('float32'),
        k=top_k
    )

    weighted_sections = {}

    for position, idx in enumerate(I[0]):

        distance = D[0][position]

        weight = 1 / (1 + distance)

        sections = extract_sections(
            df.iloc[idx]['legal_sections']
        )

        for sec in sections:

            if sec not in weighted_sections:
                weighted_sections[sec] = 0

            weighted_sections[sec] += weight

    total_weight = sum(weighted_sections.values())

    results = []

    for sec, score in weighted_sections.items():

        confidence = round(
            float((score / total_weight) * 100),
            2
        )

        results.append({

            "section": sec,
            "confidence": confidence

        })

    results.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return results