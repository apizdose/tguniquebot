FROM python:slim

WORKDIR /tgbot 
COPY . .
RUN pip install -r requirements.txt && mkdir photos
ENTRYPOINT ["python", "tgbot.py"]
