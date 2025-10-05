FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    firefox-esr \
    xvfb fonts-liberation tzdata ca-certificates curl \
 && rm -rf /var/lib/apt/lists/*

RUN curl -L -o geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz \
    && tar -zxvf geckodriver.tar.gz \
    && mv geckodriver /usr/local/bin \
    && chmod +x /usr/local/bin/geckodriver

ENV CHROME_BIN=/usr/bin/chromium \
    CHROMEDRIVER=/usr/bin/chromedriver \
    FIREFOX_BIN=/usr/bin/firefox-esr \
    GECKODRIVER=/usr/bin/geckodriver

WORKDIR /src/test

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["pytest"]