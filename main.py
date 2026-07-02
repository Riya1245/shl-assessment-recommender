from fastapi import FastAPI
from app.models import ChatRequest, ChatResponse, Recommendation
from app.chatbot import generate_response

app = FastAPI(
    title="SHL Assessment Recommender API",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = generate_response(request.messages)

    recommendations = [
        Recommendation(
            name=item["name"],
            url=item["url"],
            test_type=item["test_type"]
        )
        for item in result["recommendations"]
    ]

    return ChatResponse(
        reply=result["reply"],
        recommendations=recommendations,
        end_of_conversation=result["end_of_conversation"]
    )