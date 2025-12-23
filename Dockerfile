FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# FIX: Upgrade pip first to avoid compatibility issues
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Note: Your app runs on port 5000 but CICD maps to 8080
EXPOSE 5000

CMD ["python", "app.py"]