@ECHO OFF
cd ..\QueryTools\customer_query_tool
pip install -r requirements.txt
python manage.py makemigrations customers
python manage.py migrate
python populate.py
python manage.py runserver