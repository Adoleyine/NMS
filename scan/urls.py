from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('discovery', views.scan_network, name='discovery')
]
