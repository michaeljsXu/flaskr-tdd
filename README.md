# Flask-tdd
Flask test driven development project, taken from [https://github.com/shuruizUofT/flaskr-tdd](https://github.com/shuruizUofT/flaskr-tdd).

# Live View
[https://flaskr-tdd-bjo6.onrender.com/](https://flaskr-tdd-bjo6.onrender.com/) \
The live view is hosted using [render.com](render.comm) and uses a postgres db.


# Starting the app and using an sqlite3 database locally
`python create_db.py && gunicorn -b 0.0.0.0:5000 project.app:app`

## Run pytest
`python -m pytest`
