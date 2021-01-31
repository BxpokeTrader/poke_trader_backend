.PHONY: all test clean

compose_build:
	docker-compose build

test:
	python manage.py test
	python manage.py behave

docker-test: compose_build
	docker-compose up -d
	docker-compose exec web python manage.py test
	docker-compose exec web python manage.py behave