import ujson as json
import tornado.web
from tornado import gen
import model
import utilities

# Restful API Methods

# User Count Verbs
class UserCountHandler(model.UserCount, utilities.BaseFunctions, tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		usersCount = yield self.GetUsersCount()
		
		responseHeader = self.GetMessage("0")

		self.set_status(200)
		response = {"responseheader":responseHeader, "data": {"count":usersCount}}
		self.finish(response)

# Users Verbs
class UsersHandler(model.Users, utilities.BaseFunctions, tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		usersList = yield self.GetUsersList()
		
		responseHeader = self.GetMessage("0")

		self.set_status(200)
		response = {"responseheader":responseHeader, "data": {"users":usersList}}
		self.finish(response)