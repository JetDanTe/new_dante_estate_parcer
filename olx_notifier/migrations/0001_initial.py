# Generated by Django 3.2.6 on 2021-08-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=150)),
                ('settings', models.JSONField()),
                ('last_viewed', models.CharField(max_length=300)),
            ],
        ),
    ]