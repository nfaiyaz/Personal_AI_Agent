from fastapi import FastAPI

from app.api.conversations import router as conversations_router
from app.api.memories import router as memories_router


app = FastAPI(
    title="Personal AI Agent API",
    version="0.1.0",
)


app.include_router(conversations_router)
app.include_router(memories_router)


@app.get("/health")
async def health():
    return {"status": "ok"}