FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver" ]
