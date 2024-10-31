FROM python:3.10-slim

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure the ca.pem file is copied to the correct location
COPY app/core/ca.pem /backend/app/core/ca.pem

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]