FROM python:3.7.3

# install dependencies
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y inotify-tools make nodejs

# Add application
ADD . /app
WORKDIR /app

# Setup application
RUN pip install pipenv

# Convert pipenv para requirements.txt
RUN pip install pipenv_to_requirements
RUN pipenv run pipenv_to_requirements

# install dependencies
RUN pip install -r requirements-dev.txt
RUN pip install -r requirements.txt
RUN npm install
