
.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: devel
devel:
	pip install -r requirements.txt

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver

.PHONY: messages
LANG="ja"
messages:
	python manage.py makemessages --keep-pot --locale $(LANG)

.PHONY: jsmessages
LANG="ja"
jsmessages:
	python manage.py makemessages --domain djangojs --keep-pot --locale $(LANG)

.PHONY: compile
compile:
	python manage.py compilemessages
