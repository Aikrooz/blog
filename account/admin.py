from django.contrib import admin
from .forms import BlogUserCreationForm,BlogUserUpdateForm
from .model import BlogUser
# Register your models here.
class BlogUserAdmin(UserAdmin):
    add_form=BlogUserCreation
    form=BlogUserUpdateForm
    model=BlogUser

admin.site.register(BlogUser,BlogUserAdmin)