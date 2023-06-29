
FROM  python
EXPOSE 8000
WORKDIR /app 
COPY . /app

RUN pip install -r requirements.txt
