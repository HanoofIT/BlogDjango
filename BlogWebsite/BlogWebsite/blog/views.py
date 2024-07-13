from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import user, post, category, comment



def blogUser(request):
    myusers = user.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))


def blogPost(request):
    myposts = post.objects.all()
    template = loader.get_template('blogs.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))



def details(request, id):
  mypost = post.objects.get(id=id)
  template = loader.get_template('blogdetails.html')
  context = {
    'mypost': mypost,
  }
  return HttpResponse(template.render(context, request))

def commPost (request):
    mycomments = comment.objects.all()
    template = loader.get_template('comments.html')
    context = {
        'mycomments': mycomments,
    }
    return HttpResponse(template.render(context, request))


def blogCategories(request):
    mycategories = category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'mycategories': mycategories,
    }
    return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
