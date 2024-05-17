from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

#Create your views here.
# def index(request):
#     # '''
#     # FBB 장식 게시글 목록 페이지
#     # '''
#     posts = Post.objects.all().order_by("-pk")
#     context = {"posts": posts,}
#     return render(request,"blog/blog_list.html", context)

class PostList(ListView):
    model = Post
    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    ordering = "-pk"

def single_post_page(request, blog_id):
    post = Post.objects.get(id=blog_id)
    context = {"bb" : post}
    return render(request, "blog/single_post_page.html", context)