# We could start with a linux container, but there is a container
# purpose built for Python - why do more work than we need to?
FROM python:3

# It's a good practice to copy just requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# This defines the directory where all of our commands will be executed
WORKDIR /app

# Install our requirements
RUN pip install -r requirements.txt

# Copy the latest version of our application into the folder on the container
COPY . /app

# Basis for our commands
ENTRYPOINT [ "flask" ]

# Run the app on port 80
CMD [ "run", "--port=80", "--host=0.0.0.0" ]
