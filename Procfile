web: gunicorn hotel_management.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn hotel_management.wsgi