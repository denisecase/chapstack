"""01-hello.py

This script provides practice getting started with Bython ("Browser Python").

This is a standard Python script, starting with module imports. 

In this case, we import:
 * browser - a module shipped with the Brython engine brython.js

From this browser module, we import the following attributes:
 * document - a Python dictionary representing page content shown in the browser window
 * console - the default output terminal
 * alert - a popup read-only announcement to the user 
"""
from browser import document, console, alert

def showTalk(event):
  console.log('You clicked button 1!')
  console.log('We are sending a greeting to the console - hello!')
  console.log(event)
  console.log('Explore the mouse event that was triggered - click the information above!')
  document['output1'].text = "You made a " + event.type + " event!"
  alert("hello!")

""" 
Get the input button (by id) from the document dictionary
Bind any click event on this element to the logic in the showTalk function
"""
document['input-btn1'].bind('click', showTalk)

""" Skills practiced:

Using Python dictionaries.
Looking up a dictionary item with the string key (e.g., document['input-btn'])
Calling functions with arguments (e.g. a string event and a function name)
"""