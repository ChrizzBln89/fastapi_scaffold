FROM python:3.10-slim-buster
COPY /fastapi /fastapi
COPY requirements.txt /fastapi/
WORKDIR /fastapi
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8003
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]

##CMD ["tail", "-f", "/dev/null"]