'''

Bot for PR War, long live Hatillo Cows

'''
import math
import random
from PIL import Image, ImageDraw

#Radius of Ze Earth
Radius = 6371000

#Time and Record Keeping
Turn = 1

#Pueblo Data
#			 Name, 				Pop, 	Sq Km, 	Lat, 	  Long       Image Coords
Data_Set = [["Adjuntas", 		19483, 	172.73, 18.16379, -66.72369, (728,520)],
			["Aguada", 			41959, 	79.90, 	18.37939, -67.18824, (180,270)],
			["Aguadilla", 		60949, 	94.61, 	18.42745, -67.15407, (260,124)],
			["Aguas Buenas", 	28659, 	77.92, 	18.2569, -66.10294, (1564,438)],
			["Aibonito", 		25900, 	81.10, 	18.13996, -66.266, (1374,588)],
			["Añasco", 			29261, 	101.75, 18.28273, -67.13962, (286,368)],
			["Arecibo", 		96440, 	326.20, 18.47245, -66.71573, (847,181)],
			["Arroyo", 			19575, 	38.87,  17.9658, -66.06128, (1661,764)],
			["Barceloneta", 	24816, 	48.41,	18.4505, -66.53851, (984,159)],
			["Barranquitas", 	30318, 	88.71,	18.18662, -66.30628, (1292,489)],
			["Bayamón", 		208116, 114.80,18.39856, -66.15572, (1485,269)],
			["Cabo Rojo", 		50917, 	182.27,18.08663, -67.14573, (198,698)],
			["Caguas", 			142893, 151.77,18.23412, -66.0485, (1655,495)],
			["Camuy",			35159, 	120.06,18.48383, -66.8449, (572,176)],
			["Canóvanas",		47648, 	85.12,18.3751, -65.89934, (1875,308)],
			["Carolina",		176762, 117.38,18.38078, -65.95739, (1782,258)],
			["Cataño",			28140, 	12.55,18.44134, -66.11822, (1534, 170)],
			["Cayey",			48119, 	134.51,18.11191, -66.166, (1496,632)],
			["Ceiba",			13631, 	75.20, 18.26412, -65.6485, (2178,418)],
			["Ciales",			18782, 	172.31, 18.33606, -66.46878, (1039,352)],
			["Cidra",			43480, 	93.29, 18.17579, -66.16128, (1512,517)],
			["Coamo",			40512, 	202.27, 18.07996, -66.35795, (1237,627)],
			["Comerío",			20778, 	73.56, 18.21801, -66.226, (1424,467)],
			["Corozal",			37142, 	110.26, 18.34106, -66.31684, (1303,357)],
			["Culebra",			1818, 	30.10, 18.30301, -65.30099, (2189,902)],
			["Dorado",			38165, 	59.80, 18.45883, -66.26767, (1347,165)],
			["Fajardo",			36993, 	77.34, 18.32579, -65.65238, (2172,330)],
			["Florida",			12680, 	39.39, 18.36245, -66.56128, (973,264)],
			["Guánica",			19427, 	95.96, 17.97163, -66.90795, (506,775)],
			["Guayama",			45362, 	168.32, 17.98413, -66.11378, (1551,781)],
			["Guayanilla",		21581, 	109.48, 18.01913, -66.79184, (671,709)],
			["Guaynabo",		97924, 	71.43, 18.35745, -66.111, (1562,297)],
			["Gurabo",			45369, 	72.23, 18.2544, -65.97294, (1738,401)],
			["Hatillo",			41953, 	108.21, 18.48633, -66.82545, (665,170)],
			["Hormigueros",		17250, 	29.37, 18.13968, -67.1274, (258,583)],
			["Humacao",			58466, 	115.90, 18.14968, -65.82738, (1991,561)],
			["Isabela",			45631, 	143.23, 18.50078, -67.02435, (390,159)],
			["Jayuya",			16642, 	115.33, 18.21857, -66.59156, (946,467)],
			["Juana Díaz",		79897, 	156.12, 18.05246, -66.50656, (1083,709)],
			["Juncos",			40290, 	68.61, 18.22746, -65.921, (1853,456)],
			["Lajas",			25753, 	159.15, 18.04996, -67.05934, (368,764)],
			["Lares",			30753, 	159.15, 18.29467, -66.87712, (577,385)],
			["Las Marías",		9881, 	120.07, 18.2519, -66.99212, (429,440)],
			["Las Piedras",		38675, 	87.75, 18.18301, -65.86627, (1897,511)],
			["Loíza",			30060, 	50.17, 18.43134, -65.88016, (1853,187)],
			["Luquillo",		20068, 	66.85, 18.37245, -65.71655, (2101,302)],
			["Manatí",			44113, 	119.48, 18.42745, -66.49212, (1083,181)],
			["Maricao",			6276, 	94.85, 18.18079, -66.9799, (478,528)],
			["Maunabo",			12225, 	54.57, 18.00719, -65.89933, (1831,742)],
			["Mayagüez",		89080, 	201.11, 18.20107, -67.13962, (263,489)],
			["Moca",			40109, 	130.38, 18.39467, -67.11324, (280,253)],
			["Morovis",			32610, 	100.67, 18.32578, -66.40656, (1177,335)],
			["Naguabo",			26720, 	133.80, 18.21162, -65.73488, (2068,467)],
			["Naranjito",		30402, 	70.97, 18.30079, -66.24489, (1375,374)],
			["Orocovis",		23423, 	164.78, 18.2269, -66.391, (1177,489)],
			["Patillas",		19277, 	120.95, 18.00635, -66.01572, (1710,726)],
			["Peñuelas",		24282, 	115.57, 18.05635, -66.72156, (781,704)],
			["Ponce",			166327, 297.23, 18.01108, -66.61406, (907,709)],
			["Quebradillas",	25919, 	58.74, 18.47383, -66.93851, (489,143)],
			["Rincón",			15200, 	37.01, 18.34023, -67.2499, (99,302)],
			["Río Grande",		54304, 	157.01, 18.38023, -65.83127, (1958,297)],
			["Sabana Grande",	25265, 	92.80, 18.07774, -66.96045, (473,638)],
			["Salinas",			31078, 	179.67, 17.97747, -66.29795, (1397,742)],
			["San Germán",		35527, 	141.15, 18.08163, -67.0449, (357,621)],
			["San Juan",		395326, 123.93, 18.46633, -66.10572, (1644,242)],
			["San Lorenzo",		41058, 	137.55, 18.1894, -65.961, (1760,583)],
			["San Sebastián",	42430, 	182.39, 18.33662, -66.99018, (407,302)],
			["Santa Isabel",	23274, 	88.119, 17.96608, -66.40489, (1215,786)],
			["Toa Alta",		74066, 	69.98, 18.38828, -66.24822, (1386,269)],
			["Toa Baja",		89609, 	60.19, 18.44384, -66.25961, (1446,165)],
			["Trujillo Alto",	74842, 	53.77, 18.35467, -66.00739, (1727,302)],
			["Utuado",			33149, 	294.04, 18.26551, -66.70045, (786,396)],
			["Vega Alta",		39951, 	71.82, 18.41217, -66.33128, (1298,192)],
			["Vega Baja",		59662, 	118.78, 18.44439, -66.38767, (1215,181)],
			["Vieques",			9301, 	131.49, 18.14913, -65.44266, (2051,1078)],
			["Villalba",		26073, 	92.31, 18.12718, -66.49212, (1100,594)],
			["Yabucoa",			37941, 	142.99, 18.05052, -65.87933, (1892,676)],
			["Yauco",			42043, 	176.61, 18.03496, -66.8499, (572,649)]]
			

#Calculates Distance from one Territory to another using 'haversine' formula
def Distance (Territory1, Territory2):
	latitude1 = math.radians(Data_Set[Territory1][3])
	latitude2 = math.radians(Data_Set[Territory2][3])
	
	deltaLatitude = math.radians((Data_Set[Territory2][3] - Data_Set[Territory1][3]))
	deltaLongitude = math.radians((Data_Set[Territory2][4] - Data_Set[Territory1][4]))

	a = math.pow(math.sin(deltaLatitude/2), 2) + ((math.cos(latitude1) * math.cos(latitude2)) * math.pow(math.sin(deltaLongitude/2),2))
	c = 2 * (math.atan2(math.sqrt(a), math.sqrt(1-a)))
	
	result = Radius * c
	
	return result

#Initialize Data Set with every Territory controlling itself and having number of controlled territories of 1
def Initialize ():	
	image = Image.open('Map_Base.png')
	for x in range(0, len(Data_Set)):
		Data_Set[x].append(Data_Set[x][0])
		Data_Set[x].append(1)
		
		#Color stuff (Temp)
		color = (random.randint(0,200), random.randint(0,200), random.randint(0,200), 255)
		ImageDraw.floodfill(image, Data_Set[x][5], color, thresh = 100)
		
		Data_Set[x].append(color)
		
	image.save ("Map_Game1.png")
		
def PrintData ():
	for x in range(0, len(Data_Set)):
		print (Data_Set[x])
	
def Select_Attacker ():
	selected = random.randint(0, 77)
	#print("Selected Attacker: " + str(Data_Set[selected][0]) + " under the control of: " + str(Data_Set[selected][5]))
	return selected
	
def Select_Target (Attacker):
	Close_Target = 0
	Shortest_Distance = 999999999999999
	for x in range (0, len(Data_Set)):
		if (Data_Set[Attacker][6] != Data_Set[x][6]):
			if (Distance(Attacker, x) < Shortest_Distance):
				Close_Target = x
				Shortest_Distance = Distance(Attacker, x)
	return Close_Target
	
def Determine_Outcome (Attacker, Target):
	global Turn 
	
	print("Turn " + str(Turn) + ": " + str(Data_Set[Attacker][6]) + " attacked " + str(Data_Set[Target][0]) + " which is under the control of " + str(Data_Set[Target][6]))

	#Update amount of controled territorries
	Temp1 = GetID(Target)
	Data_Set[Temp1][7] = Data_Set[Temp1][7] - 1
	
	Temp2 = GetID(Attacker)
	Data_Set[Temp2][7] = Data_Set[Temp2][7] + 1
	
	#Change who controls
	Data_Set[Target][6] = Data_Set[Attacker][6]
	
	image = Image.open("Map_Game" + str(Turn) + ".png")
	
	color = Data_Set[GetID(Attacker)][8]
	ImageDraw.floodfill(image, Data_Set[Target][5], color, thresh = 5)
	
	Turn = Turn + 1
	
	image.save ("Map_Game" + str(Turn) + ".png")
	
def GetID (number):	
	for x in range (0, len(Data_Set)):
		if (Data_Set[x][0] == Data_Set[number][6]):
			return x
	
#--------------------------------
#Initialize
Initialize()
Has_Someone_Won = False


#Game Loop
while (not Has_Someone_Won):

	Attacker = Select_Attacker()
	Target = Select_Target(Attacker)
	Determine_Outcome(Attacker, Target)
	if (Data_Set[GetID(Attacker)][7] == 78):
		print(str(Data_Set[GetID(Attacker)][6]) + " has won")
		Has_Someone_Won = True;
		PrintData()
		
		
		
'''		
#To do:

When someone gets eliminated
When someone loses their Capital

'''

	
	
