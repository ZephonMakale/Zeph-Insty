from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import TemplateView
from instaclone import views as instaclone_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('instaclone.urls')),
    path('signup/', instaclone_views.signup, name='signup'),
    path('profile/', instaclone_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home')
]
