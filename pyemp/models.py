from django.db import models


# Create your models here.


# 生成同步数据库的脚本：python manage.py makemigrations
#
#同步数据库:  python manage.py migrate

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    author = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.id


class Author(models.Model):
    name = models.CharField(max_length=32)
