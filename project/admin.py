from django.contrib import admin
from project.models import *

# Register your models here


class BathroomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'b_slug': ('name',)}
    fieldsets = [
        ('Required', {'fields': ['name', 'building', 'level', 'gender']}),
        ('Not required', {'fields': ['rating']}),
        ('Prepopulated', {'fields': ['b_slug']})
    ]


class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'userSlug': ('user',)}


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Required', {'fields': ['comment', 'user', 'bathroom']}),
    ]


admin.site.register(Bathroom, BathroomAdmin)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rate)
