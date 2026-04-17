FROM python:3.11-slim

WORKDIR /app

# éviter problèmes d'encodage + logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# copier requirements
COPY requirements.txt .

# upgrade pip + install deps
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# copier le code
COPY . .

EXPOSE 8003

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8003"]