"""
URL configuration for Harpy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views  # a default view that django provides us with for login/logout
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls'))
]

"""
We don't want users to be exposed to the admin section when they try to login after logging out, rather we want them to be redirected to
a general user-login page. Thus, we need to create 'logout.html' in 'users' app instead of using the default logout system.

We want a user to be redirected to 'localhost/login/' page when they try to access their profile page through browser without logging in. But
"path('login/',...)" -> here, we are just telling django that whenever a user NAVIGATES to 'localhost/login/' page, route them to the following view. Thus, we have to set 'LOGIN_URL' in settings.py.
"""
