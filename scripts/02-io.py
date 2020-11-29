"""02-io.py

This script provides practice working with Python variables. 

Exercise: choose operations in addition to (or instead of) addition.
"""
from browser import document, console

def show2(event):
  console.log('You clicked button 2!')
  console.log('name1 element=' + document['input-name1'])
  console.log('num1 element=' + document['input-num1'])
  console.log('name1=' + document['input-name1'].value)
  console.log('name2=' + document['input-name2'].value)
  console.log('num1=' + document['input-num1'].value)
  console.log('num2=' + document['input-num2'].value)

  # This gets the whole element (a fairly complex object)
  name1element = document['input-name1']
  name2element = document['input-name2']

  # What we really want is the input element's value attribute
  name1 = document['input-name1'].value or 'Please enter your name'
  name2 = document['input-name2'].value or 'Please enter your friend\'s name'
  num1 = document['input-num1'].value
  num2 = document['input-num2'].value

  # convert values to numbers as needed (HTML values are always strings)
  total = int(num1)+int(num2)

  # use Python 3.6 string literals or f-strings to create a message
  message = f'Hello {name1} & {name2}, your sum is {num1}+{num2} or {total}!'
  document['output2'].text = message

# First, bind the btn2 click event to our callback method 
document['input-btn2'].bind('click', show2)

# Then, bind input events on the numbers (fires when the input changes)
document['input-num1'].bind('input', show2)
document['input-num2'].bind('input', show2)

# Exercise - bind input events on the name fields as well


