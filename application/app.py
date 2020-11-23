import io
import gridfs

from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from base64 import b64encode
from PIL import Image
from pydicom import dcmread
from pydicom.filebase import DicomBytesIO


def create_app(config_name):
    """Creates a flask app and expects the config name develpment or production"""
    
    app = Flask(__name__)

    # Capitalize so we get application.config.DevelopmentConfig from config.py    
    config_module = f"application.config.{config_name.capitalize()}Config"
    app.config.from_object(config_module)
    
    # Setup the mongodb url...could be set in the config too
    app.config["MONGO_URI"] = "mongodb://"+app.config['MONGO_INITDB_USERNAME']+":"+app.config['MONGO_INITDB_PASSWORD']+"@"+app.config['MONGO_INITDB_HOSTNAME']+":"+app.config['MONGO_INITDB_PORT']+"/"+app.config['MONGO_INITDB_DATABASE']
    mongo = PyMongo(app)
    fs = gridfs.GridFS(mongo.db)



    @app.route("/")
    def hello_world():
        """ Home handler function """

        lista = mongo.db.file_list.find({"fileType":"DICOM"})        
        return render_template("home.html", content=lista)


    @app.route("/delete/<filename>")
    def delete_file(filename):
        """ Delete file handler """
        theFile = mongo.db.file_list.find_one({"filename":filename})
        if fs.exists(theFile["fileId"]):
            fs.delete(theFile["fileId"])
        mongo.db.file_list.delete_one({"filename":filename})

        return render_template("uploaded.html",message="FILE DELETED!")



    @app.route("/uploads/<filename>")
    def get_upload(filename):
        """ Upload confirmation handler """
        # TODO: Validate is a DICOM format
        theFile = mongo.db.file_list.find_one({"filename":filename})
        if theFile:
            if fs.exists(theFile["fileId"]):
                raw = DicomBytesIO(fs.get(theFile["fileId"]).read())
                ds = dcmread(raw)
                message="Your file was uploaded "+filename                    
                new_im = Image.fromarray(ds.pixel_array)

                # test demo only
                # this is not optimal as it does not benefit from browser and file cache
                # also it is not generating preview only once
                with io.BytesIO() as output:
                    new_im.convert('RGB').save(output, format="JPEG")
                    contents = output.getvalue()               
                img = b64encode(contents).decode("utf-8")
        
                return render_template("uploaded.html",message=message,img=img)  
            return render_template("uploaded.html",message="FILE "+filename+" exists but is not uploaded! ")                        
        return render_template("uploaded.html",message="FILE DOES NOT EXIST! ")


    @app.route("/uploads/<path:filename>", methods=["POST"])
    def save_upload(filename):
        """ Handler to upload files """
        # TODO: Validate is a DICOM format
        out = mongo.save_file(filename, request.files["file"])                
        mongo.db.file_list.insert({"fileType":"DICOM","filename":request.files["file"].filename,"fileId":out})
        return redirect(url_for("get_upload", filename=request.files["file"].filename))


    return app