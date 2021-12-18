from django.urls import path
from . import views 

urlpatterns = [
    path('<int:id2>', views.profile, name="home"),       
]
