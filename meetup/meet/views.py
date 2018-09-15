# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

def index(request):
    response=requests.get('https://api.meetup.com/find/upcoming_events?photo-host=public&page=20&sig_id=231653554&lon=137&sig=61131d1509f7833b9df56242ca59e38bf8b243e7')
    data=response.json()
    return render(request,'index.html',{'data':data})
def details(request):
    response=requests.get('https://api.meetup.com/find/upcoming_events?photo-host=public&page=20&sig_id=231653554&lon=137&sig=61131d1509f7833b9df56242ca59e38bf8b243e7')
    info=response.json()
    return render(request,'detail.html',{'info':info})



# Create your views here.
# # 'id':data['events'][0]['id'],
# "name":data['events'][0]['name'],
# "time":data['events'][0]['time'],
# # "featured_photo":data['events'][0]['featured_photo'],
# "local_date":data['events'][0]['local_date'],
# "local_time":data['events'][0]['local_time'],
# "venue_name":data['events'][0]['venue']['name'],
# "venue_address":data['events'][0]['venue']['address_1'],
# 'api_key': '783c4f5927046604e3d7b4222497458',
