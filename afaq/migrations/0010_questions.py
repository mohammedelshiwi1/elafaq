# Generated by Django 4.2.1 on 2023-06-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afaq', '0009_alter_lecture_lecture_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('ques', models.CharField(max_length=200)),
            ],
        ),
    ]
