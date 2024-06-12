FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

RUN pip install fastapi uvicorn 

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
#CMD [ "uvicorne" ,"main:app","--host","0.0.0.0","800"] 