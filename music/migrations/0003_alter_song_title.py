# Generated by Django 4.2.1 on 2023-05-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(help_text='song name', max_length=100),
        ),
    ]
