.PHONY: all test clean

clean:
	fuser -k 8000/tcp

test:
	python manage.py runserver &
	python manage.py behave
	fuser -k 8000/tcp