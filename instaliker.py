import json
import subprocess
import random
import time
import csv
import re
import requests
from datetime import datetime, timedelta

loginform=False
passwordform=False
spam = False
base = 'base.csv'
counter = 0
counterLook = 0
XInstagramAJAX = csrftoken = ds_user_id = sessionid = ig_did = mid = ig_nrcb = shbid = shbts = rur = XIGWWWClaim = False
XIGAppID = "1217981644879628"
print('IGAppid for your version is: '+XIGAppID)
likable = False
photocode = False

if os.path.isfile('login.txt'):
    logins={}
    with open('login.txt','r') as file:
        lgns = file.read().splitlines()
        for i in lgns:
            slic=i.split(":")
            logins[slic[0]]=slic[1]
            
    loginbase = [(k, v) for k, v in logins.items()]
    loginform=loginbase[0][0]
    passwordform=loginbase[0][1]
    print(logins)

#Открываем сессию и получаем куки
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
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/"})
        csrf = re.findall(r"csrf_token\":\"(.*?)\"",r.text)[0]
        globals()['XInstagramAJAX'] = re.findall(r"rollout_hash\":\"(.*?)\"",r.text)[0]
        
        
        
        


        r = s.post(login_url,data=payload,headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "X-IG-WWW-Claim":'0',
            "x-csrftoken":csrf
        })
        global XIGWWWClaim
        XIGWWWClaim = r.headers['x-ig-set-www-claim']
        print(XIGWWWClaim)
        time.sleep(30)
        
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

            
def getcoo():
    headers={
        'Host': 'www.instagram.com',
        'Connection': 'keep-alive',
        ###
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'X-ASBD-ID': '198387',
        ###
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
        res = [(k, v) for k, v in cookies.items()]
        for i in res:globals()[i[0]] = i[1]
                
################################################################################        	

def checkuser(username):
    global photocode
    photocode = False
    media_id=''
    global likable
    likable = False
    link = f'https://www.instagram.com/{username}/?__a=1'
    with requests.Session() as s:

      headers = {

        'Host': 'www.instagram.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-IG-WWW-Claim': XIGWWWClaim,
        'X-Requested-With': 'XMLHttpRequest',
        'X-ASBD-ID': '198387',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'X-IG-App-ID': XIGAppID,
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://www.instagram.com/{username}/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cookie': f'mid={mid}; ig_did={ig_did}; shbid={shbid}; shbts={shbts}; rur={rur}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}',
          }  

      r = s.get(link, headers = headers)
      
      try:
        data = json.loads(r.text)
        cookies=dict(r.cookies)
        res = [(k, v) for k, v in cookies.items()]
        for i in res:globals()[i[0]] = i[1]
      except:
          print('bad_data')
          raise
    #########

    try:
        spamcheck = data['spam']
        if spamcheck:
            print('CHECK USER SPAM DETECTED')
            timesleep =  datetime.now() + timedelta(seconds=5000)
            print("SLEEPING from "+str(datetime.now())+" to "+str(timesleep)) 
            time.sleep(10000)
            sessionData()
            time.sleep(600)

    except: print('----------------------------------')                
    try:
        private = data['graphql']['user']['is_private']
        posts = data['graphql']['user']['edge_owner_to_timeline_media']['count']
        followed = data['graphql']['user']['followed_by_viewer']
        follows = data['graphql']['user']['follows_viewer']
        likable = True
        if private or posts < 4 or followed or follows:
            likable = False
            global counterLook
            global counter
            counterLook+=1
            time.sleep(random.randint(20,40))
            if counterLook % 5 == 0:
            	print('Sleeping 5 min to checking')
            	time.sleep(500)
            	#REPLACE COUTER SLEEP TO SENDLIKE FUNCTION AFTER COUNTER ITERATOR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    
            print('@> '+username+' >>>is not valid account!...... LOOKING   '+str(counterLook))
    except: print(username+'  page not found')
    if likable:
	photonum=random.randint(0,3)
        media_id=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][photonum]['node']['id']
	photocode=data['graphql']['user']['edge_owner_to_timeline_media']['edges'][photonum]['node']['shortcode']
        print(username+ "  >>> Sending like!")    
        return media_id

#################################################################################            
def sendlike(media_id):
    global likable
    ######################### LOGIC TO IF LIKABE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if likable:
        linklike = f'https://www.instagram.com/web/likes/{media_id}/like/'
        try:
            global counter
            

            
            with requests.Session() as s:

                headers={

                    'Host': 'www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '0',
                    'X-IG-WWW-Claim': XIGWWWClaim,
                    'X-Instagram-AJAX': XInstagramAJAX,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                    'X-CSRFToken': csrftoken,
                    'X-IG-App-ID': XIGAppID,
                    'Origin': 'https://www.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': f'https://www.instagram.com/p/{photocode}/',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
                    'Cookie': f'mid={mid}; ig_did={ig_did}; shbid={shbid}; shbts={shbts}; rur={rur}; csrftoken={csrftoken}; ds_user_id={ds_user_id}; sessionid={sessionid}',
            
                    }
                
                r = s.post(linklike,headers=headers)
                
            liked = json.loads(r.text)
            try:
                spamlike = liked['spam']
                if spamlike:
                    print('Like SPAM DETECTED!')
                    timesleep =  datetime.now() + timedelta(seconds=5000)
                    print("SLEEPING from "+str(datetime.now())+" to "+str(timesleep))
                    time.sleep(5000)
                    sessionData()
                    time.sleep(600)

            except:
                    cookies=dict(r.cookies)
                    res = [(k, v) for k, v in cookies.items()]
                    for i in res:globals()[i[0]] = i[1]

                    counter+=1
                    print("  >>> liked!....  "+str(counter))
                    print('Sleeping after like 2-3 min')
                    time.sleep(random.randint(120,200))
                    
                    if counter % 3 == 0:
                        print('Sleeping 10 min to like')
                        time.sleep(600)
                
                    if counter % 100 == 0:
                        print('DOING 100 likes!')
                        timesleep =  datetime.now() + timedelta(seconds=5000)
                        print("SLEEPING from "+str(datetime.now())+" to "+str(timesleep))
                        time.sleep(5000)
            

        except Exception as ee: print(ee)      


if __name__ == '__main__':
	if not loginform:
		raise ValueError('LOGIN REQUIRED. PLEASE FIL THE LOGINS FILE!!!')	

	sessionData()
	time.sleep(30)
	print("LOGGED IN!")

	with open(f'{base}') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			try:
				if not spam:
					sendlike(checkuser(row[0]))
					with open(f'{base}-log.txt', 'a') as logerfile:logerfile.write(row[0]+'\n')
					
				else:break
			except Exception as err:
				exceptn = str(err)
				print(exceptn)
				print('---------------------------------------')
				continue
