from django.db import models


# create role
class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "角色"
        verbose_name_plural = "角色"


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    role = models.ForeignKey('Role',on_delete=models.CASCADE,default=0)
    active = models.BooleanField(max_length=1,default=0)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
