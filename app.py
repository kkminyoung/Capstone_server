from flask import send_file
from flask_login import LoginManager, login_user, current_user, logout_user

from src.fulls import *
from src.users import *
from src.edits import *
from src.login import *

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['JSON_AS_ASCII'] = False
login_manager = LoginManager()
login_manager.init_app(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads/')

@login_manager.user_loader
def load_user(user_id):
    return USERS[user_id]


@app.route('/')
def show_url():
    return render_template('url.html')


@app.route("/video/<fileName>", methods=["GET"])
def full(fileName):
    return render_template('video.html', data=fileName)


@app.route("/edited/<fileName>", methods=["GET"])
def edited(fileName):
    return render_template('edited_video.html', data=fileName)


@app.route("/uploads/<fileName>", methods=["GET"])
def show_video(fileName):
    path = UPLOAD_FOLDER + fileName
    return send_file(path, mimetype='multipart/form')


@app.route("/edit/<fileName>", methods=["GET"])
def show_edit_video(fileName):
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'edit_folder/')
    path = UPLOAD_FOLDER + fileName
    return send_file(path, mimetype='multipart/form')


app.register_blueprint(user_api, url_prefix='/api')
app.register_blueprint(full_api, url_prefix='/api')
app.register_blueprint(edit_api, url_prefix='/api')
app.register_blueprint(login_api)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',port='5001',debug=True)


