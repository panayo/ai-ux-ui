FROM python:3.10.9

RUN apt-get update && apt-get install -y  chromium \
  libleptonica-dev \
  tesseract-ocr \
  libtesseract-dev \
  python3-pil \
  tesseract-ocr-eng \
  tesseract-ocr-script-latn \
  && rm -rf /var/lib/apt/lists/*


RUN pip install pipenv

WORKDIR /app
COPY Pipfile* /app

RUN mkdir /app/.venv
RUN pipenv install --deploy
RUN pip install streamlit

EXPOSE 8501

COPY ./app/ /app

ENTRYPOINT [ "pipenv", "run", "streamlit"]
CMD [ "run","frontend.py" ]
