@ECHO OFF
cd ..\ProjectImplementation\QueryTools\second_customer_query_tool\customer_query_tool
pip install -r requirements.txt
python manage.py makemigrations customers
python manage.py migrate
python populate.py
python manage.py runserver