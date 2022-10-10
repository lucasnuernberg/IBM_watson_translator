from flask import Flask

app = Flask(__name__)

import views

app.register_blueprint(views.views, url_prefix='/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
