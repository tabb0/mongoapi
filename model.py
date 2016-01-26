from tornado import gen
import motor

class UserCount():
	@gen.coroutine
	def GetUsersCount(self):
		n = yield self.settings["db"].users.find().count()

		raise gen.Return(n)

class Users():
	@gen.coroutine
	def GetUsersList(self):
		userList = []
		usersCursor = self.settings["db"].users.find()

		while (yield usersCursor.fetch_next):
			document = usersCursor.next_object()
			userList.append(document["email"])

		raise gen.Return(userList)