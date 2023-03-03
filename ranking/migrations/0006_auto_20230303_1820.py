# Generated by Django 3.2.18 on 2023-03-03 18:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ranking', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-submitted_on_date']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reported',
        ),
        migrations.AddField(
            model_name='comment',
            name='flags',
            field=models.ManyToManyField(blank=True, related_name='comment_flag', to=settings.AUTH_USER_MODEL),
        ),
    ]
