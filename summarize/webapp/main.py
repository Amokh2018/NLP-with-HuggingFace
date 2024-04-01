from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
generator = pipeline("text-generation", model="gpt2")

app = FastAPI()

class Body(BaseModel):
    text: str

@app.get('/')
def root():
    return HTMLResponse("<h1>A self-documenting API to interact with a GPT2 model and generate text </h1>")

@app.post("/generate")
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]  


if __name__ == "__main__":
   uvicorn.run(app, host="localhost", port=9000)
