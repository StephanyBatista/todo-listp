from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions import BusinessError, NotFoundError
from routes.router import router as tasks_router

app = FastAPI(title="Todo List")


@app.exception_handler(NotFoundError)
def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(BusinessError)
def business_handler(request: Request, exc: BusinessError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})


@app.get("/health")
def health_check():
    return {"status": "production"}


app.include_router(tasks_router)
