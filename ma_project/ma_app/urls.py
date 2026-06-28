from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('selection', views.selection, name='selection'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
]