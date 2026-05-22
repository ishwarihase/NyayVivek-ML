from ml_engine import (
    retrieve_similar_cases,
    predict_legal_sections
)

query = """
The accused was involved in a murder case.
Eyewitnesses and medical evidence were presented.
"""

# Similar cases
similar_cases = retrieve_similar_cases(query)

print("\nSIMILAR CASES:\n")

for case in similar_cases:

    print(case)

# Legal sections
sections = predict_legal_sections(query)

print("\nPREDICTED SECTIONS:\n")

for sec in sections:

    print(sec)