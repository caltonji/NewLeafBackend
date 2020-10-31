flask app

Needs environment variables:
AZURE_STORAGE_CONNECTION_STRING
CLIENT_BASE_URI
COMMUNICATION_SERVICES_CONNECTION_STRING

Use virtual env
on git bash
. venv/Scripts/activate

To run:
export FLASK_APP=hello.py
flask run

<!-- or gunicorn --bind=0.0.0.0 --timeout 600 application:app -->