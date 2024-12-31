FROM python:3.8

WORKDIR /app

COPY environment/requirements.txt .
RUN pip install -r requirements.txt

COPY code /app/code

# Add any other necessary setup commands

CMD ["python", "code/main.py"] # Or whatever your main entry point is
