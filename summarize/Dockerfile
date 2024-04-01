FROM python:3.8
COPY ./webapp/requirements.txt ./webapp/requirements.txt 
WORKDIR /webapp
COPY webapp/* /webapp

RUN pip install -r requirements.txt
#ENTRYPOINT ["uvicorn"]
CMD ["python3","main.py"]