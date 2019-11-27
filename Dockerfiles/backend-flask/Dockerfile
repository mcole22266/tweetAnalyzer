FROM python:3.7-slim

LABEL maintainer="Michael Cole" \
      email="mcole042891@gmail.com" \
      description="TODO: Update Container Description"

ENV INSTALL_PATH /tweetanalyzer
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY Resources/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY Resources/ ./

EXPOSE 5000

CMD ["python", "app.py"]
