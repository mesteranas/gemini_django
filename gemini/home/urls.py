from django.urls import path
from . import views
urlpatterns=[
    path("",views.home_,name="homePage"),
    path("contect/",views.Contect,name="contect"),
    path("about/",views.about,name="about"),
    path("model/text",views.text,name="TextModel"),
    path("model/img",views.IMGModel,name="IMGModel")
]