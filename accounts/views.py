from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    RegisterSerializer,
    UserSerializer,
    ProfileSerializer,
    PostSerializer,
    CommentSerializer
)
from .models import Profile, Post, Like, Comment
from .forms import RegisterForm, ProfileForm


# Página inicial
def home(request):
    return HttpResponse("Bem-vindo à Bookstore!")


# API para registrar usuário via DRF
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Dados do usuário logado
class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


# Perfil do usuário logado
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


# Lista de usuários
class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


# Curtir / descurtir postagem
class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()
            return Response({"message": "Você removeu a curtida."})
        return Response({"message": "Você curtiu a postagem."})


# Comentar postagem
class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post=post)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Registro de usuário via template HTML
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()  # salva o usuário com senha hash

            # Cria o profile apenas se não existir
            profile, created = Profile.objects.get_or_create(user=user)

            # Se enviou avatar, salva no profile
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
                profile.save()

            messages.success(request, "Conta criada com sucesso!")
            return redirect('login')
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

from django.http import HttpResponse
from .models import Profile

def limpar_profiles(request):
    # Remove Profiles órfãos
    Profile.objects.filter(user__isnull=True).delete()
    # Remove duplicados (mantém apenas um por user)
    from django.db.models import Count
    duplicates = (
        Profile.objects
        .values('user')
        .annotate(user_count=Count('id'))
        .filter(user_count__gt=1)
    )
    for dup in duplicates:
        profiles = Profile.objects.filter(user_id=dup['user'])
        # Mantém o primeiro, deleta os outros
        for profile in profiles[1:]:
            profile.delete()
    return HttpResponse("Profiles órfãos e duplicados removidos")


def criar_profiles_usuarios(request):
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)
    return HttpResponse("Profiles criados para todos os usuários.")
