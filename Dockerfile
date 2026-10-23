FROM python:3.11-slim

WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/rlaalstn1504/sample_2.git .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]