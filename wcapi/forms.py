from django import forms
from .models import Themes, Icons, Wallpapers, Theme, Icon, Wallpaper, WidgetsHome, WidgetsLock, WidgetsLockS, \
    WidgetsHomeH


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Themes
        fields = ['category', 'file']


class ResumeFormIcons(forms.ModelForm):
    class Meta:
        model = Icons
        fields = ['category', 'file']


class ResumeFormWallpapers(forms.ModelForm):
    class Meta:
        model = Wallpapers
        fields = ['category', 'file']


class ResumeFormThemesSlug(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'preview', 'cat_slug', 'font']


class ResumeFormThemesSlugPremium(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['premium', 'name', 'preview', 'cat_slug', 'font']


class ResumeFormIconSlug(forms.ModelForm):
    class Meta:
        model = Icon
        fields = ['name', 'preview', 'icons', 'wallpaper', 'cat_slug']


class ResumeFormIconPremium(forms.ModelForm):
    class Meta:
        model = Icon
        fields = ['premium', 'name', 'preview', 'icons', 'wallpaper', 'cat_slug']


class ResumeFormWallpaperSlug(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = ['name', 'wallpaper', 'cat_slug']


class ResumeFormWallpaperPremium(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = ['premium', 'name', 'wallpaper', 'cat_slug']


class ResumeWidgetsHome(forms.ModelForm):
    class Meta:
        model = WidgetsHome
        fields = ['category', 'file']


class ResumeWidgetsLock(forms.ModelForm):
    class Meta:
        model = WidgetsLock
        fields = ['category', 'file']


class ResumeWidgetsLockSlugPremium(forms.ModelForm):
    class Meta:
        model = WidgetsLockS
        fields = ['premium', 'name', 'preview', 'widgets', 'cat_slug', 'font']


class ResumeWidgetsLockSlug(forms.ModelForm):
    class Meta:
        model = WidgetsLockS
        fields = ['name', 'preview', 'widgets', 'cat_slug', 'font']


class ResumeWidgetsHomeSlugPremium(forms.ModelForm):
    class Meta:
        model = WidgetsHomeH
        fields = ['premium', 'name', 'preview', 'widgets', 'cat_slug', 'font']


class ResumeWidgetsHomeSlug(forms.ModelForm):
    class Meta:
        model = WidgetsHomeH
        fields = ['name', 'preview', 'widgets', 'cat_slug', 'font']
