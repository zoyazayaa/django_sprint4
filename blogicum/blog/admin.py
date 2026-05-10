from django.contrib import admin
from .models import Location, Category, Post


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'location',
        'pub_date', 'is_published', 'created_at'
    )
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'author', 'pub_date')
    search_fields = ('title', 'text')
    date_hierarchy = 'pub_date'
    raw_id_fields = ('author',)
