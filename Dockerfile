FROM python:3.10-slim

WORKDIR /app

COPY app/main.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask prometheus-flask-exporter

COPY ./app /app

CMD ["python", "main.py"]
