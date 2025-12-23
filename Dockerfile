FROM python:3.9-slim

WORKDIR /app

# Copy everything
COPY . /app

# Debug: Show the problematic line
RUN echo "=== Checking requirements.txt ===" && \
    cat requirements.txt && \
    echo "=== End of requirements.txt ==="

# Fix pip and install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]