# Generated by Django 3.1.1 on 2020-09-05 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createPost', '0006_auto_20200905_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
