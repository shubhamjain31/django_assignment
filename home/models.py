from django.db import models

# Create your models here.

class Coin_Market(models.Model):
    name                    = models.CharField(max_length=150, blank=True, null=True)
    price                   = models.IntegerField(blank=True, null=True)
    market_cap              = models.CharField(max_length=150, blank=True, null=True) 
    volume24h               = models.CharField(max_length=150, blank=True, null=True) 
    circulating_supply      = models.CharField(max_length=150, blank=True, null=True) 
    one_hour_per            = models.CharField(max_length=150, blank=True, null=True) 
    one_day_per             = models.CharField(max_length=150, blank=True, null=True) 
    seven_day_per           = models.CharField(max_length=150, blank=True, null=True) 
    coin_data               = models.JSONField(default=dict)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Coin Market'
        ordering = ["-created_at"]

class Detail(models.Model):
    row_number              = models.IntegerField(default=0)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.row_number)

    class Meta:
        verbose_name = 'Detail'
        ordering = ["-created_at"]