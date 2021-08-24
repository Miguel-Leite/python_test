python run server:
	python3 manage.py runserver 0.0.0.0:8000

python loaddump:
	python3 manage.py loaddata requiremments.txt

python makemigrations:
	python3 ./manage.py makemigrations 

python migrate:
	python3 manage.py migrate

python3 createuser:
	python3 manage.py createsuperuser