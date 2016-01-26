import ujson as json

class BaseFunctions():
	def GetMessage(self, messageCode):
		if messageCode in ["0"]:
			data = {}
			data["message"] = "Ok!"
			data["code"] = "0"
			return data
		if messageCode in ["99"]:
			data = {}
			data["message"] = "Invalid Request"
			data["code"] = "99"
			return data
		if messageCode in ["98"]:
			data = {}
			data["message"] = "Invalid Request"
			data["code"] = "98"
			return data

	def ValidateRequest(self, requestJson):
		data = json.loads(requestJson)
		try:
			if data["message"]:
				return True
			else:
				return False
		except ValueError:
			return False
		except:
			return False