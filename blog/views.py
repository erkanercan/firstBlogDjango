from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        yayinlanma_tarihi__lte=timezone.now()).order_by('yayinlanma_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
