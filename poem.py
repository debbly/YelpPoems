from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

client = Client(auth)

# Parameters, update the limit to randomize! 
params = {
	'limit': '3'
}

#need error checking in python

def main():
	city = ''
	all_words_dict = text(city)['snippet_text'].split('\n')

def text(city):
# User should input the city
	jsonString = client.search(city, params)
	json = jsonString[1]
	return json['businesses']