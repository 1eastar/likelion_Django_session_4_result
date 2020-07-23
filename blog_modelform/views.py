from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Blogg
from .forms import BlogPost

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    blog_all = Blogg.objects.all()
    paginator = Paginator(blog_all, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogg, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home2')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})