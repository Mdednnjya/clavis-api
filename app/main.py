from fastapi import FastAPI
from app.api.endpoints import router as summarization_router

app = FastAPI(title="Clavis API")

app.include_router(summarization_router, prefix="/api/v1", tags=["summarization"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clavis API"}