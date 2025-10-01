from transformers import pipeline
import PyPDF2
import io 
import torch

class SummarizationService:
    def __init__(self):
            # using GPU if exist (through CUDA)
            device = 0 if torch.cuda.is_available() else -1
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

    def generateSummary(self, file_bytes: bytes) -> str:
          # Extract text from PDF file in bytes and return a summary
            try:
                pdf_file = io.BytesIO(file_bytes)
                reader = PyPDF2.PdfReader(pdf_file)
            
                full_text = ""
                for page in reader.pages:
                      page_text = page.extract_text()
                      if page_text:
                            full_text += page_text + "\n"

                # chunking the data into model since we have a limited token 
                chunks = [full_text[i:i+2000] for i in range (0, len(full_text), 2000)]

                # to store the post summary text
                summaries = []

                # core logic on inserting chunk data into model
                for chunk in chunks:
                      if chunk.strip():
                            summary = self.summarizer(chunk, max_length=250, min_length=50, do_sample=False)
                            summaries.append(summary[0]['summary_text'])


                return " ".join(summaries)            
            except Exception as e:
                  print(f"An error occurred: {e}")
                  return "Error: Could not process the PDF file."
            

summarization_service = SummarizationService()