FROM python:3.9-slim-buster

WORKDIR /app

COPY model/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN python model/main.py

EXPOSE 5000

CMD ["python", "app.py"]