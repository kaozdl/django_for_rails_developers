mkvirtualenv django_for_rails_developers
pip install pipenv
pipenv install django
django-admin startproject django_trello
cd django_trello
mv ../Pipfile .
mv ../Pipfile.lock .
python manage.py runserver
python manage.py migrate
python manage.py startapp trello
# edit django_trello/settings.py (install the newly created trello app)
# edit vim trello/models.py (create the board model)
# edit trello/admin.py (register your newly created model)
python manage.py makemigrations
# edit trello/models.py (create column and card models)
# edit trello/admin.py (register them into the admin)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
pipenv install djangorestframework
# edit django_trello/settings.py
python manage.py startapp api
# edit django_trello/settings.py
# create api/serializers.py
# edit api/views.py
# create api/urls.py
# edit django_trello/urls.py
