from django.contrib import admin
from .models import PostModel
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=("title","author","publish","status")

admin.site.register(PostModel,PostAdmin)