import uuid
from django.db import models


class Themes(models.Model):
    id_themes = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return f'ID: {self.id_themes}; Category: {self.category};'

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"


class Theme(models.Model):
    id_theme = models.AutoField(primary_key=True)
    premium = models.CharField(max_length=255, default='off')
    name = models.CharField(max_length=255)
    preview = models.FileField(upload_to='files/', null=True)
    cat_slug = models.CharField(max_length=255)
    is_publish = models.CharField(max_length=255, default='off')
    font = models.CharField(max_length=255, default='off')

    def __str__(self):
        return f'Premium: {self.premium}; name: {self.name};'

    class Meta:
        verbose_name = "ТемаПод"
        verbose_name_plural = "ТемаПод"


class Category(models.Model):
    id_category = models.CharField(max_length=255)
    theme_name = models.CharField(max_length=255)
    icons = models.CharField(max_length=255)
    premium = models.CharField(max_length=255)

    def __str__(self):
        return f'ID: {self.id_category}; Category: {self.theme_name}; '

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Icon(models.Model):
    id_icon = models.AutoField(primary_key=True)
    premium = models.CharField(max_length=255, default='off')
    name = models.CharField(max_length=255)
    preview = models.FileField(upload_to='files/', null=True)
    icons = models.FileField(upload_to='files/', null=True)
    wallpaper = models.FileField(upload_to='files/', null=True)
    cat_slug = models.CharField(max_length=255)
    is_publish = models.CharField(max_length=255, default='off')

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='icons', null=True)

    def __str__(self):
        return f'Premium: {self.premium}; Name: {self.name};'

    class Meta:
        verbose_name = "ИконкаПод"
        verbose_name_plural = "ИконкиПод"


class Icons(models.Model):
    id_icons = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return f'ID: {self.id_icons}; Category: {self.category}; '

    class Meta:
        verbose_name = "Иконки"
        verbose_name_plural = "Иконки"


class Wallpapers(models.Model):
    id_wallpapers = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return f'ID: {self.id_wallpapers}; Category: {self.category}; '

    class Meta:
        verbose_name = "Обои"
        verbose_name_plural = "Обои"


class Wallpaper(models.Model):
    id_wallpapers = models.AutoField(primary_key=True)
    premium = models.CharField(max_length=255, default='off')
    name = models.CharField(max_length=255)
    wallpaper = models.FileField(upload_to='files/', null=True)
    cat_slug = models.CharField(max_length=255)
    is_publish = models.CharField(max_length=255, default='off')

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='wallpapers', null=True)

    def __str__(self):
        return f'Premium: {self.premium}; Name: {self.name};'

    class Meta:
        verbose_name = "ОбоиПод"
        verbose_name_plural = "ОбоиПод"


class WidgetsLock(models.Model):
    id_Widgets = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return f'ID: {self.id_Widgets}; Category: {self.category}; '

    class Meta:
        verbose_name = "ВиджетLock"
        verbose_name_plural = "ВиджетыLock"


class WidgetsLockS(models.Model):
    id_Widgets = models.AutoField(primary_key=True)
    premium = models.CharField(max_length=255, default='off')
    name = models.CharField(max_length=255)
    needed_id_name = models.CharField(max_length=255, default='default', null=False)
    preview = models.FileField(upload_to='files/', null=True)
    widgets = models.FileField(upload_to='files/', null=True)
    cat_slug = models.CharField(max_length=255)
    is_publish = models.CharField(max_length=255, default='off')
    font = models.CharField(max_length=255, default='off')

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='widget_locks', null=True)

    def __str__(self):
        return f'Premium: {self.premium}; Name: {self.name}; Needed id name: {self.needed_id_name}'

    class Meta:
        verbose_name = "ВиджетLockS"
        verbose_name_plural = "ВиджетыLockS"


class WidgetsHome(models.Model):
    id_Widgets = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', null=True)

    def __str__(self):
        return f'ID: {self.id_Widgets}; Category: {self.category}; '

    class Meta:
        verbose_name = "ВиджетHome"
        verbose_name_plural = "ВиджетыHome"


class WidgetsHomeH(models.Model):
    id_Widgets = models.AutoField(primary_key=True)
    premium = models.CharField(max_length=255, default='off')
    name = models.CharField(max_length=255)
    needed_id_name = models.CharField(max_length=255, default='default', null=False)
    preview = models.FileField(upload_to='files/', null=True)
    widgets = models.FileField(upload_to='files/', null=True)
    cat_slug = models.CharField(max_length=255)
    is_publish = models.CharField(max_length=255, default='off')
    font = models.CharField(max_length=255, default='off')

    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='widget_homes', null=True)

    def __str__(self):
        return f'Premium: {self.premium}; Name: {self.name}; Needed id name: {self.needed_id_name}'

    class Meta:
        verbose_name = "ВиджетHome"
        verbose_name_plural = "ВиджетыHome"


class MobileConfig(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(upload_to='config/', null=False, verbose_name="Файл")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="UUID")

    def __str__(self):
        return f'Name: {self.name}; Created time: {self.created_time};'

    class Meta:
        verbose_name = "Конфигурационный файл"
        verbose_name_plural = "Конфигурационные файлы"
