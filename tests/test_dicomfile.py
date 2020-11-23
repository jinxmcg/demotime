from flask import Flask
from flask_pymongo import PyMongo

def test__database(app):
    mongo = PyMongo(app)
    mongo.db.command("ping") 
    
def test__files(app):    
    mongo = PyMongo(app)
    mongo.db.file_list.insert_one({"fileType":"DICOM","filename":"filename1","fileId":"fileid"})
    theFile = mongo.db.file_list.find_one({"filename":"filename1"})

    assert "DICOM" == theFile["fileType"]

def test_base_route(app):
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200


def test_filename(app):    
    client = app.test_client()
    url = '/uploads/filename1'
    response = client.get(url)
    assert response.get_data().find(b"filename1") > -1
    assert response.status_code == 200


def test__delete_file(app):    
    client = app.test_client()
    url = '/delete/filename1'
    response = client.get(url)

    url = '/uploads/filename1'
    response = client.get(url)
    assert response.get_data().find(b"filename1") == -1

    assert response.status_code == 200