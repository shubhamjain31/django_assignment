from celery import shared_task

from home.scraper import scrape_website
from home.models import Detail, Coin_Market

import requests, json

@shared_task(bind=True)
def bulk_added_coin_market(self):
    obj     = Detail.objects.last()
    index   = obj.row_number
    data_list = scrape_website()

    headers = {'content-type': 'application/json'}

    data = dict()
    data['coin_data'] = data_list[index:index+2]
    requests.post('http://localhost:8000/api/cryptocurrency/', data=json.dumps(data), headers=headers)

    obj.row_number = index+2
    obj.save()
    print('Bulk Created!')

@shared_task(bind=True)
def bulk_update_coin_market(self):
    obj     = Detail.objects.last()
    index   = obj.row_number

    all_pks = list(Coin_Market.objects.values_list('id', flat=True))

    if len(all_pks) == 0:
        return
        
    data_list = scrape_website()

    headers = {'content-type': 'application/json'}

    data = dict()
    data['coin_data'] = data_list[0:index]
    data['all_pks'] = all_pks
    requests.put('http://localhost:8000/api/cryptocurrency/', data=json.dumps(data), headers=headers)

    print('Bulk Updated!')