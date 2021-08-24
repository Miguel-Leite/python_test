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

python3 --out:
	python3 ./manage.py graphql_schema --schema core.schema --out schema.graphql

python3 help graphql:
	python3 ./manage.py graphql_schema -h