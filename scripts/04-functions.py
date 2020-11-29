"""04-functions.py

This script provides practice working with functions.

It's based on the script 3 - we use functions to make our code more
reusable and easier to maintain. 

We add some fun css effects (zoom when we hover).

See index.html - in this example, our html has additional elements
See styles - we add a zoom class to our images with some :hover behavior
"""
from browser import document, console, html

# Define a function to convert a string value to integers
# If it works, return the int
# If it fails, return None
def getIntFromString(s):
  try:
    x = int(s)
  except:
    x = None
  return x

# Define a function that takes 2 integers and 
# returns a string message comparing them
def getCompareMessage(a, b):
  if type(a) != int or type(b) != int:
    s = f'Oh oh! We could not compare the numbers :(.'
  elif a > b:
    s = f'Wow! num1 ({a}) is GREATER than num2 ({b}).'
  elif a < b:
    s = f'Hey! num1 ({a}) is LESS than num2 ({b}).'
  else:
    s = f'Yay! num1 ({a}) is EQUAL to num2 ({b}).'
  return s

# Define a function that returns a new sheep image
def makeSheepImage():
  image = html.IMG()
  image.src = "images/sheep.png"
  image.alt = "one sheep"
  image.width = 50
  image.height = 50
  # Add classes Cwith a capital Class
  image.class_name = "zoom"
  return image

# Define a callback function (for after an event)
def show4(event):
  console.log('You clicked button 4!')

  # Compare numbers
  num1 = document['input-num1'].value
  num2 = document['input-num2'].value
  x = getIntFromString(num1)
  y = getIntFromString(num2)
  document['output4'].text = getCompareMessage(x,y)

  # Compare names
  name1 = document['input-name1'].value 
  name2 = document['input-name2'].value 
  name1len = len(name1)
  name2len = len(name2)
  secondMessage = f'Your name has {name1len} letters and your friend has {name2len}.'
  document['output4-names'].text = secondMessage

  # Explain the ranch
  ranchMessage = f'Hi {name1}! Hi {name2}! You can store {x*y} sheep on a {x} mi x {y} mi ranch.'
  document['output4-ranch-message'].text = ranchMessage

  # In this exercise, we've explicitly added the article and br to the html

  # Append the sheep
  for i in range(0, x*y):
    document['output4-ranch-article'] <= makeSheepImage()

# Define a callback function (for after an event)
def moveSheep4(event):
  console.log('You clicked on the ranch!')
  # make sheep move 


# First, bind the btn4 click event to our callback method 
document['input-btn4'].bind('click', show4)

# Next, bind the mouseover event to our article
document['output4-ranch-article'].bind('click', moveSheep4)