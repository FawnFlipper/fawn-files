# Generated by Django 4.1.2 on 2022-10-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_type_version_files_type_files_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.AlterField(
            model_name='files',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(db_index=True, max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='version',
            name='name',
            field=models.CharField(db_index=True, max_length=40, verbose_name='Название'),
        ),
    ]
