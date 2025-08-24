from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer, PostSerializer, CommentSerializer
from .models import Profile, Post, Like, Comment
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à Bookstore!")

# Registrar usuário
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Dados do usuário logado
class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


# Perfil logado
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)


# Seguir / deixar de seguir
class FollowAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        if target_user == request.user:
            return Response({"error": "Você não pode seguir a si mesmo."}, status=400)

        profile = request.user.profile
        target_profile = target_user.profile

        if target_profile in profile.following.all():
            profile.following.remove(target_profile)
            return Response({"message": f"Você deixou de seguir {username}."})
        else:
            profile.following.add(target_profile)
            return Response({"message": f"Você começou a seguir {username}."})


# Feed de notícias
class FeedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_profiles = request.user.profile.following.all()
        posts = Post.objects.filter(author__profile__in=following_profiles).order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class UserListView(APIView):
    permission_classes = [IsAuthenticated]  # apenas usuários autenticados podem ver

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Curtir / descurtir
class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            return Response({"message": "Você removeu a curtida."})
        return Response({"message": "Você curtiu a postagem."})


# Comentar
class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)