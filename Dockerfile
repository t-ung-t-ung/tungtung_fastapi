FROM python:3.11

WORKDIR /workspace

RUN pip install --no-cache-dir \
    fastapi uvicorn[standard] \
    sqlmodel pymysql \
    python-jose[cryptography] httpx \
    passlib

ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0"]