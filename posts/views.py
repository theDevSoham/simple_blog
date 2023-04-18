from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def add_post(request):

    if request.user.is_authenticated == False:
        messages.error(request, 'You must login first!')
        return redirect('login')

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        
        if len(title) > 100 or len(content) > 1000:
            messages.error(request, 'Title or content too long!')
            return redirect('add_post')
        else:
            post = Post(title=title, content=content)
            post.save()
            messages.success(request, 'Post added successfully!')
            return redirect('add_post')
    else:
        return render(request, 'add_post.html')
    
def delete_post(request, pk):
    if request.user.is_authenticated == False:
        messages.error(request, 'You must login first!')
        return redirect('login')
    else:
        post = Post.objects.get(id=pk)
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('index')

def edit_post(request, pk):
    if request.user.is_authenticated == False:
        messages.error(request, 'You must login first!')
        return redirect('login')
    else:

        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            post = Post.objects.get(id=pk)
            post.title = title
            post.content = content
            post.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('/view/' + pk)
        else:
            post = Post.objects.get(id=pk)
            return render(request, 'edit_post.html', {'post': post})
    
def view_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'view_post.html', {'post': post})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('login')
