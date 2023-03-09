# Generated by Django 3.2.18 on 2023-03-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0008_comment_num_flags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Unmanaged'), (1, 'Approved')], default=0),
        ),
    ]
