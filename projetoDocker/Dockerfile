FROM python:3.11.5

WORKDIR /projetoDocker
COPY requirements.txt requirements.txt
RUN apt update
RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install -r requirements.txt

COPY . ./

EXPOSE 5432

CMD ["python","main.py"]
