# Generated by Django 3.1.5 on 2021-01-26 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_delete_usercat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(),
        ),
    ]
