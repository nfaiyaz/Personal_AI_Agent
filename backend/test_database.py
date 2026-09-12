import asyncio

from sqlalchemy import select

from app.db.database import SessionLocal
from app.db.models import TestRecord


async def main():
    async with SessionLocal() as session:
        record = TestRecord(
            name="My first AI agent record"
        )

        session.add(record)

        await session.commit()
        await session.refresh(record)

        print("Created record:")
        print("ID:", record.id)
        print("Name:", record.name)
        print("Created:", record.created_at)

        result = await session.execute(
            select(TestRecord)
        )

        records = result.scalars().all()

        print("\nAll records:")

        for item in records:
            print(
                item.id,
                item.name,
                item.created_at,
            )


if __name__ == "__main__":
    asyncio.run(main())