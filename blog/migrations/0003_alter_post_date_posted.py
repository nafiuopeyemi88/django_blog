# Generated by Django 4.0.1 on 2022-01-28 22:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 22, 9, 32, 712664, tzinfo=utc)),
        ),
    ]
