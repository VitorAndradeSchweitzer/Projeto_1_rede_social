from django.contrib import admin
from .models import Conta,Post, Like, Save
# Register your models here.

class ContaAdmin(admin.ModelAdmin):
    ...
admin.site.register(Conta, ContaAdmin)

class PostsAdmin(admin.ModelAdmin):
    ...
admin.site.register(Post, PostsAdmin)

class LikesAdmin(admin.ModelAdmin):
    ...
admin.site.register(Like, LikesAdmin)

class SavesAdmin(admin.ModelAdmin):
    ...
admin.site.register(Save,SavesAdmin)