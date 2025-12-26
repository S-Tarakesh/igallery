from django.urls import include,path
from . import views
urlpatterns=[
    path("gallery/",views.gallery,name="gallery")
]