import requests as r
import sys,json
domain=sys.argv[1]
resp=r.get('https://crt.sh/?q=%s&output=json'% domain)
rjson=resp.json()
sublist=[]
for i in range(len(rjson)):
    subs=rjson[i]["name_value"]
    if subs not in sublist:
        sublist.append(subs)
print(*sublist,sep='\n')
