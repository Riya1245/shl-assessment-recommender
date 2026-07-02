Added the complete SHL Assessment Recommender project with API, retrieval logic, chatbot, and documentation.
# SHL Assessment Recommender

## Overview
This project is a conversational SHL Assessment Recommender API built using FastAPI, Python, retrieval based recommendation, and Google Gemini.

The API recommends relevant SHL assessments based on user queries, asks clarifying questions when needed, compares assessments, and handles off topic or prompt injection attempts.

## Features

- Conversational recommendation API
- SHL catalog retrieval
- Clarifying questions
- Assessment comparison
- Prompt injection protection
- Off topic detection
- Gemini powered response generation
- FastAPI REST API

## Tech Stack

- Python
- FastAPI
- Google Gemini
- JSON Catalog
- Uvicorn

## API Endpoints

### GET /health

Returns the API health status.

### POST /chat

Accepts a user query and returns relevant SHL assessment recommendations.

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I need a Java developer assessment for a mid level candidate"
    }
  ]
}
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Repository

Contains the complete implementation submitted for the SHL Assessment Recommender assignment.
