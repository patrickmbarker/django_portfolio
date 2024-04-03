from django.urls import path

from . import views
#These URLs represent the different views in our views.py file

urlpatterns = [
    path("",views.index, name="index"),
]