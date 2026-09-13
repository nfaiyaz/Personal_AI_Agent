from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Conversation, Message


async def create_conversation(
    session: AsyncSession,
    title: str | None = None,
) -> Conversation:
    conversation = Conversation(
        title=title,
    )

    session.add(conversation)

    await session.commit()
    await session.refresh(conversation)

    return conversation


async def add_message(
    session: AsyncSession,
    conversation_id: int,
    role: str,
    content: str,
) -> Message:
    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
    )

    session.add(message)

    await session.commit()
    await session.refresh(message)

    return message


async def get_messages(
    session: AsyncSession,
    conversation_id: int,
) -> list[Message]:
    result = await session.execute(
        select(Message)
        .where(
            Message.conversation_id == conversation_id
        )
        .order_by(Message.created_at)
    )

    return list(result.scalars().all())