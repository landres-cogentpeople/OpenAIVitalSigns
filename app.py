import json
import os

from flask import Flask
from flask import request
from flask import send_from_directory

import openai


app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    openai.api_key = "<API_KEY>"
    with open("apiKey.txt", "r") as filein:
        fileline = filein.readline()
        openai.api_key = fileline.strip()

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/static/<path:path>")
    def sendStaticFile(path):
        return send_from_directory("static", path)

    @app.route("/upload_utterance", methods=["POST"])
    def uploadUtterance():

        transcript = None

        if not os.path.exists("uploads"):
            os.makedirs("uploads")

        try:
            os.remove("uploads/utterance.webm")
        except FileNotFoundError as fnfe:
            pass

        request.files["utterance_file"].save("uploads/utterance.webm")
        with open("uploads/utterance.webm", "rb") as utteranceFile:
            transcript = openai.Audio.transcribe("whisper-1", utteranceFile)

        try:
            os.remove("uploads/utterance.webm")
        except FileNotFoundError as fnfe:
            pass

        return json.dumps(transcript)

    @app.route("/get_json_translation", methods=["POST"])
    def getJSONTranslation():
        requestText = """
Patient Note:

{}

Format the Patient Note into JSON with the following key value pairs if present in the Patient Note:

blood_pressure_systolic: systolic blood pressure in mmHg
blood_pressure_diastolic: diastolic blood pressure in mmHg
heart_rate: heart rate in beats per minute
respiratory_rate: respiratory rate in breaths per minute
height: height in centimeters
weight: weight in kilograms
""".format(request.form["utterance_text"])
        jsonString = openai.Completion.create(
            model="text-davinci-003",
            prompt=requestText,
            max_tokens=300
        )
        print(jsonString)
        return jsonString

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000, host="0.0.0.0")
