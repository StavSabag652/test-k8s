FROM python:3.10-alpine3.20

WORKDIR /app2

COPY requierments.txt .

RUN pip install -r requierments.txt

COPY . .

EXPOSE 8070

CMD [ "python","app.py" ]