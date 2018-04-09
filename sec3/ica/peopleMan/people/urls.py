from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.people_list),
    url(r'^persons/add', views.add_person)
]
