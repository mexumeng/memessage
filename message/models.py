from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(default='', max_length=10, verbose_name='姓名')
    messages = models.CharField(max_length=500, verbose_name='留言信息')
    phone_num = models.CharField(max_length=11, verbose_name='联系地址')
    email = models.EmailField(default='', verbose_name='邮箱')
