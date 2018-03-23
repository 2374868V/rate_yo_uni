from django.contrib import admin
from project.models import *

# Register your models here


class BathroomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'bathroomSlug': ('bathroomSlug',)}
    fieldsets = [
        (None, {'fields': ['name', 'bathroomSlug']}),
        ('Required', {'fields': ['building', 'level', 'gender']}),
        ('Not required', {'fields': ['rating', 'image']}),
    ]


class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'userSlug': ('user_name',)}


admin.site.register(Bathroom, BathroomAdmin)
admin.site.register(BathroomInteraction)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Comment)
admin.site.register(BathroomImage)