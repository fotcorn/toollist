build:
	docker build . -t toollist

start:
	docker pull fotcorn/toollist
	docker-compose up -d
	docker-compose exec django /code/manage.py migrate

restart:
	docker-compose restart

stop:
	docker-compose stop
