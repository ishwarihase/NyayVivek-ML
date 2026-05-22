# NyayVivek

NyayVivek is an AI-assisted legal intelligence and case analysis platform designed to help users analyze complex legal documents, retrieve similar judgments, detect contradictions, identify missing evidence, and generate structured legal insights from judicial case materials.

The platform focuses on combining legal NLP, semantic retrieval, and analytical reasoning into a unified legal intelligence workflow.

## Current Features

### Applicable Legal Section Detection

Identifies relevant IPC and CrPC sections from uploaded judgment documents and legal text.

### Similar Case Retrieval

Uses semantic embeddings and FAISS vector search to retrieve contextually similar legal cases and judgments.

### Missing Evidence Detection

Analyzes case narratives and identifies potentially missing supporting evidence or investigative gaps.

### Legal Text Processing

Preprocesses and structures legal judgment text for downstream analytical tasks.

## Planned Features

* Contradiction Detection
* Evidence-to-Law Mapping
* AI Case Summarization
* Timeline Reconstruction
* Multi-document Analysis
* Dashboard Integration
* API-based Processing Pipeline
* Secure Legal Workspace

## Workflow

```text
Judgment PDF
      ↓
Text Extraction
      ↓
Legal NLP Processing
      ↓
Embedding Generation
      ↓
AI Legal Analysis
      ↓
Structured Intelligence Outputs
```

## Current Project Structure

```text
laww/
│
├── backend/
├── frontend/
├── ml/
│   ├── nyayvivek_legal_analysis_pipeline.ipynb
│   ├── requirements.txt
│   ├── sample_cases/
│   └── README.md
```

## Tech Stack

### Machine Learning / NLP

* SentenceTransformers
* FAISS
* Scikit-learn
* Transformers

### Backend

* Python
* Flask / FastAPI (planned)

### Frontend

* React (planned)

## Current MVP Direction

The current MVP focuses primarily on judgment-based legal analysis using publicly available court judgments and structured legal documents.

The platform currently prioritizes:

* semantic legal understanding
* precedent retrieval
* section detection
* investigative insight generation

before expanding into full confidential case workflows.

## Installation

```bash
git clone https://github.com/Rishi-baba/laww.git
cd laww
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Future Vision

NyayVivek aims to evolve into a comprehensive legal intelligence workspace capable of assisting with:

* legal document understanding
* precedent analysis
* contradiction identification
* evidence structuring
* judicial insight generation

through modern AI-assisted workflows.

## Contributor

* Isha Singh

```
```
