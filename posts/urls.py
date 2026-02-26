from django.urls import path, include
from . import views as post_views
from .views import UserListCreate, PostListCreate, CommentListCreate
from .views import UserListCreate, PostListCreate, CommentListCreate, LoginView, PostDetailView, GoogleLogin, GoogleAuth, LogOut
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/google', GoogleLogin, name='google-login'),
    path('accounts/google/login/callback/', GoogleAuth, name='google-login'),
    path('logout', LogOut, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('token/', obtain_auth_token, name='api-token'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
