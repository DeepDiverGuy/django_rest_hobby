# django_rest_hobby
A simple and very basic implementation of the Django REST Framework, as a hobby project. 
Model 'Person' is associated with the built-in user model. APIs are provided for both of 
these models. Permission functionality has also been implemented for some operations. No 
'viewset' is used, since those terminate the scope of customizing things.


# To get it working

  - Install the requirements:
  
        pip install django
        pip install djangorestframework
  - In settings.py inside 'tutorial' folder, configure the SECRET_KEY.
  - In your terminal:
  
        python manage.py migrate
        python manage.py runserver
  - Look inside tutorial.urls.py & person.urls.py to know about the url routes.

