from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tarot/', views.tarot, name='tarot'),
    path('pyros/', views.pyros, name='pyros'),
    path('features/', views.features, name='features'),
    path('faq/', views.faq, name='faq'),
]
