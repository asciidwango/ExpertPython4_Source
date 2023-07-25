# "slim" はPythonの軽量イメージの出発点として良い選択です
FROM python:3.10-slim
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY echo.py .
CMD ["python", "echo.py"]
