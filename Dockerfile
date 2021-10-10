# Base Image
FROM python:3.9

# Run updates required to get OpenCV running
# The y flag means that the command assumes a "yes" to any prompts
RUN apt-get update && apt-get install -y libgl1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY sketch-app ./

EXPOSE 8501

CMD streamlit run --server.port 8501 app.py
