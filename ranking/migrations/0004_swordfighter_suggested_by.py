# Generated by Django 3.2.18 on 2023-02-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0003_swordfighter_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='swordfighter',
            name='suggested_by',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]