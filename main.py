'''
John G. Wilson Negroni
https://github.com/JakeRylander/

Python Based Clone of the Popular FB Bot WarWorldBot2020 using Puerto Rico Municipalities
'''

import math
import random
from PIL import Image, ImageDraw, ImageFilter
from Territory import Territory
import csv

#Statistics
Territories_Remaining = 0

#Radius of Ze Earth-ish
Radius = 6371000

#Time and Record Keeping
Turn = 1
Month = 1
Year = 2069
Month_Strings = ["null", "January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#List where all Territory Objects are Stored
Territories = []

#Returns Distance from one Territory to another using 'haversine' formula
def Distance (Territory1, Territory2):

	#Convert Latitutes to Radians
	latitude1 = math.radians(Territory1.latitude)
	latitude2 = math.radians(Territory2.latitude)
	
	#Average Latitude
	deltaLatitude = math.radians(Territory2.latitude - Territory1.latitude)
	
	#Average Longitude
	deltaLongitude = math.radians(Territory2.longitude - Territory1.longitude)

	#Haversine Formula Shenanigans
	a = math.pow(math.sin(deltaLatitude/2), 2) + ((math.cos(latitude1) * math.cos(latitude2)) * math.pow(math.sin(deltaLongitude/2),2))
	c = 2 * (math.atan2(math.sqrt(a), math.sqrt(1-a)))
	
	#Multiply by Radius of the Earth
	result = Radius * c
	
	#Return Distance
	return result

#Initialize Data Set with every Territory controlling itself and having number of controlled territories of 1
def Initialize ():	
	
	#Global References
	global Territories_Remaining

	#Opens Base Map Image
	image = Image.open('Map_Base.png')
	
	#CSV Dialect Register
	csv.register_dialect('myDialect', delimiter = ',', skipinitialspace=True)
	
	#Parse CSV to fill list with Objects created from parsed CSV
	with open('data.csv', 'r', encoding='UTF-8') as csvFile:
		reader = csv.reader(csvFile, dialect='myDialect')
		for row in reader:
			
			#Generate Object into temp holder to finalize color setting
			Temp = Territory(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

			#Sets a Random Color to each territory (Temporary)
			color = (random.randint(0,200), random.randint(0,200), random.randint(0,200), 255)
			ImageDraw.floodfill(image, Temp.image_coords, color, thresh = 100)
			
			#Assign color to the Territory Object
			Temp.assigned_color = color
			
			Territories.append(Temp)
		
	#Close CSV
	csvFile.close()
		
	#Saves Map with the assigned colors to begin Game
	image.save ("Map_Game1.png")
	
	#Set Initial Statistics Values
	Territories_Remaining = len(Territories)
		
#Testing Funcion for more neatly printing Data
def PrintData ():

	#Itireration over Territories
	for x in Territories:
		x.data_print()
	print("")
	
#Returns an Int which is the index of one of the Territories in the Data_Set List
def Select_Attacker ():
	
	#Pick Random Int from lenght of list.
	selected = random.choice(Territories)
	
	#Return Index of Attacker
	return selected
	
#To Do: Algorithm for N amount of closests territories instead of 2
#Selects 2 closests targets from attacker and picks 1 of them to attack, returns the Index of the Target
def Select_Target (Attacker):

	Target_List = [None,None]
	Shortest_Distance = [math.inf, math.inf] #Actually using an infinite number
	for Target in Territories:
		if (Attacker.controled_by.name != Target.controled_by.name):
			if (Distance(Attacker, Target) < Shortest_Distance[0]):
				Target_List[0] = Target
				Shortest_Distance[0] = Distance(Attacker, Target)
			elif (Distance(Attacker, Target) < Shortest_Distance[1]):
				Target_List[1] = Target
				Shortest_Distance[1] = Distance(Attacker, Target)
				
	Target = random.choice(Target_List)
	
	while (Target == None):
		Target = random.choice (Target_List)
		
	return Target
	
#Return String representation of the Date
def Get_Date ():

	#Global References
	global Month, Year

	#Generate string representation
	date = Month_Strings[Month] + " " + str(Year)

	#Return Date in string form
	return date

#Updates the Date once turn ends
def Update_Date ():
	
	#Global References
	global Turn, Month, Year
	
	#If End of Year
	if (Month == 12):
		Month = 1
		Year =  Year + 1
	else:
		Month = Month + 1
		
	#Increment Turn
	Turn = Turn + 1
	
	#New line for better readinto
	print("")
		
#To Do: More Dynamic, not just a 50/50 chance of winning or losing
#Determines the Outcome of the Fight
def Determine_Outcome (Attacker, Target):

	#Global References
	global Territories_Remaining
	
	#50/50 Chance of Defending against Attack
	chance = random.randint(0, 1)
	
	#Flavor Printout for Initial Attack
	print(Get_Date() + ": \n" + str(Attacker.controled_by.name) + " attacked " + str(Target.name) + " which is under the control of " + str(Target.controled_by.name) + ".")
	
	#Open Image
	Base_Map = Image.open("Map_Game" + str(Turn) + ".png")
	
	#Succesful Attack
	if (chance):

		#If Capital that got taken
		if (Target.name == Target.controled_by.name):
			print(str(Target.name) + " wasn't able to defend and lost it's Capital.")
		
		#Controlled Territory
		else:
			print(str(Target.controled_by.name) + " wasn't able to defend and lost it's territory.")

		#Update amount of controled territorries
		Target.controled_by.amount_of_territories = Target.controled_by.amount_of_territories - 1
		Attacker.controled_by.amount_of_territories = Attacker.controled_by.amount_of_territories + 1

		#If Target has no Territory left
		if (Target.controled_by.amount_of_territories == 0):
			print(str(Target.controled_by.name) + " has lost all territory, " + str(Target.controled_by.name) + " has been defeated.")
			
			#Decrease Remaining Territories
			Territories_Remaining = Territories_Remaining - 1
			print(str(Territories_Remaining) + " Territories Remaining.")
			
		#Change who controls
		Target.controled_by = Attacker.controled_by
		
		#Update Image Territory Color
		Attacker_Color = Attacker.controled_by.assigned_color
		ImageDraw.floodfill(Base_Map, Target.image_coords, Attacker_Color, thresh = 5)
		
		#Overlay Generator
		
		#######################
		#Save Base Map
		Base_Map.save ("Map_Game" + str(Turn) + ".png")
		
		#Open Base Map, Save as Overlay, and Re-open
		Base_Map = Image.open("Map_Game" + str(Turn) + ".png")
		Base_Map.save ("Overlay.png")
		Map_Overlay = Image.open("Overlay.png")
		
		#Load Overlay Pixels
		Overlay_Pixel = Map_Overlay.load()
		
		#Get Image Size
		width, height = Map_Overlay.size
		
		#Loops Over entire Base Map making Transparent everything that is not the Attacker Territory
		for x in range(0,width):
			for y in range(0,height):
				if (not (Overlay_Pixel[x,y] == Attacker_Color)):
					Overlay_Pixel[x,y] = (0,0,0,0)
		
		#Make Map with Edges of Territories
		Map_Overlay = Map_Overlay.filter(ImageFilter.FIND_EDGES)
		
		#Generate List of Edge Pixels	
		EdgeList = []
		for x in range(0,width):
			for y in range(0,height):
				if (not(Overlay_Pixel[x,y] == (0,0,0,0))):
					EdgeList.append((x,y))

		#Load Overlay Pixels again
		Overlay_Pixel = Map_Overlay.load()
		
		#Grow Pixel Edges Out 8 Pixels (Very Redundant can be more efficient)
		for coords in EdgeList:
			x,y = coords
			Overlay_Pixel[x,y] = Attacker_Color
			for size in range(1,8):
				Overlay_Pixel[x+size,y] = Attacker_Color
				Overlay_Pixel[x-size,y] = Attacker_Color
				Overlay_Pixel[x,y+size] = Attacker_Color
				Overlay_Pixel[x,y-size] = Attacker_Color
			
		#Refind Edges for Full Territory Overlay now
		Map_Overlay_Highlight = Map_Overlay.filter(ImageFilter.FIND_EDGES)

		#Load Overlay Pixels again
		Overlay_Pixel = Map_Overlay_Highlight.load()
		
		#Generate New Edge Pixel List
		EdgeList = []
		for x in range(0,width):
			for y in range(0,height):
				if (not(Overlay_Pixel[x,y] == (0,0,0,0))):
					EdgeList.append((x,y))
		
		#Load Overlay Pixels again
		Overlay_Pixel = Map_Overlay_Highlight.load()
		Map_Overlay_Pixel = Map_Overlay.load()
		
		#Finish Territory Overlay by comparing New Outer Edge to Filled Color
		color_highlight = (0,255,0,255)
		for coords in EdgeList:
			x,y = coords
			Overlay_Pixel[x,y] = color_highlight
			for size in range(1,8):
				Overlay_Pixel[x+size,y] = color_highlight
				Overlay_Pixel[x-size,y] = color_highlight
				Overlay_Pixel[x,y+size] = color_highlight
				Overlay_Pixel[x,y-size] = color_highlight
						
						
		#Smoothen Edges
		Map_Overlay_Highlight.show()
		Map_Overlay_Highlight = Map_Overlay_Highlight.filter(ImageFilter.SMOOTH_MORE)
		
		Map_Overlay_Highlight.show()

		#Open Base Map
		Finalized_Map = Image.open("Map_Game" + str(Turn) + ".png")
		Finalized_Map.paste(Map_Overlay_Highlight, Map_Overlay_Highlight)
		
		Finalized_Map.save("Map_Game_Final" + str(Turn) + ".png")
		#######################
		
	#Succesfully Defended Attack
	else:
		print(str(Target.controled_by.name) + " succesfully defended.")
	
	#Update Date and Turn
	Update_Date()
	
	#Save Image
	Base_Map.save ("Map_Game" + str(Turn) + ".png")
	
#--------------------------------
#Initialize
Initialize()
Has_Someone_Won = False

#Game Loop
while (not Has_Someone_Won):

	#PrintData()
	#Select Attacker
	Attacker = Select_Attacker()
	
	#Select Target
	Target = Select_Target(Attacker)
	
	#Determine Outcome
	Determine_Outcome(Attacker, Target)
	
	
	#Check if someone has all Territories
	if (Attacker.controled_by.amount_of_territories == len(Territories)):
	
		#Someone Won
		print(str(Attacker.controled_by.name) + " has won")
		Has_Someone_Won = True;
		
'''		
#To do:
IDK will write down ideas here later
'''