# Generated by Django 3.2.6 on 2021-08-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx_notifier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='chat_id',
            field=models.IntegerField(unique=True),
        ),
    ]