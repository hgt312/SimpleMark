from django.contrib import admin
from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'mobile')


admin.site.register(UserProfile, UserProfileAdmin)
