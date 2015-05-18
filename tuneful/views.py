from flask import render_template
from flask import request, Response, url_for
from werkzeug import secure_filename
from utils import upload_path

from tuneful import app
from models import Song, File
from database import session
import decorators
import json

@app.route("/")
def index():  
    files = session.query(File).all()
    return render_template("index.html", files=files)

# @app.route("/api/songs", methods=["POST"])
# @decorators.accept("application/json")
# @decorators.require("application/json")
# def post_song():
#     """ Add a new song """
#     data = request.json
#     print data

#     # check that the JSON supplied is valid
#     # if not return a 422 Unprocessable Entity
#     try:
#         validate(data, song_schema)
#     except ValidationError as error:
#         data = {"message": error.message}
#         return Response(json.dumps(data), 422, mimetype="application/json")

#     # add the song to the database
#     song = models.Song(song_file_id=data["file"]["id"])
#     session.add(song)
#     session.commit()

#     # return a 201 Created, containing the post as JSON and with the
#     # location header set to the location of the post
#     data = json.dumps(song.as_dictionary())
#     headers = {"Location": url_for("get_songs")}
#     return Response(data, 201, headers=headers, mimetype="application/json")  


# @app.route("/uploads/<filename>", methods=["GET"])
# def uploaded_file(filename):
#     return send_from_directory(upload_path(), filename)  
  
# @app.route("/api/files", methods=["GET"])
# @decorators.accept("application/json")
# def get_files():
#     """ Return a list of all the files as JSON """
#     # should we use query string arguments?

#     # get the files from the database
#     files = session.query(models.File).all()

#     # convert the songs to JSON and return a Response
#     data = json.dumps([file.as_dictionary() for file in files])
#     return Response(data, 200, mimetype="application/json")


# @app.route("/api/files", methods=["POST"])
# @decorators.require("multipart/form-data")
# @decorators.accept("application/json")
# def file_post():
#     file = request.files.get("file")
#     if not file:
#         data = {"message": "Could not find file data"}
#         return Response(json.dumps(data), 422, mimetype="application/json")

#     filename = secure_filename(file.filename)
#     db_file = models.File(filename=filename)
#     session.add(db_file)
#     session.commit()
#     file.save(upload_path(filename))

#     data = db_file.as_dictionary()  
  
