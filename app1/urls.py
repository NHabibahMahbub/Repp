from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.loginPage, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logoutPage, name='logout'),
    path('add-platform', views.add_platform, name='add-platform'),
    path('update-platform/<int:p_id>', views.update_platform, name='update-platform'),
    path('delete-platform/<int:p_id>', views.delete_platform, name='delete-platform'),
]
