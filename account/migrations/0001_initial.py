# Generated by Django 4.2.1 on 2023-06-27 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aug', models.BooleanField(default=False)),
                ('sep', models.BooleanField(default=False)),
                ('oct', models.BooleanField(default=False)),
                ('nov', models.BooleanField(default=False)),
                ('dec', models.BooleanField(default=False)),
                ('jan', models.BooleanField(default=False)),
                ('feb', models.BooleanField(default=False)),
                ('mar', models.BooleanField(default=False)),
                ('apr', models.BooleanField(default=False)),
                ('may', models.BooleanField(default=False)),
                ('jun', models.BooleanField(default=False)),
                ('jul', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
