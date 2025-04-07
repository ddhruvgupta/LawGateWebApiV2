FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y netcat-openbsd iputils-ping curl && rm -rf /var/lib/apt/lists/*

RUN chmod +x wait-for-db.sh

ENTRYPOINT ["./wait-for-db.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]
