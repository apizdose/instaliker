FROM python:3-slim
COPY ./* /liker/
WORKDIR /liker 
RUN pip install requests
ENTRYPOINT ["python", "instaliker.py"] 
