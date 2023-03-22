# OpenAIVitalSigns

The OpenAIVitalSigns project was written to demonstrate converting dictated patient notes into machine-readable language through the use of the OpenAI API.

## Prerequisites

The OpenAIVitalSigns project relies on the following prerequisites:

* Python version 3.4 or greater
* Git
* pip for installation of Python modules
* An OpenAI API Key
* (optional) venv for installation of Python modules in a virtual environment

## Installation

* In the installation directory run:

```bash
git clone https://github.com/lmandres/OpenAIVitalSigns.git
cd OpenAIVitalSigns
git pull
```

* You can create a virtual environment to run the application in Linux or MacOS (This step is optional).

```bash
python3 -m venv venv
source venv/bin/activate
```

* On in Windows Command Shell:
```
python -m venv venv
venv\Scripts\activate.bat
```

* Install the prerequisite Python modules

```bash
pip install -r requirements.txt
```

## Configuration

* Edit the "apiKey.txt" file to include the OpenAI API key.
* In this installation, you can use your favorite editor.  However, for this example we will be using Windows Notepad.
* Open the file for editing.

```bash
notepad apiKey.txt
```

* Enter the OpenAI API key and save.

## Running the application

* To run the application, you will have to do the following steps, based on your installation.
* Change into the directory containing the OpenAIVitalSigns script:

```bash
cd OpenAIVitalSigns
```

* If you installed the Python module dependencies in a virtual environment (after following the optional venv step), you will need to ensure that you source the virtual environment.

```bash
source venv/bin/activate
```

* NOTE: In Windows Command Shell, you will have to replace the previous command with the following:
```
venv\Scripts\activate.bat
```

* Run the server application
```bash
python app.py
```

## Using the application

* After starting the server application, open a web browser to the following web address

[http://localhost:5000/static/vital_signs.html](http://localhost:5000/static/vital_signs.html)

* NOTE: The security context makes it so that you can only visit this page if the server is run on localhost or a page using HTTPS.

## Stopping the application

* To stop the application, type Ctrl-C
* If you sourced a virtual environment, you can deactivate the virtual environment by entering the following command:

```bash
deactivate
```
