from django.urls import path
from . import user_api, mask_api

urlpatterns = [
    path('signup', user_api.UserCreate.as_view(), name='user-create'),
    path('login', user_api.UserLogin.as_view(), name='user-login'),
    path('logout', user_api.UserLogout.as_view(), name='user-logout'),
    path('mask', mask_api.Mask.as_view(), name='mask'),
]
