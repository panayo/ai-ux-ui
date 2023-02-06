FROM python:3.10.9

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