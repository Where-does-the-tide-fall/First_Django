from django.urls import re_path
from flying import views
urlpatterns = [
    re_path(r'^ding/$', views.fly_views)
]