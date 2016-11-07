from django.contrib import admin
from .models import Post
from .models import Post2, Comment, Title

# Register your models here.

admin.site.register(Post)
admin.site.register(Post2)
admin.site.register(Comment)
admin.site.register(Title)