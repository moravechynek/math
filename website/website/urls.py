from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('math_app/', include('math_app.urls')),
    path('', include('math_app.urls')),
    path('admin/', admin.site.urls),
]