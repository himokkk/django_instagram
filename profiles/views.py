from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from posts.models import Comment
from .forms import CommentForm
from posts.models import Post
from django.conf import settings
from main.models import Profile
from PIL import Image
import os
# Create your views here.

def profile(response, id2):
    if response.method == 'POST':
        if str(response.user) == 'AnonymousUser':
            return HttpResponseRedirect('/login')  
        id = int(list(response.POST.dict().keys())[-1].split('.')[-1])
        string = list(response.POST.dict().keys())[-1][:2]
        if string == 'pi':
            if int(response.user.id) == id:
                extension = str(response.FILES['image']).split('.')[-1]
                image=Image.open(response.FILES['image'])
                path1 = str(response.user.id) + '.' + extension
                path = str(os.path.join(settings.BASE_DIR, 'static', 'avatars', 'images', path1))
                image.save(path)
                response.user.user.path = path1
                response.user.user.save()              
        if string == 'ac':
            form = CommentForm(response.POST)
            if form.is_valid():   
                text = form.cleaned_data['comment']  
                comment_obj = Comment(text=text)   
                comment_obj.save()
                response.user.commentauthor.add(comment_obj)
                post = Post.objects.get(id=id)
                post.post.add(comment_obj)
        elif string == 'dp':
            post = Post.objects.get(id=id)
            if int(post.user.id) == response.user.id:
                post.delete()
        elif string == 'dc':
            comment = Comment.objects.get(id=id) 
            if int(comment.user.id) == response.user.id:
                comment.delete()
        elif string == 'fl':
            if response.user.id != id2:  
                user_followed = User.objects.get(id=id)                
                if len(user_followed.user.follows.filter(id=response.user.id)) == 0:
                    user_followed.user.follows.add(response.user)
                else:
                    user_followed.user.follows.remove(response.user)
                count = user_followed.user.follows.all().count()
                user_followed.user.follows_count = count  
                user_followed.user.save()
                if len(response.user.user.followed.filter(id=user_followed.user.id)) == 0:
                    response.user.user.followed.add(user_followed)
                else:
                    response.user.user.followed.remove(user_followed) 
                count = response.user.user.followed.all().count()
                response.user.user.followed_count = count
                response.user.user.save()
        return HttpResponseRedirect('/profile/'+str(id2))
    form = CommentForm()
    user_followed = User.objects.get(id=id2)
    if len(user_followed.user.follows.filter(id=response.user.id)) == 0:
        following=False
    else:
        following=True    
    return render(response, "main/profile.html", {'id':id2, 'form':form, 'following': following, 'users_profile': user_followed})
