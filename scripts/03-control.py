"""03-control.py

This script provides practice working with control logic. 

We practice if and comparison operators,
conditions, branching, and repetition.

Note: we also bring in the html module
"""
from browser import document, console, html

def show3(event):
  # display helpful information
  console.log('You clicked button 3!')
  console.log('name1=' + document['input-name1'].value)
  console.log('name2=' + document['input-name2'].value)
  console.log('num1=' + document['input-num1'].value)
  console.log('num2=' + document['input-num2'].value)

  # Get values (always text on a web page)
  name1 = document['input-name1'].value 
  name2 = document['input-name2'].value 
  num1 = document['input-num1'].value
  num2 = document['input-num2'].value

  # Try to convert the number values to integers
  # This can fail (for example if the input is empty)
  # So we first try it 
  # If it works, great!
  # If it doesn't (there is an exception), find a way to keep our app working
  try:
    x = int(num1)
  except:
    x = None

  try:
    y = int(num2)
  except:
    y = None

  # Compare the numbers and prepare a suitable message
  if x is None or y is None:
    message = f'Oh oh! We could not compare the numbers :(.'
    document['output3'].text = message
  elif x > y:
    message = f'Wow! num1 ({num1}) is GREATER than num2 ({num2}).'
    document['output3'].text = message
  elif x < y:
    message = f'Hey! num1 ({num1}) is LESS than num2 ({num2}).'
    document['output3'].text = message
  else:
    message = f'Yay! num1 ({num1}) is EQUAL to num2 ({num2}).'
    document['output3'].text = message
    # Yay! let's empty the text and APPEND a new <h3> element
    # document['output3'].clear()
    # document['output3'] <= html.H3(message)

  # Exercise: Compare the length of the names 
  # and replace this with a suitable message
  # Can the len function ever fail? 
  # Keep the app running if there is an exception

  name1len = len(name1)
  name2len = len(name2)
  secondMessage = f'Your name has {name1len} letters and your friend has {name2len}.'
  document['output3-names'].text = secondMessage

  # Sheep ranch

  ranchMessage = f'Hi {name1}! Hi {name2}! You can store {x*y} sheep on a {x} mi x {y} mi ranch.'
  document['output3-ranch'].text = ranchMessage

  # Let's append a line break
  document['output3-ranch'] <= html.BR()

  # Create an article to hold our sheep  
  article = html.ARTICLE()

  # Append sheep to the article
  for i in range(0, x*y):
    console.log(i)
    # Create a sheep image
    # <img src="images/sheep.png" alt="sheep" width="50" height="50">
    image = html.IMG()
    image.src = "images/sheep.png"
    image.alt = "one sheep"
    image.width = 50
    image.height = 50
    article <= image
  
  # Append our article of sheep to the document
  document['output3-ranch'] <= article

# First, bind the btn3 click event to our callback method 
document['input-btn3'].bind('click', show3)