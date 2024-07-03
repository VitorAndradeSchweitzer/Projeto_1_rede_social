from django.db import models

from django.contrib.auth.models import User


class Conta(models.Model):
    picture = models.ImageField(upload_to='profile/covers/%y/%m/%d')
    user= models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.user.username

    

class Post(models.Model):

    author_profile = models.ForeignKey(Conta, on_delete= models.SET_NULL, null=True, blank='True')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank='True')
    text = models.CharField(max_length=1600)
    image = models.ImageField(upload_to='posts/covers/%y/%m/%d', null=True, blank='True')
    likes = models.IntegerField(default=0)
   
    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='user_likes')
    post = models.ForeignKey(Post,on_delete=models.CASCADE ,related_name='post_likes')
    def user_has_liked(self, user):
        return self.like_set.filter(user=user).exists()

class Save(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='user_saves')
    post = models.ForeignKey(Post,on_delete=models.CASCADE ,related_name='post_saves')
     
    def __str__(self):
        return self.post