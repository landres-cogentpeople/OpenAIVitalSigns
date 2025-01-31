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

    # Load the API_KEY.  The line below only sets a temporary API_KEY
    openai.api_key = "<API_KEY>"

    # The actual API_KEY is loaded from the "apiKey.txt" file in the line below.
    with open("apiKey.txt", "r") as filein:
        fileline = filein.readline()
        openai.api_key = fileline.strip()

    # The following function serves static files under the "/static" base URL
    @app.route("/static/<path:path>")
    def sendStaticFile(path):
        return send_from_directory("static", path)

    # The following function serves static files under the "/get_json_translation"
    # URL endpoint.
    @app.route("/get_json_translation", methods=["POST"])
    def getJSONTranslation():

        # The prompt, along with context data, is stored in the requestText python variable.
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
""".format(request.form["patient_note_text"])

        # The next line prints the prompt that will be sent to OpenAI for debugging purposes.
        print(requestText)

        # This makes the call to OpenAI to be processed using the "text-davinci-003" model
        jsonString = openai.Completion.create(
            model="text-davinci-003",
            prompt=requestText,
            max_tokens=300
        )

        # The next line prints the returned string from OpenAI for debugging purposes.
        print(jsonString)

        # This returns the result as a jsonString
        return jsonString

    # This returns the entire app as a result of the create_app() method.
    return app


# Main call to start the application.
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000, host="0.0.0.0")
