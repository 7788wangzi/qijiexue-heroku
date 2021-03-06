# Generated by Django 2.1 on 2019-09-17 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='createdate',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 16, 8, 2, 796671), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=500),
        ),
    ]
