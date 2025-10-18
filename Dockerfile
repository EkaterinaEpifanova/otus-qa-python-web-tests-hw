FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /src/test

COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["pytest", "src/test/"]