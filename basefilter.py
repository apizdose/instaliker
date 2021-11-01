import csv
import random

base=input('your base: ') or 'base'
times=input('How many times filter base? (recomended more than 5): ') or '6'


print(f'\nFiltering {base}.csv.\n')
print('Working...')   


symarr=['_','.',]
for i in range(10):
    symarr.append(str(i))
   
arabiansym=[]
blacklist=[]
unique=[]


for n in range(0x600,0x6FF+1):
    c = chr(n)
   
    arabiansym.append(str(c))
    
for n in range(0x900,0x97F+1):
    c = chr(n)
    
    arabiansym.append(str(c))    

for n in range(0x400,0x4FF+1):
    c = chr(n)
    
    arabiansym.append(str(c))
    
for n in range(0x980,0x9FF+1):
    c = chr(n)
    
    arabiansym.append(str(c))    



with open("blacklist.txt", "r", encoding='utf-8') as file:
    global tname
    for i in file:
        tname = i.lower().replace("\n", "")
        if len(tname)>=5:
            blacklist.append(tname)
        if len(tname)<5 and len(tname)>3:
            for i in symarr:
                addname = tname+i
                nameadd = i+tname
                blacklist.append(addname)
                blacklist.append(nameadd)

print('\nPreparing blacklist...')
for i in set(blacklist):
    if blacklist.count(i) > 1:del blacklist[blacklist.index(i)]
 

with open(f'{base}.csv',mode='r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    global data
    data = list(reader)

def filter():        
    for name in data:
        nickname=name[0]
        full_name=name[1].lower()
        for i in blacklist:
            if i in nickname or i in full_name or 'raja' in nickname or 'raja' in full_name or 'rama' in nickname or 'rama' in full_name:
                try:data.remove(name)
                except:None

def arabfilter():
    for name in data:
        full_name=name[1].lower()        
        for i in arabiansym:
            if i in full_name:
                try:data.remove(name)
                except:continue


def writetobase():
    random.shuffle(data)
    with open(f'{base}_redacted.csv', mode='a',newline='',encoding='utf-8') as mkf:
        mkwriter = csv.writer(mkf)
        mkwriter.writerows(data)

def uniquedata(when):
    print(f'\nCreating unique list {when} filtering...')
    for i in data:
        if data.count(i) > 1:unique.append(i)
    with open(f'{base}_unique_{when}.csv', mode='a',newline='',encoding='utf-8') as mkf:
        mkwriter = csv.writer(mkf)
        mkwriter.writerows(unique)
        unique.clear()

uniquedata('before')

for i in range(50):
    arabfilter()
print('\nArabian symbols filtered')
print('\nStarting filtering by name (Can take a long time...)\n')
    
for i in range(int(times)):
    filter()
    print(f"Filtered {i+1}/{int(times)} cycles.")
    
writetobase()
uniquedata('after')
print(f'\nDone! Check {base}_redacted.csv')

