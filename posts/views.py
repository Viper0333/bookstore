from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post

@login_required
def feed(request):
    # Busca todos os posts de todos os usuários
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def novo_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')

        if content or image:
            Post.objects.create(author=request.user, content=content, image=image)

        return redirect('posts')  # redireciona para o feed depois de criar post

    return redirect('posts')
