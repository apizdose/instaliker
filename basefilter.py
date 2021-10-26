import csv
import random

base=input('your base: ') or 'base'
   
name=''
name=name+'\n'.lower()
capcase = name.capitalize() 
lowcase = name.lower()

symarr=['_','.',]
for i in range(10):
    symarr.append(str(i))
   

blacklist=[]
nolist=[]
mybase=[]




with open("blacklist.txt", "r", encoding='utf-8') as file:
    global tname
    for i in file:
        tname = i.lower().replace("\n", "")
        if len(tname)>=5:
            blacklist.append(tname)
        if len(tname)<5:
            for i in symarr:
                addname = tname+i
                nameadd = i+tname
                blacklist.append(addname)
                blacklist.append(nameadd)
                
        

with open(f'{base}.csv') as csvfile:
    reader = csv.reader(csvfile)
    for name in reader:
        mybase.append(name[0])

for name in mybase:
    name=name.lower()
    for i in blacklist:
              
            if i in name:
               nolist.append(name)
    

for i in nolist:
    try:mybase.remove(i)
    except:continue

for i in mybase:
    if 'raja' in i or 'rama' in i:
        mybase.remove(i)
        
random.shuffle(mybase)
with open(f'{base}_redacted.csv', mode='a',newline='') as mkf:
    mkwriter = csv.writer(mkf)
    for i in mybase:
        mkwriter.writerow([i.replace("\n", "")])


  
