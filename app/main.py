from fastapi import FastAPI
from app.api.endpoints import router as summarization_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Clavis API")

# CORS config
origins = [
    "http://localhost:3000",
    "http://localhost",
    "https://clavis-app.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(summarization_router, prefix="/api/v1", tags=["summarization"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Clavis API"}