run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

shell:
	poetry run python manage.py shell_plus --ipython
