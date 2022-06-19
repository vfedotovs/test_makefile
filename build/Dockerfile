FROM python:3.8-alpine
 

ARG srcDir=src
WORKDIR /app
COPY $srcDir/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY $srcDir/app.py .
COPY $srcDir/ ./app

 
ENTRYPOINT ["python"]
CMD ["app.py"]
