from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('game/', include('game.urls')),
]
