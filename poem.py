from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

client = Client(auth)

# Parameters should be user inputted
params = {
	'limit': '1'
}

def main():
	city = ''
	all_words_dict = text(city)

def text(city):
# User should input the city
	jsonString = client.search(city, params)
	return json['text']