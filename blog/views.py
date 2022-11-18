from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from datetime import datetime
from .forms import PostForm
from django.utils import timezone
# Create your views here.


# url route = index
def index(request):
    posts = Post.objects.filter(published_at__lte=datetime.now()).order_by('-published_at')
    return render(request,'blog/index.html',{'posts': posts})


# url route = detail
def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/detail.html',{'post':post})


#url route = new-form
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/new_form.html',{'form':form})



#url route = update
def update_form(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/new_form.html',{'form':form})