from django.contrib import admin
from instagram.models import Comment, Image, Profile

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('likes',)

admin.site.register(Profile)
admin.site.register(Image,ImageAdmin)
admin.site.register(Comment)