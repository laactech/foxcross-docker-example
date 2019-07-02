# Base docker image to build from
FROM python:3.7

# Update and install OS dependencies
RUN apt-get update

# Create new user with a home directory so that
# we don't run as root
RUN useradd -m python-user
USER python-user
WORKDIR /home/python-user

# Add the new user's local bin to the path for
# running python scripts such as django-admin
ENV PATH="${PATH}:/home/python-user/.local/bin"

# Allow the port to be accessed
EXPOSE 8000

# Copy only requirements.txt for caching
COPY requirements.txt ./

# Install our python requirements into local user bin
RUN pip install --user -r requirements.txt

# Copy our application files into the current
# directory
COPY . ./

# Use this command when the docker image is run
CMD gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker app:app