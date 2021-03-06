from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Blog

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    blog_all = Blog.objects.all()
    paginator = Paginator(blog_all, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.content = request.GET['content']
    blog.save()
    return redirect('/blog/'+str(blog.id))
