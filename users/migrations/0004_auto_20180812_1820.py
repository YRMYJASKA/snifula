# Generated by Django 2.1 on 2018-08-12 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180811_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='usercomment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='userpost',
            name='author',
        ),
        migrations.DeleteModel(
            name='UserComment',
        ),
        migrations.DeleteModel(
            name='UserPost',
        ),
    ]
