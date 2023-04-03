# Generated by Django 4.1.5 on 2023-01-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcapi', '0002_wallpaper_alter_icon_options_alter_icon_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='WidgetsHome',
            fields=[
                ('id_Widgets', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
            options={
                'verbose_name': 'ВиджетHome',
                'verbose_name_plural': 'ВиджетыHome',
            },
        ),
        migrations.CreateModel(
            name='WidgetsLock',
            fields=[
                ('id_Widgets', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
            options={
                'verbose_name': 'ВиджетLock',
                'verbose_name_plural': 'ВиджетыLock',
            },
        ),
        migrations.DeleteModel(
            name='Widgets',
        ),
    ]
