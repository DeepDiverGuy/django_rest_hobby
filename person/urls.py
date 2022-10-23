from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views



app_name = 'person'


rest_urlpatterns = [
    path('list/', views.PersonList.as_view(), name='list'),
    path('detail/<int:pk>/', views.PersonDetail.as_view(), name='detail'),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(rest_urlpatterns)