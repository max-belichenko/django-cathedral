from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about/<int:pk>/', views.about_article, name='about_article'),
    path('commemoration/', views.commemoration, name='commemoration'),
    path('contacts/', views.contacts, name='contacts'),
    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.events_article, name='events_article'),
    path('schedule/', views.schedule, name='schedule'),
]
