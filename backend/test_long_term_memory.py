import asyncio

from app.db.database import SessionLocal
from app.memory.long_term import (
    get_all_memories,
    save_memory,
)


async def main():
    async with SessionLocal() as session:

        # Save memories
        await save_memory(
            session,
            "User prefers Python examples.",
        )

        await save_memory(
            session,
            "User is learning FastAPI.",
        )

        # Retrieve memories
        memories = await get_all_memories(
            session
        )

        print("Long-term memories:")

        for memory in memories:
            print(
                f"[{memory.id}] "
                f"{memory.content} "
                f"({memory.created_at})"
            )


if __name__ == "__main__":
    asyncio.run(main())