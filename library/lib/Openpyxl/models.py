from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=28, default='默认用户')
    count = models.CharField(max_length=128, unique=True)
    sex = models.CharField(max_length=10, default='男')
    age = models.IntegerField(default=18)
    university = models.CharField(max_length=64, default='世界一流大学')

    class Meta:
        verbose_name = '用户'
        db_table = '用户'