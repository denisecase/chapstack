"""05-sequences.py

This script provides practice working with sequence collections: lists & tuples.

Sequences are the same type. We often use them to track items 
we may want to sort or search. 

Think of common lists - a list of groceries, a list of words.

A tuple is a multi-part item. 
Think of table records - each record/row is unique, but the 
order & type of the columns are the same for all.
A tuple is like a row in a data table.
"""
from browser import document, console, html

def convertToCharList(s):
   # Splitting a word into a list of letters 
  # creates a list with each character in the word as an element. 
  charList = list(s)
  # Log the list
  console.log(f'charList1={charList}')
  return charList

# from the Python docs
# Code that modifies a collection while 
# iterating over that same collection can be tricky to get right. 
# Instead, it is usually more straight-forward to 
# create a new collection.
def dropSpecialCharacters(inList):
  outList = []
  for line in inList:
    firstParens = line.find('(')
    secondParens = line.find(')')
    if firstParens > -1 and secondParens > -1:
      console.log(f'firstParens={firstParens}')
      console.log(f'secondParens={secondParens}')
      firstPart = line[0:firstParens - 1]
      secondPart = line[secondParens+1:len(line) ]
      line = firstPart + secondPart
      console.log(f'cleanline={line}')
    line = line.replace("*","")
    if len(line) > 1:
      outList.append(line.strip())
  return outList


def convertToGroceryList(s):
  lineList = s.splitlines()
  console.log(f'lineList={lineList}')
  return lineList

def show5(e):
  console.log('You clicked button 5!')
  name1 = document['input-name1'].value 
  document['output5-message'].text = convertToCharList(name1)

def show5groceries(e):
  console.log('You clicked the other button 5!')
  recipe = document['input-recipe-5'].value 
  rawList = convertToGroceryList(recipe)
  cleanList = dropSpecialCharacters(rawList)
  sortedList = sorted(cleanList)
  for line in sortedList:
    document['output-list-5'] <= html.LI(line, Class="list-group-item")

document["input-btn5"].bind("click", show5)
document["input-recipe-5"].bind("input", show5groceries)
