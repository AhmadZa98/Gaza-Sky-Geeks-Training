from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Category
# Create your views here.
def index(request):
    posts = Post.objects.filter(id__gte=2)
    context = {'posts':posts}
    #return HttpResponse(output)
    return render(request,'posts/posts.html',context)


def getPost(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {'post':post}
    return render(request,'posts/post.html',context=context)

def getCategories(request,category_id):
    categories = Category.object.all()
    context = {"categories" : categories}
    return render(request,'categories/categories.html',context=context)

def getCategory(request,category_id):
    category = Category.objects.get(id=category_id)
    context = {'category':category}
    return render(request,'posts/category.html',context=context)