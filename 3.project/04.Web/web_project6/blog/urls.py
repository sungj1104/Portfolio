from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    # path("", views.index, name="index"), # FBV 방식 게시글 목록페이지
    path("", views.PostList.as_view(), name="post_list"),
    path("<int:blog_id>/", views.single_post_page, name="post_detail"),
]
