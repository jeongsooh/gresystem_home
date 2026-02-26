from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('leads/', include('leads.urls')),
    path('board/', include('board.urls')),
]
