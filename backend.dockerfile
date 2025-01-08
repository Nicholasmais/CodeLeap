FROM python:3.11

WORKDIR /app

COPY ./codeleap/requirements.txt .
RUN pip install -r requirements.txt

COPY ./codeleap .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]