from flask import Flask, request, jsonify

from ml_engine import (
    retrieve_similar_cases,
    predict_legal_sections
)

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])

def analyze_case():

    data = request.json

    query = data.get("query")

    similar_cases = retrieve_similar_cases(query)

    sections = predict_legal_sections(query)

    return jsonify({

        "similar_cases": similar_cases,

        "predicted_sections": sections

    })

if __name__ == "__main__":

    app.run(debug=True)