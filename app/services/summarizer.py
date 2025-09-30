from transformers import pipeline
import PyPDF2
import io 

class SummarizationService:
    def __init__(self):
            self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def generateSummary(self, file_bytes: bytes) -> str:
          # Extract text from PDF file in bytes and return a summary
            try:
                pdf_file = io.BytesIO(file_bytes)
                reader = PyPDF2.PdfReader(pdf_file)
            
                full_text = ""
                for page in reader.pages:
                      page_text = page.extract_text()
                      if page_text():
                            full_text += page_text + "\n"

                # chunking the data into model since we have a limited token 
                summary = self.summarizer(full_text, max_length=250, min_length=50, do_sample=False)

                return summary[0]['summary_text']            
            except Exception as e:
                  print("An error occurred: {e}")
                  return "Error: Could not process the PDF files."
            

summarization_service = SummarizationService()