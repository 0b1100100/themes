from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'Админ панель тем'
admin.site.site_title = 'Админка темы'
admin.site.register(Themes)
admin.site.register(Category)
admin.site.register(Icon)
admin.site.register(Wallpapers)
admin.site.register(Icons)
admin.site.register(Wallpaper)
admin.site.register(WidgetsLock)
admin.site.register(WidgetsLockS)
admin.site.register(WidgetsHomeH)
admin.site.register(MobileConfig)


class IconInLine(admin.TabularInline):
    model = Icon
    raw_id_fields = ['theme', ]
    extra = 1
    fields = ['id_icon', 'premium', 'name', 'preview', 'icons', 'wallpaper', 'is_publish']


class WallpaperInLine(admin.TabularInline):
    model = Wallpaper
    raw_id_fields = ['theme', ]
    extra = 1
    fields = ['id_wallpapers', 'premium', 'name', 'wallpaper', 'is_publish']


class WidgetHomeHInLine(admin.TabularInline):
    model = WidgetsHomeH
    raw_id_fields = ['theme', ]
    extra = 1
    fields = ['id_Widgets', 'premium', 'name', 'needed_id_name', 'preview', 'widgets', 'is_publish', 'font']


class WidgetLockSInLine(admin.TabularInline):
    model = WidgetsLockS
    raw_id_fields = ['theme', ]
    extra = 1
    fields = ['id_Widgets', 'premium', 'name', 'needed_id_name', 'preview', 'widgets', 'is_publish', 'font']


class ThemeAdmin(admin.ModelAdmin):
    inlines = [IconInLine, WallpaperInLine, WidgetLockSInLine, WidgetHomeHInLine]


admin.site.register(Theme, ThemeAdmin)
