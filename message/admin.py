from django.contrib import admin
from django.contrib.admin import ModelAdmin
from message.models import Message


# Register your models here.


# class MyAdminSite(AdminSite):
#     site_header = '我的'
#     site_title = '我的网站'
#     site_footer = '蒙格格格'


class MessageAdmin(ModelAdmin):
    list_display = ['name', 'messages', 'phone_num', 'email']
    list_filter = ['name', 'phone_num', 'email']
    search_fields = ['name', 'email']


admin.site.site_title = '孟个个个个'
admin.site.register(Message, MessageAdmin)
