FROM python:3.11.5

WORKDIR /simuladorBazin
COPY requirements.txt requirements.txt
RUN apt update
RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install -r requirements.txt

COPY . ./

EXPOSE 8501

CMD ["streamlit","run","app.py"]