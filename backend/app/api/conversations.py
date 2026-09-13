from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.memory.conversation import (
    create_conversation,
    get_messages,
)


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