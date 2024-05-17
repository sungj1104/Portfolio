from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.
def index(request):
    return render(request, "index.html")
 
def post_list(request):
    context = {
        "posts" : Post.objects.all(),        
                }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id 값인 Post객체
    
    if request.method == "POST": # method가 POST일 때
        comment_content = request.POST["comment"] #textarea의 name 속성값(comment)를 가져옴
        # 전달된 comment 값으로 Comment 객체를 생성
        Comment.objects.create(
            post=post, content=comment_content)
        # 1. GET 요청으로 글 상세 페이지를 보여주거나
        # 2. POST 요청으로 댓글이 생성되거나
        # 3. 두 경우 모두, 이 글의 상세 페이지를 보여주면 됨
   
    context = {
        "post" : post
    }

    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST": # method가 POST일 때
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES.get("thumbnail", None) # 이미지가 없는 경우에도 업로드 가능
        #thumbnail = request.FILES.["thumbnail"] 이미지가 필수적으로 있을때 사용
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail
        )
        return redirect(f"/posts/{post.id}/")
    
    #else: # method가 POST가 아닐 때, else: 부분은 지워도 상관 없음
    #    print("method GET")
    
    return render(request, "post_add.html")