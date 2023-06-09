from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from drfsitewc import settings
from wcapi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('icons', icons, name='icons'),
    path('wallpapers', wallpapers, name='wallpapers'),
    path('themes/add_category', index_add_category, name='index_add_category'),
    path('themes/del_category/<slug:cat_slug>/', index_del_category, name='index_del_category'),
    path('icons/del_category/<slug:cat_slug>/', icons_del_category, name='icons_del_category'),
    path('wallpapers/del_category/<slug:cat_slug>/', wallpapers_del_category, name='wallpapers_del_category'),
    path('themes/<slug:cat_slug>/', index_cat_slug, name='index_cat_slug'),
    path('themesp/<slug:cat_slug>/<slug:pwev_slug>', p_index_cat_slug, name='p_index_cat_slug'),
    path('themesp/edit/<slug:cat_slug>/<slug:pwev_slug>', edit_index_cat_slug, name='edit_index_cat_slug'),
    path('themesp/delete/<slug:cat_slug>/<slug:pwev_slug>', del_p_index_cat_slug, name='del_p_index_cat_slug'),
    path('themeadd/<slug:cat_slug>/', index_add_cat_slug, name='index_add_cat_slug'),
    path('icons/<slug:cat_slug>/', icons_cat_slug, name='icons_cat_slug'),
    path('iconsp/<slug:cat_slug>/<slug:pwev_slug>', p_icons_cat_slug, name='p_icons_cat_slug'),
    path('iconsp/edit/<slug:cat_slug>/<slug:pwev_slug>', edit_icons_cat_slug, name='edit_icons_cat_slug'),
    path('iconsp/delete/<slug:cat_slug>/<slug:pwev_slug>', del_p_icons_cat_slug, name='del_p_icons_cat_slug'),
    path('iconadd/<slug:cat_slug>/', icon_add_cat_slug, name='icon_add_cat_slug'),
    path('wallpapers/<slug:cat_slug>/', wallpapers_cat_slug, name='wallpapers_cat_slug'),
    path('wallpapersp/<slug:cat_slug>/<slug:pwev_slug>', p_wallpapers_cat_slug, name='p_wallpapers_cat_slug'),
    path('wallpapers/edit/<slug:cat_slug>/<slug:pwev_slug>', edit_wallpapers_cat_slug, name='edit_wallpapers_cat_slug'),
    path('wallpapersp/delete/<slug:cat_slug>/<slug:pwev_slug>', del_p_wallpapers_cat_slug,
         name='del_p_wallpapers_cat_slug'),
    path('walladd/<slug:cat_slug>/', wallpapers_add_cat_slug, name='wallpapers_add_cat_slug'),
    path('icons/add_category', icons_add_category, name='icons_add_category'),
    path('wallpapers/add_category', wallpapers_add_category, name='wallpapers_add_category'),
    path('widgetslock', widgetslock, name='widgetslock'),
    path('widgetslock/add_category', widgetslock_add_category, name='widgetslock_add_category'),
    path('widgetslock/del_category/<slug:cat_slug>/', widgetslock_del_category, name='widgetslock_del_category'),
    path('widgetslock/<slug:cat_slug>/', widgetslock_cat_slug, name='widgetslock_cat_slug'),
    path('widgetslockadd/<slug:cat_slug>/', widgetslock_add_cat_slug, name='widgetslock_add_cat_slug'),
    path('widgetslockp/delete/<slug:cat_slug>/<slug:pwev_slug>', del_p_widgetslock_cat_slug,
         name='del_p_widgetslock_cat_slug'),
    path('widgetslockp/<slug:cat_slug>/<slug:pwev_slug>', p_widgetslock_cat_slug, name='p_widgetslock_cat_slug'),
    path('widgetslockp/edit/<slug:cat_slug>/<slug:pwev_slug>', edit_widgetslock_cat_slug,
         name='edit_widgetslock_cat_slug'),
    path('widgetshome', widgetshome, name='widgetshome'),
    path('widgetshome/add_category', widgetshome_add_category, name='widgetshome_add_category'),
    path('widgetshome/del_category/<slug:cat_slug>/', widgetshome_del_category, name='widgetshome_del_category'),
    path('widgetshome/<slug:cat_slug>/', widgetshome_cat_slug, name='widgetshome_cat_slug'),
    path('widgetshomeadd/<slug:cat_slug>/', widgetshome_add_cat_slug, name='widgetshome_add_cat_slug'),
    path('widgetshomep/delete/<slug:cat_slug>/<slug:pwev_slug>', del_p_widgetshome_cat_slug,
         name='del_p_widgetshome_cat_slug'),
    path('widgetshomep/<slug:cat_slug>/<slug:pwev_slug>', p_widgetshomep_cat_slug, name='p_widgetshomep_cat_slug'),
    path('widgetshomep/edit/<slug:cat_slug>/<slug:pwev_slug>', edit_widgetshomep_cat_slug,
         name='edit_widgetshomep_cat_slug'),

    path('api/v1/themes', ThemesAPIView.as_view()),
    path('api/v1/themes/add_category', ThemesAddCategoryAPIView.as_view()),
    path('api/v1/themes/del_category', ThemesDelCategoryAPIView.as_view()),
    path('api/v1/themes/cat_slug', ThemesCatSlugAPIView.as_view()),
    path('api/v1/themesadd/cat_slug', ThemesAddCatSlugAPIView.as_view()),
    path('api/v1/themesp/delete/catslug/pwevslug', ThemespDelCatPweAPIView.as_view()),
    path('api/v1/themesp/catslug/pwevslug', ThemespCatPweAPIView.as_view()),
    path('api/v1/themesp/edit/catslug/pwevslug', ThemespEditCatPweAPIView.as_view()),

    path('api/v1/icons', IconsAPIView.as_view()),
    path('api/v1/icons/add_category', IconsAddCategoryAPIView.as_view()),
    path('api/v1/icons/del_category', IconsDelCategoryAPIView.as_view()),
    path('api/v1/icons/cat_slug', IconsCatSlugAPIView.as_view()),
    path('api/v1/iconsadd/cat_slug', IconsAddCatSlugAPIView.as_view()),
    path('api/v1/iconsp/delete/catslug/pwevslug', IconspDelCatPweAPIView.as_view()),
    path('api/v1/iconsp/catslug/pwevslug', IconspCatPweAPIView.as_view()),
    path('api/v1/iconsp/edit/catslug/pwevslug', IconspEditCatPweAPIView.as_view()),
    path('api/v1/widgetslock', WidgetsLockAPIView.as_view()),
    path('api/v1/widgetslock/add_category', WidgetsLockAddCategoryAPIView.as_view()),
    path('api/v1/widgetslock/del_category', WidgetsLockDelCategoryAPIView.as_view()),
    path('api/v1/widgetslock/cat_slug', WidgetsLockCatSlugAPIView.as_view()),
    path('api/v1/widgetslockadd/cat_slug', WidgetsLockAddCatSlugAPIView.as_view()),
    path('api/v1/widgetslock/delete/catslug/pwevslug', WidgetsLockDelCatPweAPIView.as_view()),
    path('api/v1/widgetslock/catslug/pwevslug', WidgetsLockCatPweAPIView.as_view()),
    path('api/v1/widgetslock/edit/catslug/pwevslug', WidgetsLockEditCatPweAPIView.as_view()),

    path('api/v1/widgetshome', WidgetsHomeAPIView.as_view()),
    path('api/v1/widgetshome/add_category', WidgetsHomeAddCategoryAPIView.as_view()),
    path('api/v1/widgetshome/del_category', WidgetsHomeDelCategoryAPIView.as_view()),
    path('api/v1/widgetshome/cat_slug', WidgetsHomeCatSlugAPIView.as_view()),
    path('api/v1/widgetshomeadd/cat_slug', WidgetsHomeAddCatSlugAPIView.as_view()),
    path('api/v1/widgetshome/delete/catslug/pwevslug', WidgetsHomeDelCatPweAPIView.as_view()),
    path('api/v1/widgetshome/catslug/pwevslug', WidgetsHomeCatPweAPIView.as_view()),
    path('api/v1/widgetshome/edit/catslug/pwevslug', WidgetsHomeEditCatPweAPIView.as_view()),

    path('api/v1/wallpapers', WallpapersAPIView.as_view()),
    path('api/v1/wallpapers/add_category', WallpapersAddCategoryAPIView.as_view()),
    path('api/v1/wallpapers/del_category', WallpapersDelCategoryAPIView.as_view()),
    path('api/v1/wallpapers/cat_slug', WallpapersCatSlugAPIView.as_view()),
    path('api/v1/wallpapersadd/cat_slug', WallpapersAddCatSlugAPIView.as_view()),
    path('api/v1/wallpapers/delete/catslug/pwevslug', WallpapersDelCatPweAPIView.as_view()),
    path('api/v1/wallpapers/catslug/pwevslug', WallpapersCatPweAPIView.as_view()),
    path('api/v1/wallpapers/edit/catslug/pwevslug', WallpapersEditCatPweAPIView.as_view()),

    path('download/', download_file.as_view(), name='download'),

    path('api/v1/mobileconfig/', ConfigFileAPIView.as_view()),
    path('api/v1/mobileconfig/<str:file_uuid>/', GetConfigFileAPIView.as_view(), name='get_config_file_path'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
