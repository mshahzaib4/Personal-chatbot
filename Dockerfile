FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Debug: Show contents of requirements.txt
RUN cat requirements.txt

# Update pip and install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]