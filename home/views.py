from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .models import Post
from .models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render( request, 'index.html', {'posts':posts})

def about(request):
    return render( request, 'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(fname=fname, lname=lname, email=email, phone=phone, message=message, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent!')
    return render( request, 'contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render( request, 'dashboard.html', {'posts':posts})
    else:
        return HttpResponseRedirect('login')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, files = request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                blog_image = form.cleaned_data['blog_image']
                pst = Post(title = title, desc = desc, blog_image = blog_image)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('login')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('login')

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, files = request.FILES, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('login')


def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Hey Welcome to the Blog Project')
                    return HttpResponseRedirect('dashboard')
        else:
            form = LoginForm()
        return render( request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('dashboard')



def signupUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation Man you become an author')
            user = form.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')
