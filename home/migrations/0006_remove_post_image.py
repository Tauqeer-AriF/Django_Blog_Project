# Generated by Django 3.1.6 on 2021-02-22 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
