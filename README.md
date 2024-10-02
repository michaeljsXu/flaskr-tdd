# Flask-tdd
Flask test driven development project, taken from [https://github.com/shuruizUofT/flaskr-tdd](https://github.com/shuruizUofT/flaskr-tdd).

## Starting Flask App
`FLASK_APP=project/app.py python -m flask run --host=0.0.0.0 -p 5000`

# Starting Gunicorn and making the db
`python create_db.py && gunicorn -b 0.0.0.0:5000 project.app:app`

## Run pytest
`python -m pytest`