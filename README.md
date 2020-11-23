# Code sample
Simple demo code using docker, docker-compose, flask, python, mongodb, html, css
It just creates two docker containers one mongodb and one with web frontend.
Upload a DICOM file and see the preview of it in browser.

What is happening behind the scenes
1. Flask setup
2. Docker containers for development and docker testing environment
3. Auto setup of mongodb
4. Upload form and post files save them in mongodb (not optimized just for demo and practice)
5. Convert DICOM to JPEG capture output and display in browser
6. Delete uploaded file file
7. Invented some tests to learn and play with the pytest and flask testing environment

# Todo
- [ ] validatate of the uploaded file
- [ ] optimize to write the preview to file/mongo 

Estimated time to learn and develop:
5:30h

# Run

The following command runs the microservices which listen on 0.0.0.0:5000 for frontend web
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

```
pip install -r requirements/development.txt
```
