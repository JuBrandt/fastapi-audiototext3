FROM python:3.8
RUN pip3 install fastapi uvicorn
COPY ./fastapi-audiototext3 /app
CMD ["uvicorn", "fastapi-audiototext3.main:app", "--host", "0.0.0.0", "--port", "15400"]