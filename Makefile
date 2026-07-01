PYTHON = python
MANAGE = $(PYTHON) manage.py

install: 
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

run:
	$(MANAGE) runserver

user:
	$(MANAGE) createsuperuser