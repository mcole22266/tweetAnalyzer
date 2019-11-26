FROM python:3.7

LABEL Michael Cole <mcole042891@gmail.com>

WORKDIR /app

COPY Resources/* /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
