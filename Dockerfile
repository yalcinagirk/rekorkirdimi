
FROM  python

WORKDIR /app 
COPY . /app

RUN pip install -r requirements.txt

RUN python manage migrate
RUN python manage.py create_currencies
