FROM python:3.7

LABEL Michael Cole <mcole042891@gmail.com>

COPY Resources/* /

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]