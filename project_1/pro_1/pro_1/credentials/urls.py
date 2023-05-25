from . import views
from django.urls import path

urlpatterns = [

    path('registration',views.registration,name='registration'),
    path('index_login',views.index_login,name='index_login'),
    path('logout',views.logout,name='logout'),
]