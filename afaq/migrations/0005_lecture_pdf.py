# Generated by Django 4.2.1 on 2023-06-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afaq', '0004_alter_lecture_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='pdf',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
    ]
