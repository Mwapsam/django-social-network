from django.contrib import admin
from .models import Friend

class FriendAdmin(admin.ModelAdmin):
    pass
  
admin.site.register(Friend, FriendAdmin)