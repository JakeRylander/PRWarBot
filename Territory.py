class Territory:
	def __init__ (self, name, population, area, latitude, longitude, image_x, image_y):
		self.name = str(name)
		self.latitude = float(latitude)
		self.longitude = float(longitude)
		self.population = int(population)
		self.area = float(area)
		self.image_coords = (int(image_x), int(image_y))
		self.controled_by = self
		self.amount_of_territories = 1
		self.assigned_color = None
		
	def data_print(self):
		print(self.name, self.latitude,	self.longitude,
		self.population,
		self.area ,
		self.image_coords ,
		self.controled_by.name, 
		self.amount_of_territories,
		self.assigned_color)