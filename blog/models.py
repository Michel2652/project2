from collections.abc import Iterable
from django.db import models
from accounts.models import UserProfile
from django.urls import reverse_lazy
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug=models.SlugField(max_length=300,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    like=models.ManyToManyField(UserProfile,related_name="post_like",null=True,blank=True)
    dislike=models.ManyToManyField(UserProfile,related_name="post_dislike",null=True,blank=True)

    def __str__(self):
        return self.body + " " + str(self.id)
    
    def  get_absolute_url(self):
        return reverse_lazy("post", kwargs={"slug": self.slug})
    
    def save(self,*args, **kwargs):
        super().save()
        if not self.slug :
            self.slug= slugify(self.title)
            self.save()


class Comment(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    body = models.TextField(null=True)
#    is_validate = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    update_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f'{self.created_at}'

