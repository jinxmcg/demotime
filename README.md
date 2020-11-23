# Code sample
Simple demo code using docker, docker-compose, flask, python, mongodb, html, css
It just creates two docker containers one mongodb and one with web frontend.
Simply upload a DICOM file and see the preview in browser.

What is happening behind the scenes
1. Flask setup
2. docker testing environment
3. auto setup of mongodb 
4. upload form and post files save them in mongodb (not optim just for demo and practice)
5. convert DICOM to JPEG capture output and display in browser

Estimated time to develop:
2h
# Install

```
pip install -r requirements/development.txt
```

# Run

The following command runs the webserver which listens on 0.0.0.0:5000
```
./demo.py compose up
```
Open browser and point it towards the new web docker container, usually:
http://localhost:5000


# Run as a daemon 
```
./demo.py compose up -d
```

# Run tests
```
./demo.py test
```