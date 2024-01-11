FROM python:3

RUN apt-get update && apt-get install -y \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD Xvfb :99 -screen 0 1024x768x16 & \
    export DISPLAY=:99 && \
    python ./UserInterface.py 