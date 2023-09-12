
from django.urls import path, include
from . import views



urlpatterns = [
    path('',views.PersonList, name='Persons' ),
  path('detail/<int:pk>',views.PersonDetail ),
  path('update/<int:pk>',views.PersonUpdate ),
  path('create',views.PersonCreate ),
  path('delete/<int:pk>',views.PersonDelete ),
]