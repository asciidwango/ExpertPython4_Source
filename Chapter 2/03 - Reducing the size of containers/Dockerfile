FROM alpine:3.16
WORKDIR /app/

RUN apk add --no-cache python3

COPY requirements.txt .

RUN apk add --no-cache py3-pip && \
    pip3 install -r requirements.txt && \
    apk del py3-pip

COPY echo.py .
CMD ["python3", "echo.py"]
