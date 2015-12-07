from pymongo import MongoClient
from bson.objectid import ObjectId
from RegDetails import UserDetails
from datetime import datetime
from flask import request

class UserRepo(object):
    """ Repository implementing CRUD operations on contacts collection in MongoDB """
    def __init__(self):
        # initializing the MongoClient, this helps to 
        # access the MongoDB databases and collections 
        self.client = MongoClient(host='localhost', port=27017)
        self.database = self.client['user_db']
    def create(self,user):
	create_id =None
	if user is not None:
		userName=user.User_Name	
		if self.database.users.find_one({"User_Name":userName}):
			print create_id
			return create_id
		else:
			create_id = self.database.users.insert(user.get_as_json())
			print create_id
			return create_id
	else:
		raise Exception("Nothing to save, becuase contact parameter is None")
	

    def read(self,user_id=None):
	if user_id is None:
		return self.database.User.find({})
	else:
		return self.database.User.find({"_id":user_id})

    def is_user_valid(self,user_name, password):
	if self.database.users.find_one({"User_Name":user_name}) and self.database.users.find_one({"Password":password}):
		time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		ip=request.remote_addr
		sessionobj={'ipaddress':ip,'time':time}
		self.database.users.update({"User_Name":user_name},{"$push":{"noOfSessions":sessionobj}})
		return True
	else:
		return False
