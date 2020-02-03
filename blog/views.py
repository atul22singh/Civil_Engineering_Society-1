
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def post_list(request):
	posts = Post.objects.filter(
		published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
# 	Post.objects.get(pk=pk)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
	return render(request, "index.html")

def about(request):
	return render(request, 'about.html')

def blog(request):
	return render(request, 'blog/blog.html')

def contact(request):
	return render(request, 'contact.html')

def resources(request):
	return render(request, 'resources.html')

def team(request):
	return render(request, 'blog/team.html')

