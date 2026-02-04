from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authentication import TokenAuthentication

from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .permissions import IsPostAuthor, IsAdmin

from django.contrib.auth import authenticate
from django.contrib.auth.models import User as UserAuth
from django.contrib.auth.models import Group

class GetUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer

    def get(self, request):
        users = UserAuth.objects.values()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class CreateNewUser(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            email = serializer.data.get('email')
            is_staff = serializer.data.get('is_staff')
            is_superuser = serializer.data.get('is_superuser')
            user = UserAuth.objects.create_user(username = username, password = password, email = email, is_staff = is_staff, is_superuser = is_superuser)
            if user is not None:
                data = serializer.save(user.username, user.password, email, is_staff, is_superuser)
                return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogin(APIView):
    def authenticate_user(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListCreate(generics.ListCreateAPIView):
    def get(self, request):
        comments = Comment.objects.all().order_by("-created_at")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsPostAuthor]

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        self.check_object_permissions(request, post)
        return Response({"content": post.content})
    
class PostRetrieveUpdateDestroy(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsPostAuthor]

    def perform_update(self, serializer):
        if 'author' in serializer.validated_data:
            del serializer.validated_data['author']  # Prevent users from changing the post's author field
        super().perform_update(serializer)
