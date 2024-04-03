from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google-t5/t5-small")

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, truncation = True, framework="tf")
with open("./summarize/input.txt","r") as _f:
    print(summarizer(_f.read()))