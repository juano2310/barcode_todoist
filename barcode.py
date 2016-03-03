#!/usr/bin/env python

import sys
import termios
import contextlib
import json
import todoist
from semantics3 import Products
 
products = Products(
  api_key = "semantics3_key",
  api_secret = "semantics3_secret"
)

def todoist_user = "Todoist_user"
def todoist_password = "Todoist_password"

@contextlib.contextmanager
	
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)

def main():
    print 'exit with ^C or ^D'
    api = todoist.TodoistAPI()
    TODOuser = api.login(todoist_user, todoist_password)
    api.projects.sync()
    ShoppingList = [p for p in api.state['Projects'] if p['name'] == 'Shopping'][0]
    buffer = ''
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(1)
                if ch == chr(4):
                    break                
                if ch == chr(10):
   					# Build the request
   					print(buffer)
   					try:
	   					products.products_field("upc", buffer)
						products.products_field("fields", ["name"])
						# Run the request
						results = products.get_products()
						finalresult = json.dumps(results['results'][0]['name']).strip("\"")
						print(finalresult)
						item = api.items.add(finalresult, ShoppingList['id'])
						api.commit()
					except Exception as e:
						print(e)
					buffer = ''
                else:
                	buffer = buffer + ch		
        except (KeyboardInterrupt, EOFError):
            pass


if __name__ == '__main__':
    main()