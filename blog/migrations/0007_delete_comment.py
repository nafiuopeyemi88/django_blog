# Generated by Django 4.0.1 on 2022-02-04 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
