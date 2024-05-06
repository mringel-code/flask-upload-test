from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS

app = Flask(__name__)

pdfs = UploadSet('pdfs', DOCUMENTS)

app.config['UPLOADED_PDFS_DEST'] = 'static/files'
configure_uploads(app, pdfs)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'pdf' in request.files:
        filename = pdfs.save(request.files['pdf'])
        return "PDF Saved with name: " + filename
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
