from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('commemoration/', views.commemoration, name='commemoration'),
    path('commemoration/success/', views.comm_success, name='comm_success'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('events/', views.EventsView.as_view(), name='events'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_view'),
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
]

