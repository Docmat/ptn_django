from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post


def main_page(request):
    posts = Post.objects.all()  # select * from Post
    context = {
        "posts": posts
    }
    return render(request, "main_page.html", context=context)


def post_detail(request, pk):
    print(dir(request))
    post = Post.objects.get(pk=pk)
    return render(request,
                  "post_detail.html",
                  locals())


def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES["image"]
        print(image)
        post_obj = Post.objects.create(
            title=title, content=content, image=image)
        return redirect("main-page")
    return render(request, "post_create.html")

