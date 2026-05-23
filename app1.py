from fastapi import FastAPI

from pydantic import BaseModel

from ml_model import analyze_case


# Create FastAPI app
app = FastAPI()


# Input structure
class CaseInput(BaseModel):

    query: str


# Home route
@app.get("/")

def home():

    return {

        "message":
        "NyayaVivek API Running"
    }


# Main analysis route
@app.post("/analyze_case")

def analyze(data: CaseInput):

    results = analyze_case(
        data.query
    )

    return results
