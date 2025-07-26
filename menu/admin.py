from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_slug')

    def get_slug(self, obj):
        return obj.slug
    get_slug.short_description = 'Slug'

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_menu', 'get_parent', 'get_slug')
    list_filter = ('menu',)

    def get_menu(self, obj):
        return obj.menu.title
    get_menu.short_description = 'Menu'

    def get_parent(self, obj):
        return obj.parent.title if obj.parent else '-'
    get_parent.short_description = 'Parent'

    def get_slug(self, obj):
        return obj.slug if obj.slug else '-'
    get_slug.short_description = 'URL'
