from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from accounts.models import UserProfile


# Create your views here.
def index(request):
    return render(request,'blog/index.html')




def posts(request):
    if request.method== 'GET' :
        posts=Post.objects.all().order_by('-created_at')[:100]
        return render(request,'blog/posts.html',{'posts':posts})
    
    elif request.method == 'POST' :
            body=request.POST.get('body')
            if request.POST.get('title') :
                title=request.POST.get('title')
            else :
                title =body[:4]
            
            post=Post(
                body=body,
                author= UserProfile.objects.get(id=request.user.id) ,
                title=title
            )
            post.save()
            posts=Post.objects.all().order_by('-created_at')[:100]
            return render(request,'blog/posts.html',{'posts':posts})




def post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    if request.method == 'GET' :
        return render(request,'blog/post.html',{'post':post})
    elif request.method == 'POST' :
        body=request.POST.get('body')
        comment=Comment(
            body=body,
            author= UserProfile.objects.last(),
            post=post
        )
        comment.save()
        comments=post.comment_set.all().order_by('-created_at')[:500]
        return render (request,'blog/post.html',{'post':post,'comments':comments})
