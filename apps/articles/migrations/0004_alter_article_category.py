# Generated by Django 5.1.4 on 2024-12-21 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_original_file'),
        ('categories', '0003_alter_category_options_category_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category', verbose_name='Direction'),
        ),
    ]
