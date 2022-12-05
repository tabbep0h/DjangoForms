from django.contrib import admin
from django.urls import path,re_path,include
from DjangoFormsAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('appointment/',views.appointment),
    path('ordermain/',views.ordermain)
]
