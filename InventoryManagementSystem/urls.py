from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL
    path('inventory/', include('inventory.urls')),  # Include app URLs
]
