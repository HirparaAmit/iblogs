from django.contrib import admin
from .models import *

# Register your models here.

# Configure category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

# Configure post admin

class PostAdmin(admin.ModelAdmin):
    # list_display = ('title',)
    # search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)