FROM python:slim

RUN pip install -r requirements.txt
WORKDIR /tgbot 
COPY . .
ENTRYPOINT ["python", "tgbot.py"]
