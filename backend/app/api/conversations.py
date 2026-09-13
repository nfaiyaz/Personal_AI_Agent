from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.memory.conversation import (
    add_message,
    create_conversation,
    get_messages,
)


class MessageRequest(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)


@router.post("/")
async def create_new_conversation(
    title: str | None = None,
    session: AsyncSession = Depends(get_db),
):
    conversation = await create_conversation(
        session,
        title=title,
    )

    return {
        "id": conversation.id,
        "title": conversation.title,
        "created_at": conversation.created_at,
    }


@router.post("/{conversation_id}/messages")
async def save_conversation_message(
    conversation_id: int,
    message: MessageRequest,
    session: AsyncSession = Depends(get_db),
):
    saved_message = await add_message(
        session,
        conversation_id,
        message.role,
        message.content,
    )

    return {
        "id": saved_message.id,
        "conversation_id": saved_message.conversation_id,
        "role": saved_message.role,
        "content": saved_message.content,
        "created_at": saved_message.created_at,
    }


@router.get("/{conversation_id}/messages")
async def get_conversation_messages(
    conversation_id: int,
    session: AsyncSession = Depends(get_db),
):
    messages = await get_messages(
        session,
        conversation_id,
    )

    if not messages:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found or has no messages.",
        )

    return [
        {
            "id": message.id,
            "role": message.role,
            "content": message.content,
            "created_at": message.created_at,
        }
        for message in messages
    ]