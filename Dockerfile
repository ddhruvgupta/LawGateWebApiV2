FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install dos2unix and other necessary tools
RUN apt-get update && apt-get install -y \
    dos2unix \
    netcat-openbsd \
    iputils-ping \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Convert wait-for-db.sh to Unix-style line endings
RUN dos2unix wait-for-db.sh

RUN chmod +x wait-for-db.sh

ENTRYPOINT ["./wait-for-db.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]
