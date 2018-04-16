FROM python:3-jessie

RUN echo "deb http://http.debian.net/debian jessie-backports main contrib non-free" > /etc/apt/sources.list.d/backports.list
RUN apt update && apt install -y prometheus-node-exporter
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
CMD bash /app/run.sh
