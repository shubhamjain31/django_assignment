# Generated by Django 4.1.2 on 2022-10-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_address_details_coin_market_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin_market',
            options={'ordering': ['-created_at'], 'verbose_name': 'Coin Market'},
        ),
        migrations.AddField(
            model_name='coin_market',
            name='row_number',
            field=models.IntegerField(default=0),
        ),
    ]
