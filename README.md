cd social_network/

python manage.py makemigrations

python manage.py migrate

#
python manage.py migrate --run-syncdb # If smth wrong happend to migrations