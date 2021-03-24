@ECHO OFF
cd ..\operator_api
pip install -r requirements.txt
python manage.py makemigrations api
python manage.py migrate
python populate.py
python manage.py runserver