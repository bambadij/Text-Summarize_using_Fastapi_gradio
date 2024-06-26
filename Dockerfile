FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt 

RUN pip install fastapi uvicorn 

EXPOSE 8080
# CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
# CMD ["python", "text_image.py"]

CMD [ "uvicorn" ,"main:app","--host","0.0.0.0","8080"] 