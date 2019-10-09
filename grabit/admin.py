from django.contrib import admin
from .models import User, Item

# Register your models here.

@admin.register(Item)
class Item(admin.ModelAdmin):
    fields = ('title', 'description', 'img', 'is_worthy')
    list_display = ('title', 'description', 'is_worthy')



# PRE DEFINED ###########################
@admin.register(User)
class User(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'is_worthy')
    list_display = ('first_name', 'last_name', 'email', 'is_worthy')