from django.forms.forms import DeclarativeFieldsMetaclass
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .forms import CreatePostForm
from .models import Post, Comment
from django.conf import settings
from PIL import Image
import os

# Create your views here.

def create(response):
    if str(response.user) == 'AnonymousUser':
        return HttpResponseRedirect('/login')        
    if response.method == 'POST':
        form = CreatePostForm(response.POST, response.FILES)
        if form.is_valid():  
            description =  form.cleaned_data["description"]   
            post = Post(description=description, path='123') 
            post.description =  form.cleaned_data["description"]  
            post.save() 
            image = Image.open(form.cleaned_data["image"])              
            response.user.postauthor.add(post)
            extension = str(form.cleaned_data["image"]).split('.')[-1]
            path = str(post.id) + '.' + extension
            post.path = path
            post.save()
            path = str(os.path.join(settings.BASE_DIR, 'static', 'posts', 'images', path))
            image.save(path)
            return redirect('/profile/'+str(response.user.id))
        return HttpResponseRedirect('/post/create')  
            
    form = CreatePostForm()
    return render(response, "main/create.html", {"form": form})