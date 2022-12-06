from django.urls import path

from . import views

app_name = 'inrite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]