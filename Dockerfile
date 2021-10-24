FROM python:3.8

WORKDIR /home/julia/dev/fastapi-audiototext3

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /home/julia/dev/fastapi-audiototext3/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/julia/dev/fastapi-audiototext3/requirements.txt

COPY ./ /home/julia/dev/fastapi-audiototext3

CMD ["uvicorn", "main:app", "--host", "185.26.121.104", "--port", "15400"]
