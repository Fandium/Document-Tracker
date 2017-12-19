#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 04:00:21 2017

@author: abbafanda
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:43:11 2017

@author: abbafanda
"""

import json
import matplotlib.pyplot as plt
import re
from collections import Counter
from tkinter import *

continents = { 'AF' : 'Africa', 'AS' : 'Asia', 'EU' : 'Europe', 'NA' : 'North America', 'SA' : 'South America', 'OC' : 'Oceania', 'AN' : 'Antarctica' }
cntry_to_cont = { 'AF' : 'AS', 'AX' : 'EU', 'AL' : 'EU', 'DZ' : 'AF', 'AS' : 'OC', 'AD' : 'EU', 'AO' : 'AF', 'AI' : 'NA', 'AQ' : 'AN', 'AG' : 'NA', 'AR' : 'SA', 'AM' : 'AS', 'AW' : 'NA', 'AU' : 'OC', 'AT' : 'EU', 'AZ' : 'AS', 'BS' : 'NA', 'BH' : 'AS', 'BD' : 'AS', 'BB' : 'NA', 'BY' : 'EU', 'BE' : 'EU', 'BZ' : 'NA', 'BJ' : 'AF', 'BM' : 'NA', 'BT' : 'AS', 'BO' : 'SA', 'BQ' : 'NA', 'BA' : 'EU', 'BW' : 'AF', 'BV' : 'AN', 'BR' : 'SA', 'IO' : 'AS', 'VG' : 'NA', 'BN' : 'AS', 'BG' : 'EU', 'BF' : 'AF', 'BI' : 'AF', 'KH' : 'AS', 'CM' : 'AF', 'CA' : 'NA', 'CV' : 'AF', 'KY' : 'NA', 'CF' : 'AF', 'TD' : 'AF', 'CL' : 'SA', 'CN' : 'AS', 'CX' : 'AS', 'CC' : 'AS', 'CO' : 'SA', 'KM' : 'AF', 'CD' : 'AF', 'CG' : 'AF', 'CK' : 'OC', 'CR' : 'NA', 'CI' : 'AF', 'HR' : 'EU', 'CU' : 'NA', 'CW' : 'NA', 'CY' : 'AS', 'CZ' : 'EU', 'DK' : 'EU', 'DJ' : 'AF', 'DM' : 'NA', 'DO' : 'NA', 'EC' : 'SA', 'EG' : 'AF', 'SV' : 'NA', 'GQ' : 'AF', 'ER' : 'AF', 'EE' : 'EU', 'ET' : 'AF', 'FO' : 'EU', 'FK' : 'SA', 'FJ' : 'OC', 'FI' : 'EU', 'FR' : 'EU', 'GF' : 'SA', 'PF' : 'OC', 'TF' : 'AN', 'GA' : 'AF', 'GM' : 'AF', 'GE' : 'AS', 'DE' : 'EU', 'GH' : 'AF', 'GI' : 'EU', 'GR' : 'EU', 'GL' : 'NA', 'GD' : 'NA', 'GP' : 'NA', 'GU' : 'OC', 'GT' : 'NA', 'GG' : 'EU', 'GN' : 'AF', 'GW' : 'AF', 'GY' : 'SA', 'HT' : 'NA', 'HM' : 'AN', 'VA' : 'EU', 'HN' : 'NA', 'HK' : 'AS', 'HU' : 'EU', 'IS' : 'EU', 'IN' : 'AS', 'ID' : 'AS', 'IR' : 'AS', 'IQ' : 'AS', 'IE' : 'EU', 'IM' : 'EU', 'IL' : 'AS', 'IT' : 'EU', 'JM' : 'NA', 'JP' : 'AS', 'JE' : 'EU', 'JO' : 'AS', 'KZ' : 'AS', 'KE' : 'AF', 'KI' : 'OC', 'KP' : 'AS', 'KR' : 'AS', 'KW' : 'AS', 'KG' : 'AS', 'LA' : 'AS', 'LV' : 'EU', 'LB' : 'AS', 'LS' : 'AF', 'LR' : 'AF', 'LY' : 'AF', 'LI' : 'EU', 'LT' : 'EU', 'LU' : 'EU', 'MO' : 'AS', 'MK' : 'EU', 'MG' : 'AF', 'MW' : 'AF', 'MY' : 'AS', 'MV' : 'AS', 'ML' : 'AF', 'MT' : 'EU', 'MH' : 'OC', 'MQ' : 'NA', 'MR' : 'AF', 'MU' : 'AF', 'YT' : 'AF', 'MX' : 'NA', 'FM' : 'OC', 'MD' : 'EU', 'MC' : 'EU', 'MN' : 'AS', 'ME' : 'EU', 'MS' : 'NA', 'MA' : 'AF', 'MZ' : 'AF', 'MM' : 'AS', 'NA' : 'AF', 'NR' : 'OC', 'NP' : 'AS', 'NL' : 'EU', 'NC' : 'OC', 'NZ' : 'OC', 'NI' : 'NA', 'NE' : 'AF', 'NG' : 'AF', 'NU' : 'OC', 'NF' : 'OC', 'MP' : 'OC', 'NO' : 'EU', 'OM' : 'AS', 'PK' : 'AS', 'PW' : 'OC', 'PS' : 'AS', 'PA' : 'NA', 'PG' : 'OC', 'PY' : 'SA', 'PE' : 'SA', 'PH' : 'AS', 'PN' : 'OC', 'PL' : 'EU', 'PT' : 'EU', 'PR' : 'NA', 'QA' : 'AS', 'RE' : 'AF', 'RO' : 'EU', 'RU' : 'EU', 'RW' : 'AF', 'BL' : 'NA', 'SH' : 'AF', 'KN' : 'NA', 'LC' : 'NA', 'MF' : 'NA', 'PM' : 'NA', 'VC' : 'NA', 'WS' : 'OC', 'SM' : 'EU', 'ST' : 'AF', 'SA' : 'AS', 'SN' : 'AF', 'RS' : 'EU', 'SC' : 'AF', 'SL' : 'AF', 'SG' : 'AS', 'SX' : 'NA', 'SK' : 'EU', 'SI' : 'EU', 'SB' : 'OC', 'SO' : 'AF', 'ZA' : 'AF', 'GS' : 'AN', 'SS' : 'AF', 'ES' : 'EU', 'LK' : 'AS', 'SD' : 'AF', 'SR' : 'SA', 'SJ' : 'EU', 'SZ' : 'AF', 'SE' : 'EU', 'CH' : 'EU', 'SY' : 'AS', 'TW' : 'AS', 'TJ' : 'AS', 'TZ' : 'AF', 'TH' : 'AS', 'TL' : 'AS', 'TG' : 'AF', 'TK' : 'OC', 'TO' : 'OC', 'TT' : 'NA', 'TN' : 'AF', 'TR' : 'AS', 'TM' : 'AS', 'TC' : 'NA', 'TV' : 'OC', 'UG' : 'AF', 'UA' : 'EU', 'AE' : 'AS', 'GB' : 'EU', 'US' : 'NA', 'UM' : 'OC', 'VI' : 'NA', 'UY' : 'SA', 'UZ' : 'AS', 'VU' : 'OC', 'VE' : 'SA', 'VN' : 'AS', 'WF' : 'OC', 'EH' : 'AF', 'YE' : 'AS', 'ZM' : 'AF', 'ZW' : 'AF' }

def Country (*args):
    file='cw2.json'
    ID=[]
    with open(file,"r") as f:
     for line in f:
        if (re.search(iCon.get(), line)):
            ID.append(line)
    country=[]
    lis={}
    for i in range(len(ID)):
     jID = [json.loads(str(item)) 
     for item in ID[i].strip().split('\n')]
     for item in jID:
      country.append(item['visitor_country'])
    lis = Counter(country)
    n = len(lis) 
    plt.barh(range(n), list(lis.values()), align='center', alpha=0.4)
    plt.yticks(range(n), list(lis.keys())) 
    plt.xlabel('count')
    plt.title('visitor country')
    plt.draw()
    plt.show()
    
def Continents(*args):
    file='cw2.json'
    ID=[]
    with open(file,"r") as f:
     for line in f:
        if (re.search(iCon.get(), line)):
            ID.append(line)
    country=[]
    for i in range(len(ID)):
     jID = [json.loads(str(item)) 
     for item in ID[i].strip().split('\n')]
     for item in jID:
      country.append(item['visitor_country'])
    cont=[]
    i=0
    for i in range(len(country)):
        n = country[i] 
        if n in cntry_to_cont:
          cont.append(cntry_to_cont[n])
          i+=0
    conti=[]
    a=0
    for a in range(len(cont)):
        m = cont[a] 
        if m in continents:
          conti.append(continents[m])
          a+=0
    lis2 = Counter(conti)
    b = len(lis2) 
    plt.barh(range(b), list(lis2.values()), align='center', alpha=0.4)
    plt.yticks(range(b), list(lis2.keys()))
    plt.xlabel('count')
    plt.title('visitor continents')
    plt.draw()
    plt.show()

      
def browser (*args):
    file='cw2.json'
    ID=[]
    with open(file,"r") as f:
     for line in f:
        if (re.search(iBr.get(), line)):
            ID.append(line)
    country=[]
    browserS=[]
    browser=[]
    lis3={}
    lis4={}
    for i in range(len(ID)):
     jID = [json.loads(str(item)) 
     for item in ID[i].strip().split('\n')]
     for item in jID:
      country.append(item['visitor_country'])
      browser.append(item['visitor_useragent'])
      text =item['visitor_useragent']
      m = re.search('(.+?)/', text)
      if m:
       browserS.append(m.group(1))
    lis3 = Counter(browser)
    n = len(lis3)
    plt.barh(range(n), list(lis3.values()), align='center', alpha=0.4)
    plt.yticks(range(n), list(lis3.keys()))
    plt.xlabel('count')
    plt.title('browser')
    plt.show()  
    lis4 = Counter(browserS)
    return lis4
    
def browser1(*args):
    file='cw2.json'
    ID=[]
    with open(file,"r") as f:
     for line in f:
        if (re.search(iBr.get(), line)):
            ID.append(line)
    country=[]
    browserS=[]
    browser=[]
    lis4={}
    for i in range(len(ID)):
     jID = [json.loads(str(item)) 
     for item in ID[i].strip().split('\n')]
     for item in jID:
      country.append(item['visitor_country'])
      browser.append(item['visitor_useragent'])
      text =item['visitor_useragent']
      m = re.search('(.+?)/', text)
      if m:
       browserS.append(m.group(1))  
    lis4 = Counter(browserS)
    n = len(lis4) 
    plt.barh(range(n), list(lis4.values()), align='center', alpha=0.4)
    plt.yticks(range(n), list(lis4.keys()))
    plt.xlabel('count')
    plt.title('browser')
    plt.show()
    

def documentUUID (s):
    file='cw2.json'
    ID2=[]
    with open(file,"r") as f:
      for line in f:
          if (re.search(s, line)):
              ID2.append(line) 
    visitors=[]
    for i in range(len(ID2)):
     jID2 = [json.loads(str(item)) 
     for item in ID2[i].strip().split('\n')]
     for item in jID2:
        visitors.append(item['visitor_uuid'])
    t=set(visitors)
    Dvisitors=list(t)
    return Dvisitors
    
     
def visitorUUID (s):     
    file='cw2.json'
    ID3=[]
    with open(file,"r") as f:
     for line in f:
        if (re.search(s, line)):
            ID3.append(line) 
    documents=[]
    for i in range(len(ID3)):
      jID3 = [json.loads(str(item)) 
      for item in ID3[i].strip().split('\n')]
      for item in jID3:
        documents.append(item['env_doc_id'])
    s=set(documents)
    Ddocuments=list(s)
    return Ddocuments
      
def alsoLike (s):
    a = documentUUID (s)
    alsolike=[]
    for item in a:
        b=[]
        b = visitorUUID (item)
        for item in b:
            alsolike.append(item)
    alsolike.sort()
    s=set(alsolike)
    t=list(s)
    return t
      
def PdocumentUUID():
    print("This document has been read by this user(s):")
    print(documentUUID(iDoc.get()))
    print ('\n')
    
def PvisitorUUID():
    print("This visitor has read this document(s):")
    print (visitorUUID(iVis.get()))
    print ('\n')
    
def Palsolike():
    print("Readers of this document also like this document(s):")
    print(alsoLike(iDoc.get()))
    print ('\n')

     
root = Tk()
root.geometry("600x120+200+200") 
root.title("Coursework 2")
Label(root, text="Enter Doc ID  :").grid(row=0)
Label(root, text="Enter Doc ID  :").grid(row=1)
Label(root, text="Enter Doc ID  :").grid(row=2)
Label(root, text="Enter User ID :").grid(row=3)
iBr = StringVar()
iCon = StringVar()
iDoc = StringVar()
iVis = StringVar()
iConEntry = Entry(root, textvariable=iCon).grid(row=0, column=1)
iBrEntry = Entry(root, textvariable=iBr).grid(row=1, column=1)
IDocEntry = Entry(root, textvariable=iDoc).grid(row=2, column=1)
IVisEntry = Entry(root, textvariable=iVis).grid(row=3, column=1)
Button(root, text="Get country graphs", command=Country).grid(row=0, column=2)
Button(root, text="Get continent graphs", command=Continents).grid(row=0, column=3)
Button(root, text="Get browser graphs", command=browser).grid(row=1, column=2)
Button(root, text="Get browser name graphs", command=browser1).grid(row=1, column=3)
Button(root, text="Get readers", command=PdocumentUUID).grid(row=2, column=2)
Button(root, text="Get also like", command=Palsolike).grid(row=2, column=3)
Button(root, text="Get documents read", command=PvisitorUUID).grid(row=3, column=2)
mainloop( )

