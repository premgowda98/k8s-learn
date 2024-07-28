FROM python:3.10.14-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8502
CMD ["python3", "main.py"]