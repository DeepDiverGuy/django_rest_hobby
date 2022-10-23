# django_rest_hobby
A simple and very basic implementation of the Django REST Framework, as a hobby project. 
Model 'Person' is associated with the built-in user model. APIs are provided for both of 
these models. Permission functionality has also been implemented for some operations. No 
'viewset' is used, since those terminate the scope of customizing things.


# To get it working

  - In your projects settings.py, configure the SECRET_KEY.
  - In your terminal:
  
        python manage.py migrate

