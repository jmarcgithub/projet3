#-*- coding: utf8 -*-
import os
from lab import *


lab01 = "_______________"
lab02 = "|            g|"
lab03 = "|  |    |     |"
lab04 = "|  |_o__|___  |"
lab05 = "|     | o |   |"
lab06 = "|_    |   |  _|"
lab07 = "|   __|__     |"
lab08 = "|  | o  |___  |"
lab09 = "| o|          |"
lab10 = "|__|_____|    |"
lab11 = "|    o|_____  |"
lab12 = "|  _| |       |"
lab13 = "| |___|o_|    |"
lab14 = "|      m      |"
lab15 = "|__|__________|"
compt = 0
answer = ""

look(lab01, lab02, lab03, lab04, lab05,\
 lab06, lab07, lab08, lab09, lab10, lab11,\
 lab12, lab13, lab14, lab15, compt)

labG = lab01 + lab02 + lab03 + lab04 + lab05 + lab06 + lab07 + lab08 + lab09 + lab10 + lab11 + lab12 + lab13 + lab14 + lab15

while labG.index("m")!= 28: #28 = place of the gardian
	answer = input() #incrément answer
	listing = list(labG) #make list
	upM = labG.index("m") - 15 #if moving up
	downM = labG.index("m") + 15 #if moving down
	rightM = labG.index("m") + 1 #if moving right
	leftM = labG.index("m") - 1 #if moving left
	
	

	if answer == "z" and listing[upM] != "_" and listing[upM] != "|":

		if listing[upM] == "o": # gift on the top
			compt += 1
			placeM = labG.index("m") - 15 #new place of "m"
			labG = labG.replace("m", " ") #wipe off "m" old place
			placeM = int(placeM)
			listing = list(labG) #make list
			listing[placeM] = "m" #new place of "m" in list
			labG = "".join(listing) #make chain
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
 lab06, lab07, lab08, lab09, lab10, lab11,\
 lab12, lab13, lab14, lab15, compt)
		else:
			placeM = labG.index("m") - 15
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
	 lab06, lab07, lab08, lab09, lab10, lab11,\
	 lab12, lab13, lab14, lab15, compt)
			

	if answer == "s" and listing[downM] != "_" and listing[downM] != "|":
		if listing[downM] == "o":
			compt += 1
			placeM = labG.index("m") + 15
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
 lab06, lab07, lab08, lab09, lab10, lab11,\
 lab12, lab13, lab14, lab15, compt)
		else:
			placeM = labG.index("m") + 15
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
	 lab06, lab07, lab08, lab09, lab10, lab11,\
	 lab12, lab13, lab14, lab15, compt)
		

	if answer == "d" and listing[rightM] != "_" and listing[rightM] != "|":
		if listing[rightM] == "o":
			compt += 1
			placeM = labG.index("m") + 1
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
 lab06, lab07, lab08, lab09, lab10, lab11,\
 lab12, lab13, lab14, lab15, compt)
		else:
			placeM = labG.index("m") + 1
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
	 lab06, lab07, lab08, lab09, lab10, lab11,\
	 lab12, lab13, lab14, lab15, compt)


	if answer == "q" and listing[leftM] != "_" and listing[leftM] != "|":
		if listing[leftM] == "o":
			compt += 1
			placeM = labG.index("m") - 1
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
 lab06, lab07, lab08, lab09, lab10, lab11,\
 lab12, lab13, lab14, lab15, compt)
		else:
			placeM = labG.index("m") - 1
			labG = labG.replace("m", " ")
			placeM = int(placeM)
			listing = list(labG)
			listing[placeM] = "m"
			labG = "".join(listing)
			lab01 = labG[0:15]
			lab02 = labG[15:30]
			lab03 = labG[30:45]
			lab04 = labG[45:60]
			lab05 = labG[60:75]
			lab06 = labG[75:90]
			lab07 = labG[90:105]
			lab08 = labG[105:120]
			lab09 = labG[120:135]
			lab10 = labG[135:150]
			lab11 = labG[150:165]
			lab12 = labG[165:180]
			lab13 = labG[180:195]
			lab14 = labG[195:210]
			lab15 = labG[210:225]
			look(lab01, lab02, lab03, lab04, lab05,\
	 lab06, lab07, lab08, lab09, lab10, lab11,\
	 lab12, lab13, lab14, lab15, compt)
		
if compt == 6:
	print("§§§ VOUS AVEZ REUSSI ! §§§")
else:
	print("§§§ VOUS ETES MORT §§§")

		
os.system("pause")