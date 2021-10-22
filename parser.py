import json
import subprocess
import random
import time
import csv
import re
import requests
from datetime import datetime, timedelta
import os
from PIL import Image
import glob
import shutil
from os import path
import urllib.parse

print('''
__________________________________________________________________________
''')




loginform=input('Login:  ') or ""
passwordform=input('Password:  ') or ""

shortcode=input('Photo shortcode:  ') or ""
query_hash=input('query_hash param:  ') or ""
basename=input('Name of base:  ') or "base"
basename=basename+'_'+shortcode
spam = False
XInstagramAJAX = csrftoken = ds_user_id = sessionid = ig_did = mid = ig_nrcb = shbid = shbts = rur = XIGWWWClaim = False
XIGAppID = input('Paste XIGAppID or press enter to default: ') or "1217981644879628"
print('IGAppid for your version is: '+XIGAppID)



    
#Open session
def sessionData():
    global XIGWWWClaim
    #link = 'https://www.instagram.com/accounts/login/'
    link = 'https://www.instagram.com/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    localtime = int(datetime.now().timestamp())

#Login and password.
    payload = {
        'username': loginform,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{localtime}:{passwordform}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
#Cookie and headers req.
    with requests.Session() as s:
        r = s.get(link, headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/"})
        csrf = re.findall(r"csrf_token\":\"(.*?)\"",r.text)[0]
        globals()['XInstagramAJAX'] = re.findall(r"rollout_hash\":\"(.*?)\"",r.text)[0]
        coo = dict(r.cookies)
        
        
        


        r = s.post(login_url,data=payload,headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "X-IG-WWW-Claim":'0',
            "x-csrftoken":csrf
        })
        global XIGWWWClaim
        XIGWWWClaim = r.headers['x-ig-set-www-claim']
        
        if r.status_code==403 or r.status_code==429:
            global spam 
            spam = True
            print("ERROR "+str(r.status_code)+" >>> "+r.text)
            timesleep =  datetime.now() + timedelta(seconds=10000)
            print("SLEEPING from "+str(datetime.now())+" to "+str(timesleep))
            time.sleep(10000)
            sessionData()
            

        else:
            cookies=dict(r.cookies)
            res = [(k, v) for k, v in cookies.items()]
            for i in res:globals()[i[0]] = i[1]
            print(r.status_code)
            print('\n\nConnected.')
            
            getcoo()
            time.sleep(random.randint(0,3))
            actions()
            

def getcoo():
    headers={
        'Host': 'www.instagram.com',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'X-ASBD-ID': '198387',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-User': '?1',
        'Referer': 'https://www.instagram.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cookie': f'ig_did={ig_did}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}',
            }

   

    with requests.Session() as s:
        r = s.get('https://www.instagram.com/accounts/onetap/?next=%2F', headers=headers)
        print('Cookies catched.')
        print(r.status_code)
        
        cookies=dict(r.cookies)
        #print(cookies)
        res = [(k, v) for k, v in cookies.items()]
        for i in res:globals()[i[0]] = i[1]
                
def actions():

###REELSTRAY

    headers={
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-IG-WWW-Claim':XIGWWWClaim,
        'X-ASBD-ID': '198387',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
        'X-IG-App-ID': XIGAppID,
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.instagram.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cookie': f'mid={mid}; ig_did={ig_did}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
            }

   

    with requests.Session() as s:
        
        r = s.get('https://i.instagram.com/api/v1/feed/reels_tray/', headers=headers)
        print('Cookies catched.')
        print('Reels_tray code: '+str(r.status_code))
        
        cookies=dict(r.cookies)
        res = [(k, v) for k, v in cookies.items()]
        for i in res:globals()[i[0]] = i[1]

        time.sleep(random.randint(1,5))


       

    ####TIMELINE

        headers={
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'Content-Length': '153',
            'X-IG-WWW-Claim': XIGWWWClaim,
            'X-Instagram-AJAX': XInstagramAJAX,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'X-ASBD-ID': '198387',
            'X-CSRFToken': csrftoken,
            'X-IG-App-ID': XIGAppID,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'Cookie': f'mid={mid}; ig_did={ig_did}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                }

        body={

            'device_id': ig_did,
            'is_async_ads_rti': '0',
            'is_async_ads_double_request': '0',
            'rti_delivery_backend': '0',
            'is_async_ads_in_headload_enabled': '0',

        }

        r = s.post('https://i.instagram.com/api/v1/feed/timeline/', data=body, headers=headers)
        print('timeline catched.')
        cookies=dict(r.cookies)
        #print(cookies)
        res = [(k, v) for k, v in cookies.items()]
        for i in res:globals()[i[0]] = i[1]


        print('timeline code: '+str(r.status_code))
        time.sleep(random.randint(1,5))


    ###########BADGE


        headers={
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'Content-Length': '67',
            'X-IG-WWW-Claim': XIGWWWClaim,
            'X-Instagram-AJAX': XInstagramAJAX,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'X-ASBD-ID': '198387',
            'X-CSRFToken': csrftoken,
            'X-IG-App-ID': XIGAppID,
            'Origin': 'https://www.instagram.com',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.instagram.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'Cookie': f'mid={mid}; ig_did={ig_did}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                }

        body={
            'user_ids': ds_user_id,
            'device_id': ig_did,

        }

        r = s.post('https://i.instagram.com/api/v1/notifications/badge/', data=body, headers=headers)
        cookies=dict(r.cookies)
        #print(cookies)
        res = [(k, v) for k, v in cookies.items()]
        for i in res:globals()[i[0]] = i[1]


        print('badge catched.')
        print('badge code: '+str(r.status_code))
        time.sleep(random.randint(1,5))

    ########MAINFEST

        headers={
                'Host': 'www.instagram.com',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
                'Accept': '*/*',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'manifest',
                'Referer': f'https://www.instagram.com/{loginform}/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
                
                    }



        r = s.get('https://www.instagram.com/data/manifest.json', headers=headers)

        print('MAINFEST catched.')
        print('MAINFEST code: '+str(r.status_code))
        #print(r.content)
        time.sleep(random.randint(1,5))



def pars():
    url='https://www.instagram.com/graphql/query/'
    index = 1
    after = None
    followers_in_progress = 0
    print('Started')
    while True:	
        after_value = f',"after":"{after}"' if after else ''
        variables = f'{{"shortcode":"{shortcode}","include_reel":true,"first":{random.randint(12,24)}{after_value}}}'
        get_params = {
            'query_hash': query_hash,
            'variables': variables
        }
        with requests.Session() as s:

            headers = {

                'Host': 'www.instagram.com',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'X-IG-WWW-Claim': XIGWWWClaim,
                'X-Requested-With': 'XMLHttpRequest',
                'X-ASBD-ID': '198387',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
                'X-CSRFToken': csrftoken,
                'X-IG-App-ID': XIGAppID,
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': f'https://www.instagram.com/p/{shortcode}/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
                'Cookie': f'mid={mid}; ig_did={ig_did}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}; shbid={shbid}; shbts={shbts}; rur={rur}',

                }
                    

            r = s.get(url,  params = get_params, headers=headers)
            data = json.loads(r.text)
            cookies=dict(r.cookies)
            res = [(k, v) for k, v in cookies.items()]
            for i in res:globals()[i[0]] = i[1]
            
        
            if not data['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']:
                break

            after = data['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
            all_followers = data['data']['shortcode_media']['edge_liked_by']['count']
            in_current_batch = len(data['data']['shortcode_media']['edge_liked_by']['edges'])
            followers_in_progress += in_current_batch 
            print(f'>>>>>Checking {followers_in_progress}/{all_followers}<<<<<')
            mkf = open(f'{basename}.csv', mode='a',newline='')
            mkwriter = csv.writer(mkf)
            
            for user in data['data']['shortcode_media']['edge_liked_by']['edges']:
                mkuser_private = user['node']['is_private']
                if not mkuser_private:
                    mkwriter.writerow([user['node']['username']])
                    print(user['node']['username']+'------------opened--------saved')
                else:
                    print(user['node']['username']+'------------closed')
                    
                
                

        time.sleep(random.randint(150,250))

        index += 1
        
    print('...')       
    print('Parsing done!')




sessionData()
pars()














