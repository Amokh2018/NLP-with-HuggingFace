FROM python:3.8
COPY ./summarize/webapp/requirements.txt ./webapp/requirements.txt 
WORKDIR /webapp
COPY summarize/webapp/* /webapp

RUN pip install -r requirements.txt
#ENTRYPOINT ["uvicorn"]
CMD ["python3","app.py"]