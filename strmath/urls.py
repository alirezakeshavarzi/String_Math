
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from calcu.views import index
from users.views import login_view, login_signup, logout_view, signup_view, update_personal_info, update_password, emailcheck, rest_pass_view, delete_account

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

    path('userpanel/', update_personal_info, name='userpanel'),

    path('update_password/', update_password, name='updatepass'),

    # if email address from user does exists then return page email else not found.
    path("authuser", emailcheck, name='emailcheck'),

    # rest password page returned.
    path("rest_password/<str:token>/", rest_pass_view, name='restpass'),

    path("delete_account", delete_account, name="delete_acc"),


    # 4. add path from simple jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    #path('accounts/', include('allauth.urls')),  # برای مدیریت احراز هویت اجتماعی
]
