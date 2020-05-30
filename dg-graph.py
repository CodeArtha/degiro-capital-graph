from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyring
import sys
import os
import json
from tinydb import TinyDB
from tinydb import Query
import time

# columns = date | portfolio value | delta
# DATABASE.insert({'date': None,
#                  'value': None,
#                  'delta': None})
DATABASE = TinyDB("history.json")


config = ""


def fetch():
	# check no entry yet for today
	today = time.asctime()
	DATABASE.
	# check time > marketclose + 20 min
	# connect to degiro website
	# grabs the portfolio value
	# calculates delta with yesterday
	# saves: date, portfolio value, delta to database


def clear_terminal():
	"""Clears the terminal, OS independant"""
    os.system('cls' if os.name == 'nt' else 'clear')
    return None


def load_config():
	global config
	print('hello world sucks')
	with open("config.json", "r") as read_file:
		config = json.load(read_file)
	return None

def update_config(field, value):
	global config
	config[field] = value

	with open("config.json", "w") as write_file:
		json.dump(config, write_file)

	return None

def new_config():
	with open("config.json", "w") as write_file:
		json.dump({"dguser" : "", "dgpass" : "", "dgpassfile" : "", "marketclose" : ""}, write_file)
	return None


def main(args):
	"""Parsing command line arguments"""
	if args[1] == "config":
		if args[2] == "--restore-defaults":
			new_config()
		if args[2] == "--endtime":
			update_config("marketclose", args[3])
		if args[2] == "--dguser":
			update_config("dguser", args[3])
		if args[2] == "--dgpass":
			update_config("dgpass", args[3])
		if args[2] == "--dgpassfile":
			update_config("pwdfile", args[3])
	if args[1] == "graph":
		pass
	if args[1] == "table":
		pass
	if args[1] == "export":
		pass
	if args[1] == "fetch":
		pass

	print(HELP_MESSAGE)


if __name__ == "__main__":
	main(sys.argv)
