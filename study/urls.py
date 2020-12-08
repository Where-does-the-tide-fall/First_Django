from django.urls import re_path
from study import views
urlpatterns = [
    re_path(r'^study/$', views.review)
]