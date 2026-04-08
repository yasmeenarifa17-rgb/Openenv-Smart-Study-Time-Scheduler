FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir gymnasium torch pydantic numpy flask

CMD ["python", "app.py"]
