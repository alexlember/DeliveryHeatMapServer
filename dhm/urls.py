from django.conf.urls import url

from dhm import views

app_name = 'dhm'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/', views.user),
]
