FROM python:3.9

ENV PYTHONDONTWRITEBYTEapp 1
ENV PYTHONBUFFERED 1

# Set project active directory
WORKDIR /app

# Curl install poetry and set configs
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.1.12 python3 -
ENV PATH /root/.local/bin:$PATH
RUN poetry config virtualenvs.create false


COPY . .
RUN rm -rf poetry.lock

#Installing dependencies
RUN poetry install --no-interaction --ansi --no-root

# expose the port that uvicorn will run the app on
EXPOSE 8000

# execute the command python main.py (in the WORKDIR) to start the app
ENV PYTHONPATH=/app