from django.contrib import admin
from django.urls import path
from passgen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # name home is called in html as {% url home%}
    path('', views.home, name="home"),
    # name password is called in html as {{ password }}
    path('passwords/', views.passwords, name='password'),
]
