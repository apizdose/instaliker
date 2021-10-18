FROM python:slim

RUN pip install requests
WORKDIR /liker 
COPY . .
ENTRYPOINT ["python", "instaliker.py"]
