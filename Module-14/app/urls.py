from django.urls import path
from .views import HomePageView, PostDetilView, AddPostView

app_name = 'app'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetilView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post'),
]
