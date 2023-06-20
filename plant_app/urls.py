from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('plant_app.common.urls')),
    path('profile/', include('plant_app.accounts.urls')),
    path('plant/', include('plant_app.plants.urls')),
]
