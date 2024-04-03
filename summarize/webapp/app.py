from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
generator = pipeline("text-generation", model="gpt2")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google-t5/t5-small")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, truncation = True, framework="tf")

app = FastAPI()

class GenerateBody(BaseModel):
    text: str

class SummarizeBody(BaseModel):
    text: str

@app.get('/')
def root():
    return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and generate text, and t5 to summarize </h1>")

@app.post("/generate")
def predict(body: GenerateBody):
    results = generator(body.text, max_length=50, num_return_sequences=1)
    return results[0]  

@app.post("/summarize/")
def summarize_text(body: SummarizeBody):
    summary = summarizer(body.text, max_length=50, min_length=10, do_sample=False)
    return summary[0]   #{"summary": summary[0]['summary_text']}

if __name__ == "__main__":
   uvicorn.run(app, host="localhost", port=9003)
