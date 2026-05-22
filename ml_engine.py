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

def detect_missing_evidence(query, top_k=5):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype('float32'),
        k=top_k
    )

    all_evidence = []

    for idx in I[0]:

        evidence_text = str(
            df.iloc[idx]["evidence_types"]
        )

        evidence_list = evidence_text.split(',')

        for ev in evidence_list:

            ev = ev.strip().lower()

            if ev:
                all_evidence.append(ev)

    evidence_counts = Counter(all_evidence)

    query_lower = query.lower()

    missing = []

    for evidence, count in evidence_counts.items():

        if count >= 2 and evidence not in query_lower:

            missing.append(evidence)

    return list(set(missing))



def judgment_pattern_analytics(query, top_k=5):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype('float32'),
        k=top_k
    )

    outcome_list = []

    for idx in I[0]:

        outcome = str(
            df.iloc[idx]["judgment_outcome"]
        ).strip()

        if outcome and outcome.lower() != "nan":

            outcome_list.append(outcome)

    outcome_counts = Counter(outcome_list)

    total = sum(outcome_counts.values())

    results = []

    for outcome, count in outcome_counts.items():

        percentage = round(
            (count / total) * 100,
            2
        )

        results.append({

            "outcome": outcome,

            "percentage": percentage

        })

    results.sort(
        key=lambda x: x["percentage"],
        reverse=True
    )

    return results



from collections import defaultdict

def evidence_law_mapping(query, top_k=5):

    query_embedding = model.encode([query])

    D, I = index.search(
        np.array(query_embedding).astype('float32'),
        k=top_k
    )

    evidence_map = defaultdict(list)

    for idx in I[0]:

        evidence_text = str(
            df.iloc[idx]["evidence_types"]
        )

        legal_text = str(
            df.iloc[idx]["legal_sections"]
        )

        evidence_list = evidence_text.split(',')

        law_list = legal_text.split(',')

        cleaned_laws = []

        for law in law_list:

            law = law.strip()

            if law and law.lower() != "nan":

                cleaned_laws.append(law)

        for ev in evidence_list:

            ev = ev.strip()

            if not ev:
                continue

            evidence_map[ev].extend(
                cleaned_laws
            )

    results = []

    for evidence, laws in evidence_map.items():

        law_counts = Counter(laws)

        top_laws = []

        for law, count in law_counts.items():

            if count >= 2:

                top_laws.append(law)

        if len(top_laws) == 0:
            continue

        results.append({

            "evidence": evidence,

            "related_laws": top_laws

        })

    return results