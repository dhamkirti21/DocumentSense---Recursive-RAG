# ---- Base Image ----
FROM python:3.11-slim

# ---- System Dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Work Directory ----
WORKDIR /app

# ---- Copy Requirements First (Layer Caching) ----
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy Project ----
COPY . .

# ---- Expose Port ----
EXPOSE 8000

# ---- Environment Variables ----
ENV PYTHONUNBUFFERED=1

# ---- Run Server ----
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]