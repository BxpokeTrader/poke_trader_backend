# Generated by Django 3.0.5 on 2021-01-31 01:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='image',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
