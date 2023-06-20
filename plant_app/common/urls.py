from django.urls import path

from plant_app.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('catalogue', views.catalogue_page, name='catalogue')
]