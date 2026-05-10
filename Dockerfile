FROM python:3.11-slim
WORKDIR /app
RUN pip install flask scikit-learn numpy pandas
COPY app.py /app/
CMD ["python", "app.py"]
