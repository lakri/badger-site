import os
import flask

UPLOAD_FOLDER = '/tmp/'

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def submit_file():
    if flask.request.method == 'POST':
        file = flask.request.files['file']
        file.save(
            os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        )
    return flask.render_template('submit-file.html')



@app.route('/plot', methods=['GET'])
def splot_file():
    
    return flask.render_template('plot-file.html')