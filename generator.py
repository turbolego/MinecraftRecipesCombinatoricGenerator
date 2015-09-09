#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from itertools import combinations_with_replacement

i = 0;


alphabets = ['260', '391', '280', '366', '350', '349', '424', '111', '320', '40']

id1 = 260; #eple
id2 = 391; #gulerot
id3 = 280; #ost
id4 = 366; #kylling
id5 = 350; #ansjos
id6 = 349; #laks
id7 = 424; #lam
id8 = 111; #spinat
id9 = 320; #gris
id10 = 40; #tomat

#Eple = 260
EpleCal = 91;
EpleCarbo = 23;
EpleFat = 1;
EpleProtein = 0;
EpleFiber = 4;
EpleSukker = 19;
EpleCvita = 1;
EpleAvita = 2;
EpleKalsium = 1;
EpleJern = 2;
EpleSalt = 2;

#Gulerot = 391
GulrotCal = 27;
GulrotCarbo = 6;
GulrotFat = 0;
GulrotProtein = 1;
GulrotFiber = 2;
GulrotSukker = 3;
GulrotCvita = 5;
GulrotAvita =  266;
GulrotKalsium = 2;
GulrotJern = 1;
GulrotSalt=45;

#Ost (stick) = 280
OstCal = 403;
OstCarbo = 1;
OstFat = 33;
OstProtein = 25;
OstFiber = 0;
OstSukker = 1;
OstCvita = 0;
OstAvita =  20;
OstKalsium = 72;
OstJern = 4;
OstSalt = 621;

#kylling = 366
KyllingCal = 300;
KyllingCarbo = 0;
KyllingFat = 21;
KyllingProtein = 26;
KyllingFiber = 0;
KyllingSukker = 0;
KyllingCvita = 0;
KyllingAvita =  7;
KyllingKalsium = 2;
KyllingJern = 8;
KyllingSalt = 87;

#Ansjos = 350
AnsjosCal = 42;
AnsjosCarbo = 0;
AnsjosFat = 2;
AnsjosProtein = 6;
AnsjosFiber = 0;
AnsjosSukker = 0;
AnsjosCvita = 0;
AnsjosAvita =  0;
AnsjosKalsium = 5;
AnsjosJern = 5;
AnsjosSalt= 733;

#Laks = 349
LaksCal = 280;
LaksCarbo = 0;
LaksFat = 13;
LaksProtein = 39;
LaksFiber = 0;
LaksSukker = 0;
LaksCvita = 0;
LaksAvita =  1;
LaksKalsium = 2;
LaksJern = 9;
LaksSalt = 86;

#Lam = 424
LamCal = 297;
LamCarbo = 0;
LamFat =  9;
LamProtein = 49;
LamFiber = 0;
LamSukker = 0;
LamCvita = 0;
LamAvita =  0;
LamKalsium = 3;
LamJern = 19;
LamSalt = 180;

#Spinat = 111
SpinatCal = 8;
SpinatCarbo = 1;
SpinatFat = 0;
SpinatProtein = 1;
SpinatFiber = 1;
SpinatSukker = 1;
SpinatCvita = 28;
SpinatAvita =  49;
SpinatKalsium = 3;
SpinatJern = 2;
SpinatSalt =73;

#Gris = 320
PorkCal = 249;
PorkCarbo = 0;
PorkFat = 13;
PorkProtein = 32;
PorkFiber = 0;
PorkSukker = 0;
PorkCvita = 0;
PorkAvita =  0;
PorkKalsium = 1;
PorkJern = 10;
PorkSalt = 2100;

#Tomat = 40
TomatCal = 111;
TomatCarbo = 18;
TomatFat = 3;
TomatProtein = 2;
TomatFiber = 3;
TomatSukker = 11;
TomatCvita = 4;
TomatAvita =  19;
TomatKalsium = 3;
TomatJern = 5;
TomatSalt = 525;




fo = open("recipes/recipes.txt", "a")
fo.write('Recipes:\n');

fo2 = open("test/RegisteredItems.txt", "a")
fo2.write('RegisteredItems:\n');

fo3 = open("test/items.txt", "a")
fo3.write('Items:\n');


for (a,b,c,d,e,f) in combinations_with_replacement(alphabets, 6):
	fo = open("recipes/recipes.txt", "a")
	s = str(i)
	fo.write('  Pizza'+s+':\n'+'    \'1\': '+a+'\n'+'    \'2\': '+b+'\n'+'    \'3\': '+c+'\n'+'    \'4\': '+d+'\n'+'    \'5\': '+e+'\n'+'    \'6\': '+f+'\n'+'    \'7\': '+'296'+'\n'+'    \'8\': '+'296'+'\n'+'    \'9\': '+'296'+'\n');
	print (s + ':' + a + ' '+ b + ' '+ c + ' '+ d + ' '+ e + ' '+ f);

	slot1 = str(a)
	slot2 = str(b)
	slot3 = str(c)
	slot4 = str(d)
	slot5 = str(e)
	slot6 = str(f)
	
	eple = str(id1)
	carrot = str(id2)
	ost = str(id3)
	kylling = str(id4)
	ansjos = str(id5)
	laks = str(id6)
	lam = str(id7)
	spinat = str(id8)
	gris = str(id9)
	tomat = str(id10)

	#Startverdi er pizzadeig totalen lol
	Cal = 1956;
	Karbo = 364;
	Fat = 32;
	Protein = 84;
	Fiber = 65;
	Sukker = 8;
	Cvita = 54;
	Avita = 122;
	Kalsium = 3;
	Jern = 0;
	Salt = 2809;
	
	total1 = str(Cal)
	total2 = str(Karbo)
	total3 = str(Protein)
	total4 = str(Fiber)
	total5 = str(Sukker)
	total6 = str(Cvita)
	total7 = str(Avita)
	total8 = str(Kalsium)
	total9 = str(Jern)
	total10 = str(Salt)

#######SLOT1
	
	if (eple == slot1):
		Cal += 91; #eple
		Karbo += 23;
		Fat += 1;
		Protein += 0;
		Fiber += 4;
		Sukker += 19;
		Cvita += 1;
		Avita += 2;
		Kalsium += 1;
		Jern += 2;
		Salt += 2;
	if (carrot == slot1):
		Cal += 27; #carrot
		Karbo += 6;
		Fat += 0;
		Protein += 1;
		Fiber += 2;
		Sukker += 3;
		Cvita += 5;
		Avita +=  266;
		Kalsium += 2;
		Jern += 1;
		Salt+=45;
	if (ost == slot1):
		Cal += 403; #ost
		Karbo += 1;
		Fat += 33;
		Protein += 25;
		Fiber += 0;
		Sukker += 1;
		Cvita += 0;
		Avita +=  20;
		Kalsium += 72;
		Jern += 4;
		Salt += 621;
	if (kylling == slot1):
		Cal += 300; #kylling
		Karbo += 0;
		Fat += 21;
		Protein += 26;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  7;
		Kalsium += 2;
		Jern += 8;
		Salt += 87;
	if (ansjos == slot1):
		Cal += 42; #ansjos
		Karbo += 0;
		Fat += 2;
		Protein += 6;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 5;
		Jern += 5;
		Salt+= 733;
	if (laks == slot1):
		Cal += 280; #laks
		Karbo += 0;
		Fat += 13;
		Protein += 39;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  1;
		Kalsium += 2;
		Jern += 9;
		Salt += 86;
	if (lam == slot1):
		Cal += 297; #lam
		Karbo += 0;
		Fat +=  9;
		Protein += 49;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 3;
		Jern += 19;
		Salt += 180;
	if (spinat == slot1):
		Cal += 8; #spinat
		Karbo += 1;
		Fat += 0;
		Protein += 1;
		Fiber += 1;
		Sukker += 1;
		Cvita += 28;
		Avita +=  49;
		Kalsium += 3;
		Jern += 2;
		Salt +=73;
	if (gris == slot1):
		Cal += 249; #gris
		Karbo += 0;
		Fat += 13;
		Protein += 32;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 1;
		Jern += 10;
		Salt += 2100;
	if (tomat == slot1):
		Cal += 111; #tomat
		Karbo += 18
		Fat += 3
		Protein += 2
		Fiber += 3
		Sukker += 11
		Cvita += 4
		Avita +=  19
		Kalsium += 3
		Jern += 5
		Salt += 525		

#######SLOT2


	if (eple == slot2):
		Cal += 91; #eple
		Karbo += 23;
		Fat += 1;
		Protein += 0;
		Fiber += 4;
		Sukker += 19;
		Cvita += 1;
		Avita += 2;
		Kalsium += 1;
		Jern += 2;
		Salt += 2;
	if (carrot == slot2):
		Cal += 27; #carrot
		Karbo += 6;
		Fat += 0;
		Protein += 1;
		Fiber += 2;
		Sukker += 3;
		Cvita += 5;
		Avita +=  266;
		Kalsium += 2;
		Jern += 1;
		Salt+=45;
	if (ost == slot2):
		Cal += 403; #ost
		Karbo += 1;
		Fat += 33;
		Protein += 25;
		Fiber += 0;
		Sukker += 1;
		Cvita += 0;
		Avita +=  20;
		Kalsium += 72;
		Jern += 4;
		Salt += 621;
	if (kylling == slot2):
		Cal += 300; #kylling
		Karbo += 0;
		Fat += 21;
		Protein += 26;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  7;
		Kalsium += 2;
		Jern += 8;
		Salt += 87;
	if (ansjos == slot2):
		Cal += 42; #ansjos
		Karbo += 0;
		Fat += 2;
		Protein += 6;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 5;
		Jern += 5;
		Salt+= 733;
	if (laks == slot2):
		Cal += 280; #laks
		Karbo += 0;
		Fat += 13;
		Protein += 39;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  1;
		Kalsium += 2;
		Jern += 9;
		Salt += 86;
	if (lam == slot2):
		Cal += 297; #lam
		Karbo += 0;
		Fat +=  9;
		Protein += 49;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 3;
		Jern += 19;
		Salt += 180;
	if (spinat == slot2):
		Cal += 8; #spinat
		Karbo += 1;
		Fat += 0;
		Protein += 1;
		Fiber += 1;
		Sukker += 1;
		Cvita += 28;
		Avita +=  49;
		Kalsium += 3;
		Jern += 2;
		Salt +=73;
	if (gris == slot2):
		Cal += 249; #gris
		Karbo += 0;
		Fat += 13;
		Protein += 32;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 1;
		Jern += 10;
		Salt += 2100;
	if (tomat == slot2):
		Cal += 111; #tomat
		Karbo += 18
		Fat += 3
		Protein += 2
		Fiber += 3
		Sukker += 11
		Cvita += 4
		Avita +=  19
		Kalsium += 3
		Jern += 5
		Salt += 525		

#######SLOT3


	if (eple == slot3):
		Cal += 91; #eple
		Karbo += 23;
		Fat += 1;
		Protein += 0;
		Fiber += 4;
		Sukker += 19;
		Cvita += 1;
		Avita += 2;
		Kalsium += 1;
		Jern += 2;
		Salt += 2;
	if (carrot == slot3):
		Cal += 27; #carrot
		Karbo += 6;
		Fat += 0;
		Protein += 1;
		Fiber += 2;
		Sukker += 3;
		Cvita += 5;
		Avita +=  266;
		Kalsium += 2;
		Jern += 1;
		Salt+=45;
	if (ost == slot3):
		Cal += 403; #ost
		Karbo += 1;
		Fat += 33;
		Protein += 25;
		Fiber += 0;
		Sukker += 1;
		Cvita += 0;
		Avita +=  20;
		Kalsium += 72;
		Jern += 4;
		Salt += 621;
	if (kylling == slot3):
		Cal += 300; #kylling
		Karbo += 0;
		Fat += 21;
		Protein += 26;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  7;
		Kalsium += 2;
		Jern += 8;
		Salt += 87;
	if (ansjos == slot3):
		Cal += 42; #ansjos
		Karbo += 0;
		Fat += 2;
		Protein += 6;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 5;
		Jern += 5;
		Salt+= 733;
	if (laks == slot3):
		Cal += 280; #laks
		Karbo += 0;
		Fat += 13;
		Protein += 39;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  1;
		Kalsium += 2;
		Jern += 9;
		Salt += 86;
	if (lam == slot3):
		Cal += 297; #lam
		Karbo += 0;
		Fat +=  9;
		Protein += 49;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 3;
		Jern += 19;
		Salt += 180;
	if (spinat == slot3):
		Cal += 8; #spinat
		Karbo += 1;
		Fat += 0;
		Protein += 1;
		Fiber += 1;
		Sukker += 1;
		Cvita += 28;
		Avita +=  49;
		Kalsium += 3;
		Jern += 2;
		Salt +=73;
	if (gris == slot3):
		Cal += 249; #gris
		Karbo += 0;
		Fat += 13;
		Protein += 32;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 1;
		Jern += 10;
		Salt += 2100;
	if (tomat == slot3):
		Cal += 111; #tomat
		Karbo += 18
		Fat += 3
		Protein += 2
		Fiber += 3
		Sukker += 11
		Cvita += 4
		Avita +=  19
		Kalsium += 3
		Jern += 5
		Salt += 525		

#######SLOT4


	if (eple == slot4):
		Cal += 91; #eple
		Karbo += 23;
		Fat += 1;
		Protein += 0;
		Fiber += 4;
		Sukker += 19;
		Cvita += 1;
		Avita += 2;
		Kalsium += 1;
		Jern += 2;
		Salt += 2;
	if (carrot == slot4):
		Cal += 27; #carrot
		Karbo += 6;
		Fat += 0;
		Protein += 1;
		Fiber += 2;
		Sukker += 3;
		Cvita += 5;
		Avita +=  266;
		Kalsium += 2;
		Jern += 1;
		Salt+=45;
	if (ost == slot4):
		Cal += 403; #ost
		Karbo += 1;
		Fat += 33;
		Protein += 25;
		Fiber += 0;
		Sukker += 1;
		Cvita += 0;
		Avita +=  20;
		Kalsium += 72;
		Jern += 4;
		Salt += 621;
	if (kylling == slot4):
		Cal += 300; #kylling
		Karbo += 0;
		Fat += 21;
		Protein += 26;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  7;
		Kalsium += 2;
		Jern += 8;
		Salt += 87;
	if (ansjos == slot4):
		Cal += 42; #ansjos
		Karbo += 0;
		Fat += 2;
		Protein += 6;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 5;
		Jern += 5;
		Salt+= 733;
	if (laks == slot4):
		Cal += 280; #laks
		Karbo += 0;
		Fat += 13;
		Protein += 39;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  1;
		Kalsium += 2;
		Jern += 9;
		Salt += 86;
	if (lam == slot4):
		Cal += 297; #lam
		Karbo += 0;
		Fat +=  9;
		Protein += 49;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 3;
		Jern += 19;
		Salt += 180;
	if (spinat == slot4):
		Cal += 8; #spinat
		Karbo += 1;
		Fat += 0;
		Protein += 1;
		Fiber += 1;
		Sukker += 1;
		Cvita += 28;
		Avita +=  49;
		Kalsium += 3;
		Jern += 2;
		Salt +=73;
	if (gris == slot4):
		Cal += 249; #gris
		Karbo += 0;
		Fat += 13;
		Protein += 32;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 1;
		Jern += 10;
		Salt += 2100;
	if (tomat == slot4):
		Cal += 111; #tomat
		Karbo += 18
		Fat += 3
		Protein += 2
		Fiber += 3
		Sukker += 11
		Cvita += 4
		Avita +=  19
		Kalsium += 3
		Jern += 5
		Salt += 525		

#######SLOT5


	if (eple == slot5):
		Cal += 91; #eple
		Karbo += 23;
		Fat += 1;
		Protein += 0;
		Fiber += 4;
		Sukker += 19;
		Cvita += 1;
		Avita += 2;
		Kalsium += 1;
		Jern += 2;
		Salt += 2;
	if (carrot == slot5):
		Cal += 27; #carrot
		Karbo += 6;
		Fat += 0;
		Protein += 1;
		Fiber += 2;
		Sukker += 3;
		Cvita += 5;
		Avita +=  266;
		Kalsium += 2;
		Jern += 1;
		Salt+=45;
	if (ost == slot5):
		Cal += 403; #ost
		Karbo += 1;
		Fat += 33;
		Protein += 25;
		Fiber += 0;
		Sukker += 1;
		Cvita += 0;
		Avita +=  20;
		Kalsium += 72;
		Jern += 4;
		Salt += 621;
	if (kylling == slot5):
		Cal += 300; #kylling
		Karbo += 0;
		Fat += 21;
		Protein += 26;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  7;
		Kalsium += 2;
		Jern += 8;
		Salt += 87;
	if (ansjos == slot5):
		Cal += 42; #ansjos
		Karbo += 0;
		Fat += 2;
		Protein += 6;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 5;
		Jern += 5;
		Salt+= 733;
	if (laks == slot5):
		Cal += 280; #laks
		Karbo += 0;
		Fat += 13;
		Protein += 39;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  1;
		Kalsium += 2;
		Jern += 9;
		Salt += 86;
	if (lam == slot5):
		Cal += 297; #lam
		Karbo += 0;
		Fat +=  9;
		Protein += 49;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 3;
		Jern += 19;
		Salt += 180;
	if (spinat == slot5):
		Cal += 8; #spinat
		Karbo += 1;
		Fat += 0;
		Protein += 1;
		Fiber += 1;
		Sukker += 1;
		Cvita += 28;
		Avita +=  49;
		Kalsium += 3;
		Jern += 2;
		Salt +=73;
	if (gris == slot5):
		Cal += 249; #gris
		Karbo += 0;
		Fat += 13;
		Protein += 32;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 1;
		Jern += 10;
		Salt += 2100;
	if (tomat == slot5):
		Cal += 111; #tomat
		Karbo += 18
		Fat += 3
		Protein += 2
		Fiber += 3
		Sukker += 11
		Cvita += 4
		Avita +=  19
		Kalsium += 3
		Jern += 5
		Salt += 525		

#######SLOT6


	if (eple == slot6):
		Cal += 91; #eple
		Karbo += 23;
		Fat += 1;
		Protein += 0;
		Fiber += 4;
		Sukker += 19;
		Cvita += 1;
		Avita += 2;
		Kalsium += 1;
		Jern += 2;
		Salt += 2;
	if (carrot == slot6):
		Cal += 27; #carrot
		Karbo += 6;
		Fat += 0;
		Protein += 1;
		Fiber += 2;
		Sukker += 3;
		Cvita += 5;
		Avita +=  266;
		Kalsium += 2;
		Jern += 1;
		Salt+=45;
	if (ost == slot6):
		Cal += 403; #ost
		Karbo += 1;
		Fat += 33;
		Protein += 25;
		Fiber += 0;
		Sukker += 1;
		Cvita += 0;
		Avita +=  20;
		Kalsium += 72;
		Jern += 4;
		Salt += 621;
	if (kylling == slot6):
		Cal += 300; #kylling
		Karbo += 0;
		Fat += 21;
		Protein += 26;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  7;
		Kalsium += 2;
		Jern += 8;
		Salt += 87;
	if (ansjos == slot6):
		Cal += 42; #ansjos
		Karbo += 0;
		Fat += 2;
		Protein += 6;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 5;
		Jern += 5;
		Salt+= 733;
	if (laks == slot6):
		Cal += 280; #laks
		Karbo += 0;
		Fat += 13;
		Protein += 39;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  1;
		Kalsium += 2;
		Jern += 9;
		Salt += 86;
	if (lam == slot6):
		Cal += 297; #lam
		Karbo += 0;
		Fat +=  9;
		Protein += 49;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 3;
		Jern += 19;
		Salt += 180;
	if (spinat == slot6):
		Cal += 8; #spinat
		Karbo += 1;
		Fat += 0;
		Protein += 1;
		Fiber += 1;
		Sukker += 1;
		Cvita += 28;
		Avita +=  49;
		Kalsium += 3;
		Jern += 2;
		Salt +=73;
	if (gris == slot6):
		Cal += 249; #gris
		Karbo += 0;
		Fat += 13;
		Protein += 32;
		Fiber += 0;
		Sukker += 0;
		Cvita += 0;
		Avita +=  0;
		Kalsium += 1;
		Jern += 10;
		Salt += 2100;
	if (tomat == slot6):
		Cal += 111; #tomat
		Karbo += 18
		Fat += 3
		Protein += 2
		Fiber += 3
		Sukker += 11
		Cvita += 4
		Avita +=  19
		Kalsium += 3
		Jern += 5
		Salt += 525		


	CalSTR = str(Cal)
	KarboSTR = str(Karbo)
	FatSTR = str(Fat)
	ProteinSTR = str(Protein)
	FiberSTR = str(Fiber)
	SukkerSTR = str(Sukker)
	CvitaSTR = str(Cvita)
	AvitaSTR = str(Avita)
	KalsiumSTR = str(Kalsium)
	JernSTR = str(Jern)
	SaltSTR = str(Salt)
	
	
	print (s);

	fo2 = open("test/RegisteredItems.txt", "a")
	fo2.write('- Pizza'+s+'\n');
	
	fo3 = open("test/Items.txt", "a")
	fo3.write('  Pizza'+s+':\n'+'    ID: 281\n'+'    DisplayName: Pizza'+s+'\n'+'    UsePermission: false\n'+'    Abilities:\n'+'    - Teleport\n'+'    Lore:\n');

	
	
	fo3.write('    - '+CalSTR+' kcal kalorier\n');
	fo3.write('    - '+FatSTR+' gram fett\n');
	fo3.write('    - '+ProteinSTR+' gram proteiner\n');
	fo3.write('    - '+KarboSTR+' gram karbohydrater\n');
	fo3.write('    - '+FiberSTR+' gram fiber\n');
	fo3.write('    - '+SukkerSTR+' gram sukker\n');
	fo3.write('    - '+SaltSTR+' milligram salt\n');
	fo3.write('    - '+CvitaSTR+' prosent c vitaminer\n');
	fo3.write('    - '+AvitaSTR+' prosent a vitaminer\n');
	fo3.write('    - '+KalsiumSTR+' prosent kalsium\n');
	fo3.write('    - '+JernSTR+' prosent jern\n');

	
	fo3.write('    Color: §a\n'+'    UseRecipe: true\n'+'    UseCustom: true\n');
	i += 1;
	fo.close()
	fo2.close()
	fo3.close()

#Displays a ASCII-art pizza in the terminal when done.

print '             ..'
print '           .....'
print '         .......=]'
print '        .....==[~==.'
print '       .....======..='
print '      ....===O=~~=....~'
print '     ....=.===={#==~====.'
print '    .....=[.==)=======.===='
print '   .....==.(]====~===.==(==='
print '   ....====)==.#..=[=~&==(=.=.'
print '  .....~.=.=======.&#======.=.=='
print '  ....=====~@=.=$========~O===R==~'
print '  ....~=====]==.~====.===!====.===='
print '  ....===.H=.=.==.~.=..H=~===~==H=~~='
print '  ....$=.=[.====~===~RO=H==.~=====~===.'
print '  .....=={=={==.=.========.]=.~.=$.===~.'
