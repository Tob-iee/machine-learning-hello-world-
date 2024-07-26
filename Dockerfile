FROM python:3.8.12-slim

RUN apt-get update && apt-get install -y build-essential

# RUN pip --no-cache-dir install pipenv

WORKDIR /app

# COPY ["Pipfile", "Pipfile.lock", "./"]
# RUN pipenv install --deploy --system --verbose && \
#     rm -rf /root/.cache

# Copy requirements.txt to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY ["predict.py", "model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]

