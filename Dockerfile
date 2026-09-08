FROM python:3.12-slim
WORKDIR /app

COPY ./mon_module.py .

ENTRYPOINT ["python", "mon_module.py"]
CMD []