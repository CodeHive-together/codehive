from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('create/',views.create),
    path('read/<id>/',views.read),
    path('delete/', views.delete),
    path('update/<id>/',views.update),
    path('achievements/', views.achievement, name='achievement'),
    path('search/', views.search, name='search'),
    path('find/', views.find, name='find'),
] 
