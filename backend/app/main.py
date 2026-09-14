import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = None
    if settings.upload_queue_url:
        from app.services.sqs_consumer import sqs_poll_loop

        task = asyncio.create_task(sqs_poll_loop())

    yield

    if task is not None:
        task.cancel()


app = FastAPI(lifespan=lifespan)