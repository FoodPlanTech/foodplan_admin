run:
	poetry run python manage.py runserver

api:
	poetry run python manage.py show_urls | rg '^/api/v1/'

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser

shell:
	poetry run python manage.py shell_plus --ipython

runprod:
	poetry run gunicorn config.wsgi -b 0.0.0.0:5555 --daemon --pid gunicorn.pid

killprod:
	kill `cat gunicorn.pid`
