FROM python3.12.8:alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./database .
COPY create_database.py .
COPY ./config .

RUN python create_database.py

COPY . .

CMD ["python", "main.py"]