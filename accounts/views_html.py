from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm, UserUpdateForm
from .models import Profile


def logout_view(request):
    logout(request)
    return redirect("login")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("posts")  # agora redireciona para posts
        else:
            return render(request, "accounts/login.html", {"form": form, "error": "Usuário ou senha inválidos."})
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)  # cria perfil automaticamente
            login(request, user)  # já loga
            return redirect("posts")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def posts_view(request):
    # Se você já tiver um modelo de Post, pode substituir isso
    posts = [
        {"title": "Primeiro post", "content": "Este é um post de exemplo."},
        {"title": "Segundo post", "content": "Outro conteúdo qualquer."},
    ]
    return render(request, "accounts/posts.html", {"posts": posts, "user": request.user})


@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile", username=request.user.username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    return render(
        request,
        "accounts/profile.html",
        {"u_form": u_form, "p_form": p_form, "user_profile": user_profile},
    )








# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from .forms import RegisterForm, ProfileForm, UserUpdateForm
# from .models import Profile
# from django.contrib.auth import logout

# def logout_view(request):
#     logout(request)
#     return redirect("login")


# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("profile", username=user.username)  # redireciona para a página do usuário
#     else:
#         form = AuthenticationForm()
#     return render(request, "accounts/login.html", {"form": form})


# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             Profile.objects.create(user=user)  # cria perfil automaticamente
#             login(request, user)  # já loga
#             return redirect("profile", username=user.username)
#     else:
#         form = RegisterForm()
#     return render(request, "accounts/register.html", {"form": form})


# @login_required
# def profile_view(request, username):
#     user_profile = get_object_or_404(User, username=username)

#     if request.method == "POST":
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             return redirect("profile", username=request.user.username)
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileForm(instance=request.user.profile)

#     return render(
#         request,
#         "accounts/profile.html",
#         {"u_form": u_form, "p_form": p_form, "user_profile": user_profile},
#     )
