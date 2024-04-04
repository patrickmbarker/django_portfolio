from django.urls import path

from . import views
#These URLs represent the different views in our views.py file
#The URLs file represents what URL address will be directed to which view.
#Furthermore, the models.py file can be imported into the views file to generate views that reference the data models in models.py

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.home, name="home"),
    path("home/",views.home, name="home"),
    path("create/",views.create, name="create"),
    path("view/",views.view, name="view"),
    path("attribution/",views.attribution, name="attribution"),
]