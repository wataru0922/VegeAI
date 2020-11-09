import os
from flask import Flask,flash,request,redirect,url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER="./uploads"
ALLOWED_EXTENSIONS={"png","jpg","gif"}


app=Flask(__name__)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/",methods=["GET","POST"])
def uoload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.ulr)
        file=request.files["file"]    
        if file.filename==" ":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
            return redirect(url_for("upload_file",filename=filename))    
    return '''

<!doctype html>
<html>
<head>
<meta charset="UTF-8>
<title>upload new file</title></head>
<body>
<h1>Upload new file</h1>
<form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
</form>
</body>
</html>
'''
