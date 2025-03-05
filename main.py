# main.py
from fastapi import FastAPI
from router.task import router as task_router  # import router จาก tasks.py

app = FastAPI(
    title="Todo API",
    description="This is a simple API for managing a Todo list.",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

# รวม router จาก tasks.py เข้ากับ app
app.include_router(task_router)
