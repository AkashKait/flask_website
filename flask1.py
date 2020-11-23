import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from mysvm import feature
from mysvm import svm


app = Flask(__name__)
app.config["DEBUG"] = True

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

ALLOWED_EXTENSIONS = {'mp3'}
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def index():
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           print(filename)
           genre = svm.GetGenre(file)
           print(genre)
           return render_template('index.html')
       return render_template('index.html')
   if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()