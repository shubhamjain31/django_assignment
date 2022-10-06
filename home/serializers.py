from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from home.models import Coin_Market
  
class CoinMarketSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coin_Market
        fields = ("name", 'price', 'market_cap', 'volume24h', 'one_hour_per', 'one_day_per', 'seven_day_per', 'coin_data', 'created_at')
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        objs = [
        Coin_Market(
            name=row['name'],
            price=row['price'],
            market_cap=row['market_cap'],
            volume24h=row['volume24h'],
            circulating_supply=row['circulating_supply'],
            one_hour_per=row['one_hour_per'],
            one_day_per=row['one_day_per'],
            seven_day_per=row['seven_day_per'],
            coin_data=row
            
        )
        for row in validated_data['coin_data']
        ]

        return Coin_Market.objects.bulk_create(objs)

    def update(self, validated_data):
        Coin_Market.objects.bulk_update(
            [
                Coin_Market(id=id_, name=values.get("name"), price=values.get("price"), market_cap=values.get("market_cap"),
                            volume24h=values.get("volume24h"), one_hour_per=values.get("one_hour_per"), one_day_per=values.get("one_day_per"),
                            seven_day_per=values.get("seven_day_per"), circulating_supply=values.get("circulating_supply"))
                for id_, values in zip(validated_data['all_pks'], validated_data['coin_data'])
            ],
            ["name", "price", "market_cap", "volume24h", "one_hour_per", "one_day_per", "seven_day_per", "circulating_supply"],
            batch_size=1000
        )
        return validated_data