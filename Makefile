run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell_plus --ipython

runprod:
	poetry run gunicorn config.wsgi -b 0.0.0.0:5555 --daemon --pid gunicorn.pid

killprod:
	kill `cat gunicorn.pid`
