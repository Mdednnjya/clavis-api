from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.summarizer import summarization_service

router = APIRouter()

@router.post("/summarize")
async def create_summary(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF.")
    
    file_bytes = await file.read()

    summary_text = summarization_service.generateSummary(file_bytes)

    if "Error:" in summary_text:
        raise HTTPException(status_code=500, detail=summary_text)
    
    return {"filename": file.filename, "summary": summary_text}