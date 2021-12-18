from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from posts.models import Post
from profiles.forms import CommentForm
from posts.models import Comment

# Create your views here.

def home(response):
    if str(response.user) == 'AnonymousUser':
        return HttpResponseRedirect('/login') 
    if response.method == 'POST':
        id = int(list(response.POST.dict().keys())[-1].split('.')[-1])
        string = list(response.POST.dict().keys())[-1][:2]    
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
            print("xd")
            post = Post.objects.get(id=id)
            if int(post.user.id) == response.user.id:
                post.delete()
        elif string == 'dc':
            comment = Comment.objects.get(id=id) 
            print(comment.user.id)
            if int(comment.user.id) == response.user.id:
                comment.delete()
        return redirect('/')
    form = CommentForm()
    posts = Post.objects.all()
    return render(response, 'main/home.html', {'form':form, 'posts':posts})