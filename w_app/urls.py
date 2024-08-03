from django.urls import path
from . import views

app_name = 'w_app'

urlpatterns = [
    path('', views.search, name='index')
]
