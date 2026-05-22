from flask import Flask, request, jsonify

from ml_engine import (
    retrieve_similar_cases,
    predict_legal_sections,
    detect_missing_evidence,
    judgment_pattern_analytics,
    evidence_law_mapping
)

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_case():

    data = request.json

    query = data.get("query")

    similar_cases = retrieve_similar_cases(query)

    sections = predict_legal_sections(query)

    missing_evidence = detect_missing_evidence(query)

    analytics = judgment_pattern_analytics(query)

    evidence_mapping = evidence_law_mapping(query)

    return jsonify({

    "similar_cases": similar_cases,

    "predicted_sections": sections,

    "missing_evidence": missing_evidence,

    "judgment_analytics": analytics,

    "evidence_law_mapping": evidence_mapping

})

if __name__ == "__main__":

    app.run(debug=True)