# Generated by Django 5.1.4 on 2024-12-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_options_category_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
