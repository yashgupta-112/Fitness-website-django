from django.db import models


# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")
    def __str__(self):
        return "Email by" +" " +self.email


class Blogpost(models.Model):
    blog_id = models.AutoField
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=5000, default="")
    thumbnail = models.ImageField(upload_to='shop/images', default="")
class Client(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    age = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    plan = models.CharField(max_length=500, default="")
    gender = models.CharField(max_length=500, default="")
    transformation = models.CharField(max_length=500, default="")
    def __str__(self):
        return "Email by" +" " +self.email