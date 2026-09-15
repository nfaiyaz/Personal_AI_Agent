from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import LongTermMemory


async def save_memory(
    session: AsyncSession,
    content: str,
) -> LongTermMemory:
    memory = LongTermMemory(
        content=content,
    )

    session.add(memory)

    await session.commit()
    await session.refresh(memory)

    return memory


async def get_all_memories(
    session: AsyncSession,
) -> list[LongTermMemory]:
    result = await session.execute(
        select(LongTermMemory)
        .order_by(LongTermMemory.created_at)
    )

    return list(result.scalars().all())