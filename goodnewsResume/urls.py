from django.urls import path
from . import views

app_name = 'goodnewsResume'

urlpatterns = [
    path('', views.home, name="home")
]
