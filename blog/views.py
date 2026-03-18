from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    form = PostForm()
    return render(request, 'blog/post_list.html', {'posts': posts, 'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('post_list')

def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    return redirect('post_list')

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')