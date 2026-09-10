from fastapi import APIRouter
from pydantic import BaseModel

from app.llm.ollama import chat

router = APIRouter(prefix="/api")


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful and intelligentpersonal AI assistant.",
        },
        {
            "role": "user",
            "content": request.message,
        },
    ]
    answer = await chat(messages)
    return {"response": answer}