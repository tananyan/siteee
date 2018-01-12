# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import os


def avatar_upload_to(instance, filename):
    return os.path.join(os.path.splitext(filename)[0]+os.path.splitext(filename)[1])


class Articles(models.Model):
    title = models.CharField(max_length=100, verbose_name="Загаловок ")
    post = models.TextField(verbose_name="Статья")
    date = models.DateTimeField(verbose_name="Дата")
    image = models.ImageField(upload_to=avatar_upload_to, verbose_name="Картинка")

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Комментарии")
    comments_date = models.DateField(u'date',auto_now=True)
    comments_article = models.ForeignKey(Articles, verbose_name="Статья")
    comments_author = models.ForeignKey(User, verbose_name="Автор")

    def __str__(self):
        return self.comments_text