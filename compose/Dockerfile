    FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ../requirements/ requirements/

RUN pip install --upgrade pip
RUN pip install -r /requirements/base.txt

COPY ../compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ../compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
COPY ./ ./

CMD [ "/entrypoint" ]
