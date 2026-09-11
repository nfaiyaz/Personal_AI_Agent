from pathlib import Path

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# SQLite database location
DATABASE_PATH = PROJECT_ROOT / "data" / "agent.db"

# Make sure the data directory exists
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

# SQLite connection URL
DATABASE_URL = f"sqlite+aiosqlite:///{DATABASE_PATH}"


engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)


SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with SessionLocal() as session:
        yield session


async def init_db():
    from app.db import models

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)