from rest_framework import serializers
from .models import Themes, Icon, Theme, Wallpaper, WidgetsLockS, WidgetsHomeH, MobileConfig


class WcapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = ('id_themes', 'category', 'amount')


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = '__all__'


class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallpaper
        fields = '__all__'


class WidgetLockSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidgetsLockS
        fields = '__all__'


class WidgetHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidgetsHomeH
        fields = '__all__'


class ThemeSerializer(serializers.ModelSerializer):
    wallpapers = WallpaperSerializer(many=True)
    icons = IconSerializer(many=True)
    widget_locks = WidgetLockSerializer(many=True)
    widget_homes = WidgetHomeSerializer(many=True)

    class Meta:
        model = Theme
        fields = '__all__'


class MobileConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileConfig
        fields = ['name', 'file']
