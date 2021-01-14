from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from blog.models import Post1,BlogComment


def bloghome(request):
    allpost=Post1.objects.all()
   
    context={'allposts':allpost}
    return render(request,'blog/blog.html',context)

def blogpost(request,slug):
    post=Post1.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    
    context={'post':post,'comments':comments,'user':request.user}
    return render(request,'blog/blogpost.html',context)
    # return HttpResponse(f'this is blogpost { slug }')


def postcomment(request):
    if request.method=="POST":
        
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post=Post1.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        print("parent ",parentSno)
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted Successfully")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,"Your reply has been posted Successfully")

        
        
        
        

    return redirect(f'/blog/{post.slug}')

