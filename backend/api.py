#uvicorn api:app --reload --port 8000
#npm run dev

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from ocr import extract_text_from_image
from llm import ask_llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or list your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.post("/process")
async def process_image(file: UploadFile = File(...), question: str = Form(...)):
    content = await file.read()
    ocr_text = extract_text_from_image(content)
    answer = ask_llm(ocr_text, question)
    print(answer)
    return {
        "ocr_text": ocr_text,
        "answer": answer
    }
