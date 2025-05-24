from fastapi import FastAPI, BackgroundTasks
import asyncio
import time

app = FastAPI()



def sync_task():
    time.sleep(3)
    print("отправлен email")


async def async_task():
    await asyncio.sleep(3)
    print("сделан запрос в сторонний api")


@app.post("/async")
async def some_async_route():
    ...
    asyncio.create_task(async_task())
    return {"ok": True}

@app.post("/sync")
async def some_sync_route(bg_tasks: BackgroundTasks):
    ...
    bg_tasks.add_task(sync_task)
    return {"ok": True}
