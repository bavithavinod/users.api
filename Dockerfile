FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DB_USERNAME=<dummy>
ENV DB_HOST=<dummy>
ENV DB_PASSWORD=<dummy>
ENV DB_NAME=<dummy>

#ENV AWS_REGION=<dummy>
#ENV AWS_ACCESS_KEY_ID=<dummy>
#ENV AWS_SECRET_ACCESS_KEY=<dummy>
#ENV ACCOUNT_KEY_REQUESTED_TOPIC=<dummy>

EXPOSE 5000

CMD [ "python", "./app.py" ]
