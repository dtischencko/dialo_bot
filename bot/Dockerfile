FROM python:3.8-slim
LABEL authors="dity"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]