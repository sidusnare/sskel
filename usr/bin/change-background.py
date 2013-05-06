#!/usr/bin/python3
#
# change-background.py
#
# A script to print a random background image file name that hasnt been used in the last full cycle.
#


import os
import random
import mimetypes
import json

verbose = False

#Get list of done images
if os.path.exists(os.environ["HOME"] + '/usr/local/var/bg.json'):
	jr=open(os.environ["HOME"] + '/usr/local/var/bg.json')
	donelist=json.loads(jr.read())
else:
	donelist={}
	if verbose:
		print('Reseting done list')

choselist=list()

backgrounds = os.environ["HOME"] + "/Pictures/"


#Initalize randomization
try:
	random.seed(os.urandom(204800))
except:
	random.seed()


dirlist = os.listdir(backgrounds)
for x in dirlist:
	if verbose:
		print("\n\tEvaluating " + x)
	try:
		if donelist[x] == False:
			choselist.append(x)
			if verbose:
				print("Adding to chose list")
		else:
			if verbose:
				print("In done list, skipping")
	except:
		donelist[x] = False
		choselist.append(x)
		if verbose:
			print("Catching except")

if len(choselist) < 1:
	if verbose:
		print("Length of choselist is " + str(len(choselist)) + " resetting")
	choselist = os.listdir(backgrounds)
	del donelist
	donelist={}

item = random.randint (0, len (choselist) - 1)
image = choselist[item]
donelist[image] = True
jw = open(os.environ["HOME"] + '/usr/local/var/bg.json',"w")
jw.writelines(json.dumps(donelist, sort_keys=True, indent=4) + "\n" )
jw.close()
print( backgrounds + image)

