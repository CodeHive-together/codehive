from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))
] #반드시 적어야 하며 위와 같이 라우팅 설정을 해야함.
