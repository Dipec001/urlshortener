from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

    path('<str:short_id>/', views.redirect_long_url, name='redirect-long-url')
]