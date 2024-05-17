from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField("포스트 제목", max_length=30)
    content = models.TextField("포스트 내용")
    created_at = models.DateTimeField("작성일시", auto_now_add=True)
    update_at = models.DateTimeField("수정일시", auto_now=True)
    def __str__(self):
        return f"[{self.id}] {self.title}"

    def get_absolute_url(self):
        #return f"/blog/{self.pk}/"
        return reverse("blog:post_detail", kwargs={"blog_id":self.id})