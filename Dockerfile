FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install Flask
RUN pip install gunicorn

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["python", "server.py"]
