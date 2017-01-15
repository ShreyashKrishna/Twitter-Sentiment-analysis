import sys
import os
import numpy as np
import re
f1=open("d.txt","r")#now read every line?
data=[]
ctr=0
ctr1=0
for line in f1:
        line=line.lower()
        data=line.split(',',3)        
        if(data[1]=='0'):
            st='negative'
            ctr=ctr+1
            st=st+str(ctr)+".txt"
            fo = open("C:\\Python34\\Sentiment\\negative\\"+st, "a")
            #print(data[3])
            #print(re.sub('^[a-zA-Z0-9()_+=\{}|\\,;.?:-]+', ' ',data[3]))
            fo.write(re.sub('^[a-zA-Z0-9()_+=\{}|\\,;.?:-]+', ' ',data[3]))
            fo.close()
        if(data[1]=='1'):
            st1='positive'
            ctr1=ctr1+1
            st1=st1+str(ctr1)+".txt"
            #print(data[3])
            f2=open("C:\\Python34\\Sentiment\\positive\\"+st1,"a")
            f2.write(re.sub('^[a-zA-Z0-9()_+=\{}|\\,;.?:-]+', ' ',data[3]))
            f2.close()
f1.close()

