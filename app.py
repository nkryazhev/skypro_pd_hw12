from flask import Flask, request, render_template, send_from_directory, g
import logging
from main.views import main_blueprint
from loader.views import loader_blueprint

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
