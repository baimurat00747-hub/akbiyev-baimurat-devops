FROM python:3.12-slim AS base

WORKDIR /app

COPY app/ /app/

RUN python -m compileall -q /app


FROM base AS test

RUN python -m unittest discover \
    -s /app \
    -p "test_*.py" \
    -v


FROM test AS runtime

EXPOSE 8000

CMD ["python", "-u", "app.py"]
