
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20)

    def getPosts(self):
        return self.post_set

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    #post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    text = models.TextField()
    cdate = models.DateField(auto_now=False)
    visible = models.BooleanField() 

