FROM python:3.9.2

ENV MY_VAR=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" ]