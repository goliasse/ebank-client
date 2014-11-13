ENV=dev

migrate:
	./manage.py makemigrations
	./manage.py migrate

build:
	rm -rf static/CACHE
	./manage.py compress --force --settings=config.environments.$(ENV)

static: build
	rm -rf public/static/*
	./manage.py collectstatic --noinput -l --settings=config.environments.$(ENV)
	
	npm i -g bower || true
	bower install

run:
	./manage.py runserver 0.0.0.0:8080
	
clean:
	find . -name '*.pyc' -delete
	rm -rf public/* || true
	rm -rf static/CACHE || true

makemessages:
	./manage.py makemessages -i '*sublime*' -i env -l en
	./manage.py makemessages -i '*sublime*' -i env -l ru
	./manage.py makemessages -i '*sublime*' -i env -l be

compilemessages:
	./manage.py compilemessages

.PHONY: build static
