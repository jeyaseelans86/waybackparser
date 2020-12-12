import sys
import requests
from pathlib import Path



u=sys.argv[1]


r=requests.get('http://web.archive.org/cdx/search/cdx?url=%s*&output=json&collapse=urlkey'%u)
rjson=r.json()

urls=[]
for i in range(1,len(rjson)):
    url=rjson[i][2]
    urls.append(url)
    sorted(set(urls))
#print(*urls,sep='\n')


extensions=[".asp",".aspx",".cer",".js",".cfm",".cfml",".rb",".php",".php3",".php4",".php5",".jsp",".json",".apk",".ods",".xls",".xlsm",".xlsx",".bak",".cab",".cpl",".dmp",".drv",".tmp",".sys",".doc",".docx",".pdf",".txt",".wpd",".bat",".bin",".cgi",".pl",".py",".exe",".gadget",".jar",".msi",".wsf",".csv",".dat",".db",".dbf",".log",".mdb",".sav",".sql",".tar",".xml",".7z",".arj",".deb",".pkg",".rar",".rpm",".tar.gz",".z",".zip",".bin",".dmg",".iso",".toast",".vcd",".email",".eml",".emlx",".msg",".oft",".ost",".pst",".vcf",".shtm",".shtml",".phtm",".phtml",".jhtml",".conf",".yml",".config",".yaml",".wsdl",".java",".key",".html",".sh"]
withext=[]
for i in range(len(urls)):
    u=urls[i]
    file_ext = Path(u).suffix
    if file_ext != None:
        withext.append(u)
for j in range(len(extensions)):
    print("The URLS with Extension %s"%extensions[j])
    for k in range(len(withext)):
        fileext=Path(withext[k]).suffix
        if extensions[j] == fileext:
            print(withext[k])
