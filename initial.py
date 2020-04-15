# -*- coding:utf-8 -*-
import requests

def call_api_virus_total_url(url_out):
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': '#', 'url': url_out}
    response = requests.post(url, data=params)
    response_str = response.json()
    str_info = 'response_code : {}\nverbose_msg : {}\nscan_id : {}\nscan_date : {}\nurl : {}\npermalink : {}'.format(response_str['response_code'], response_str['verbose_msg'], response_str['scan_id'], response_str['scan_date'], response_str['url'], response_str['permalink'])
    print(str_info)

call_api_virus_total_url('#')
