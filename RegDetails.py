from bson.objectid import ObjectId


class UserDetails(object):
	"""Class for storing UserDetails"""
	
	def __init__(self,User_ID=None,User_Name=None,FullName=None,Email=None,Password=None,noOfSessions=[]):
		if User_ID is None:
			User_ID=ObjectId()
		else:
			self.ID=User_ID

		self.User_Name=User_Name
		self.FullName=FullName
		self.Email=Email
		self.Password=Password	
		self.noOfSessions=[]	
		
	def get_as_json(self):
		""" Method returns the JSON representation of the Contac object, this can be saved to MongoDB """
		return self.__dict__
