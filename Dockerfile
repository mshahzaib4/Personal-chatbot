FROM python:3.9-slim

WORKDIR /app

# Install Flask directly without requirements.txt
RUN pip install --no-cache-dir Flask==3.1.1

COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]