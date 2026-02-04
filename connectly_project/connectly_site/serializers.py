from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at', 'password', 'is_staff', 'is_superuser']

    def save(self, _username, _password, _email, _is_staff, _is_superuser):
        self.username = _username
        self.password = _password
        self.email = _email
        self.is_staff = _is_staff
        self.is_superuser = _is_superuser


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'comments']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'created_at']


    def validate_post(self, value):
        if not Post.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Post not found.")
        return value


    def validate_author(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Author not found.")
        return value
