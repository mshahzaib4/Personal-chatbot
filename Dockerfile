FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

# my python version in vu env is Python 3.10.19 but docker hub  3.9-slim is working fine?
