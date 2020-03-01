from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyring
import sys
import os
import json


config = dict()


def clear_terminal():
	"""Clears the terminal, OS independant"""
    os.system('cls' if os.name == 'nt' else 'clear')
    return None


def load_config():
	# reads the JSON config file
	# saves the data in the config dictionary
	return None

def update_config(field, value):
	# loads the json config file, changes the apropriate field, saves the file, load_config()
	return None


def main(args):
	"""Parsing command line arguments"""
	if args[1] == "config":
		if args[2] == "--endtime":
			update_config("endtime", args[3])
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
