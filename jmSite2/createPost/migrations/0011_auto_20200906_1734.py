# Generated by Django 3.1.1 on 2020-09-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createPost', '0010_auto_20200905_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='createdbpost',
            name='order',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='createdbpost',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]