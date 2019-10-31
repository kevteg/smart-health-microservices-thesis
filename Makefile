
rungateway:
	cd services && gunicorn -b "0.0.0.0:3333" --timeout 180 --reload --log-level debug --error-logfile - wsgi

runmedrecords:
	cd services && gunicorn -b "0.0.0.0:4444" --timeout 180 --reload --log-level debug --error-logfile - wsgi

runmhealth:
	cd services && gunicorn -b "0.0.0.0:5555" --timeout 180 --reload --log-level debug --error-logfile - wsgi

runstatistics:
	cd services && gunicorn -b "0.0.0.0:6666" --timeout 180 --reload --log-level debug --error-logfile - wsgi

migrate:
	cd services && python manage.py migrate

makemigrations:
	cd services && python manage.py makemigrations

data:
	services/manage.py generate_data $(patients)

users:
	cd services && python manage.py create_users 
