# Generated by Django 2.1.1 on 2018-09-23 15:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180923_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristdestination',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touristdestination',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
