# Generated by Django 4.1.2 on 2022-10-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin_market',
            name='row_number',
        ),
        migrations.AddField(
            model_name='coin_market',
            name='coin_data',
            field=models.JSONField(default=dict),
        ),
    ]
