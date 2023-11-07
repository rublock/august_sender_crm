from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainapp.urls")),
    path("api/", include("mainapp_api.urls")),
    path("accounts/", include("accounts.urls")),
]
