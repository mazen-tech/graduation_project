from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('specific', views.specific, name='specific'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('getResponse', views.getResponse, name='getResponse'),
    path('contact/', views.contact, name='contact'),
]