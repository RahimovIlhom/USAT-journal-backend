# Generated by Django 5.1.4 on 2024-12-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0003_remove_journalissue_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalissue',
            name='downloads_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Downloads Count'),
        ),
    ]
