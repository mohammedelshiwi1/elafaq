# Generated by Django 4.2.1 on 2023-06-26 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afaq', '0003_rename_messages_notfication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]