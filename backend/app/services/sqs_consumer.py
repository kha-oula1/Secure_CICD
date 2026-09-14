import asyncio


async def sqs_poll_loop() -> None:
    while True:
        await asyncio.sleep(60)
