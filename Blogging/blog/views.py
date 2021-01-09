from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from blog.models import Post1


def bloghome(request):
    allpost=Post1.objects.all()
   
    context={'allposts':allpost}
    return render(request,'blog/blog.html',context)

def blogpost(request,slug):
    post=Post1.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request,'blog/blogpost.html',context)
    # return HttpResponse(f'this is blogpost { slug }')


