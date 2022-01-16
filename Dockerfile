# Set base image (host OS)
FROM python:3.10-alpine

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install -r requirements.txt && \
 apk --purge del .build-deps


# Copy the content of the local src directory to the working directory
COPY app.py  .
COPY config.py  .
COPY .env  .
COPY db.py  .
ADD managers managers
ADD migrations migrations
ADD models models
ADD resources resources
ADD schemas schemas
ADD services services
ADD utils utils


# Specify the command to run on container start
CMD [ "python", "./app.py" ]