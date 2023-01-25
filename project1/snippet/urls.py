from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.snippetList,name='home')
]
