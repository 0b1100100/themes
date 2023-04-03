# Generated by Django 4.1.5 on 2023-01-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wcapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallpaper',
            fields=[
                ('id_wallpapers', models.AutoField(primary_key=True, serialize=False)),
                ('premium', models.CharField(default='off', max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('wallpaper', models.FileField(null=True, upload_to='files/')),
                ('cat_slug', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'ОбоиПод',
                'verbose_name_plural': 'ОбоиПод',
            },
        ),
        migrations.AlterModelOptions(
            name='icon',
            options={'verbose_name': 'ИконкаПод', 'verbose_name_plural': 'ИконкиПод'},
        ),
        migrations.AlterField(
            model_name='icon',
            name='premium',
            field=models.CharField(default='off', max_length=255),
        ),
    ]