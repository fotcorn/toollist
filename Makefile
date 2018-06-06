start:
	docker-compose up -d
	docker-compose exec django /code/manage.py migrate

restart:
	docker-compose restart

stop:
	docker-compose stop
