# Generated by Django 3.1.5 on 2021-01-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_auto_20210124_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='news_images'),
        ),
        migrations.DeleteModel(
            name='newsDetail',
        ),
    ]
