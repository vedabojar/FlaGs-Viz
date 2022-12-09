'''
A docker file reequired to run the app on G-Gloud.
'''

FROM python:3.8

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

#EXPOSE 8080
EXPOSE $PORT

CMD python app.py
