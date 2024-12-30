FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY code /app/code
COPY data /app/data
COPY scripts /app/scripts
COPY environment /app/environment

# Add any other necessary setup commands

CMD ["python", "code/main.py"] # Or whatever your main entry point is
