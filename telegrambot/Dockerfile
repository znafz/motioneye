FROM resin/raspberry-pi-debian

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY . .

RUN pip3 install telepot

CMD [ "python3", "-u", "run.py" ]ls