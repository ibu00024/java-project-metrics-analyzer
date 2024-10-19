FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential gcc git \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for the logs
RUN mkdir -p /var/log/uwsgi

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run the application with uwsgi
CMD ["uwsgi", "--ini", "uwsgi.ini"]
