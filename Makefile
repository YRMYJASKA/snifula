run:
	pipenv run gunicorn snifula.wsgi
prep:
	pipenv run python3 manage.py collectstatic --no-input
