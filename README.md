# demotime
Light code demo 

#Install

pip install -r requirements/development.txt

FLASK_ENV="development" FLASK_CONFIG="development" docker-compose -f docker/development.yml build web

#RUN
FLASK_ENV="development" FLASK_CONFIG="development" docker-compose -f docker/development.yml up

Run as a daemon 
FLASK_ENV="development" FLASK_CONFIG="development" docker-compose -f docker/development.yml up -d

Stop containers when running as daemon
FLASK_ENV="development" FLASK_CONFIG="development" docker-compose -f docker/development.yml down