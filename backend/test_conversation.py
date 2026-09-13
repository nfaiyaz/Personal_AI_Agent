import asyncio

from app.db.database import SessionLocal
from app.memory.conversation import (
    add_message,
    create_conversation,
    get_messages,
)


async def main():
    async with SessionLocal() as session:

        # Create a new conversation
        conversation = await create_conversation(
            session,
            title="My First AI Conversation",
        )

        print("Conversation created:")
        print("ID:", conversation.id)
        print("Title:", conversation.title)

        # Add user message
        await add_message(
            session,
            conversation.id,
            "user",
            "Hello! What is FastAPI?",
        )

        # Add assistant message
        await add_message(
            session,
            conversation.id,
            "assistant",
            "FastAPI is a Python web framework.",
        )

        # Retrieve conversation messages
        messages = await get_messages(
            session,
            conversation.id,
        )

        print("\nConversation messages:")

        for message in messages:
            print(
                f"[{message.role}] {message.content}"
            )


if __name__ == "__main__":
    asyncio.run(main())