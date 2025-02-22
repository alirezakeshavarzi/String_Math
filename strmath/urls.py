"""strmath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from calcu.views import index
from users.views import login_view, login_signup, logout_view, signup_view, user_panel, update_personal_info, update_password

# 3. add views from simple jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='home'),

    path('authuser/',login_signup , name='auth'),
    path('authuser/login/',login_view , name='login'),
    path('logout/', logout_view, name='logout'),

    path('authuser/signup/', signup_view, name='signup'),

    path("update/", update_personal_info, name='update'),

    path('userpanel/', user_panel, name='userpanel'),

    path('update_password/', update_password, name='updatepass'),


    # 4. add path from simple jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
