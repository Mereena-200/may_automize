from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Define a custom UserAdmin class to include the Profile model inline
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Define custom admin class for Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_head')

# Register the Profile model with the custom admin class
admin.site.register(Profile, ProfileAdmin)
