# Generated by Django 4.2.1 on 2023-06-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afaq', '0010_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='img',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
