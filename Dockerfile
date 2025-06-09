FROM python:3.9

WORKDIR /app

# Установка Poetry
RUN pip install poetry

# Копируем зависимости
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY . /app/

EXPOSE 8000