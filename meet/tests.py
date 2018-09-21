# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import unittest
import requests
import json
# Create your tests here.
class TestIndex(unittest.TestCase):

        def test_res(self,maxDiff=None):
            response=requests.get('https://api.meetup.com/find/upcoming_events?photo-host=public&page=20&sig_id=231653554&lon=137&sig=61131d1509f7833b9df56242ca59e38bf8b243e7')

            self.assertEqual(response.json(),{ 'city':{'city':'Nairobi'}})
        

if __name__ == '__main__':
    unittest.main()
