from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='signup.html')),
    path('login/',TemplateView.as_view(template_name='login.html')),
    path('auth',views.login),
]