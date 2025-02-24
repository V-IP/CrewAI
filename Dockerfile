FROM python:3.11.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env

EXPOSE 80

CMD ["python", "src/testam/main.py"]
