FROM python:3.11-slim

WORKDIR /app

COPY . .

#compile dependency on tgt platform
RUN pip install pip==25 #lock to 25 for now, 25.3 (released 25oct) has some comp issues when doing pip-compile
RUN pip install pip-tools
RUN pip-compile requirements.in
RUN cat requirements.txt
#do not store cache
RUN pip install --no-cache-dir -r requirements.txt

#clean up some space
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip cache purge

#Set env vars
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
EXPOSE 8080

CMD ["python", "main.py"]
