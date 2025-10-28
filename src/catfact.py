import requests
class Client():
	def __init__(self):
		self.api="https://catfact.ninja"
	def get_list_breeds(self,limit:str="1"):
		return requests.get(f"{self.api}/breeds/?limit={limit}").json()["data"]
	def get_random_fact(self):
		return requests.get(f"{self.api}/fact").json()
	def get_list_facts(self):
		return requests.get(f"{self.api}/facts/").json()["data"]