# Generated by Django 4.1.5 on 2023-01-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_category', models.CharField(max_length=255)),
                ('theme_name', models.CharField(max_length=255)),
                ('icons', models.CharField(max_length=255)),
                ('premium', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id_icon', models.AutoField(primary_key=True, serialize=False)),
                ('premium', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('preview', models.FileField(null=True, upload_to='files/')),
                ('icons', models.FileField(null=True, upload_to='files/')),
                ('wallpaper', models.FileField(null=True, upload_to='files/')),
                ('cat_slug', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Иконка',
                'verbose_name_plural': 'Иконки',
            },
        ),
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id_icons', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
            options={
                'verbose_name': 'Иконки',
                'verbose_name_plural': 'Иконки',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id_theme', models.AutoField(primary_key=True, serialize=False)),
                ('premium', models.CharField(default='off', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('preview', models.FileField(null=True, upload_to='files/')),
                ('icons', models.FileField(null=True, upload_to='files/')),
                ('wallpaper', models.FileField(null=True, upload_to='files/')),
                ('widgets', models.FileField(null=True, upload_to='files/')),
                ('cat_slug', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'ТемаПод',
                'verbose_name_plural': 'ТемаПод',
            },
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id_themes', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Wallpapers',
            fields=[
                ('id_wallpapers', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('amount', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
            options={
                'verbose_name': 'Обои',
                'verbose_name_plural': 'Обои',
            },
        ),
        migrations.CreateModel(
            name='Widgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Widgets', models.CharField(max_length=255)),
                ('premium', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('preview', models.CharField(max_length=255)),
                ('widgets', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Виджет',
                'verbose_name_plural': 'Виджеты',
            },
        ),
    ]
