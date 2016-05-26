from django.conf.urls import url

from dhm import views

app_name = 'dhm'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reload_deliveries/', views.reload_deliveries),
    url(r'^delivery/', views.delivery),
    url(r'^user/', views.user),
    url(r'^check_user/', views.check_user),
    url(r'^heat_map/', views.heat_map),
    url(r'^filter_values/', views.filter_values)
]
