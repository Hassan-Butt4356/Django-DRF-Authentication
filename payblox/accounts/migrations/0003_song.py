# Generated by Django 4.1.2 on 2022-10-31 21:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('singers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
