# Generated by Django 4.2.1 on 2023-06-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afaq', '0006_lecture_videourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='pdf',
            field=models.URLField(blank=True),
        ),
    ]