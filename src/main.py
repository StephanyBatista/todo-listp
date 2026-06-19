from fastapi import FastAPI

from routes.router import router as tasks_router

app = FastAPI(title="Todo List")


@app.get("/health")
def health_check():
    return {"status": "production"}


app.include_router(tasks_router)
