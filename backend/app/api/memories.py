from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.memory.long_term import (
    get_all_memories,
    save_memory,
)


class MemoryRequest(BaseModel):
    content: str


router = APIRouter(
    prefix="/memories",
    tags=["Long-Term Memory"],
)


@router.post("/")
async def create_memory(
    memory: MemoryRequest,
    session: AsyncSession = Depends(get_db),
):
    saved_memory = await save_memory(
        session,
        memory.content,
    )

    return {
        "id": saved_memory.id,
        "content": saved_memory.content,
        "created_at": saved_memory.created_at,
    }


@router.get("/")
async def list_memories(
    session: AsyncSession = Depends(get_db),
):
    memories = await get_all_memories(
        session
    )

    return [
        {
            "id": memory.id,
            "content": memory.content,
            "created_at": memory.created_at,
        }
        for memory in memories
    ]