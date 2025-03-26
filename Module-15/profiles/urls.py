from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<str:username>/', views.ProfileDetailView.as_view(), name="detail"),
    path('<str:username>/follow/', views.FollowView.as_view(), name="follow"),
    path('<str:username>/update/username/', views.ChangeUsername.as_view(), name="update_username"),
    path('<str:username>/update/name/', views.ChangeName.as_view(), name="update_name"),
    path('<str:username>/update/password/', views.ChangePassword.as_view(), name="update_password"),
    path('<str:username>/update/avatar/', views.ChangeAvatar.as_view(), name="update_avatar"),
]