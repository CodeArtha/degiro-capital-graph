import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json
import time
import keyring
import yaml

degiro = degiroapi.DeGiro()

conf = {}

def read_config():
	with open('config.yml', 'r') as file
		global conf
		conf = yaml.safe_load(file)
	
		return 0
		
def update_config():
	with open('config.yml', 'w') as file
		global conf
		yaml.dump(conf, file)
		
		return 0
		
def dg_login():
	global degiro 
	
	if conf['auth_method'] == 'password':
		password = conf['dgpass']
	if conf['auth_method'] == 'keyring' and conf['isSetKeyring']:
		password = keyring.get_password("degiro", conf['username'])
	if conf['auth_method'] == 'keyfile':
		with open(conf['dgpassfile'], 'r') as f:
			password = f.readline().rstrip()

	degiro.login(conf['username'], password)
	
def setup():
	pass

def run():
	pass
	
if __name__ == "__main__":
	run()
	