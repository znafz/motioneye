FROM arm32v7/debian:jessie-slim

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY . .

CMD [ "python3", "-u", "run.py" ]