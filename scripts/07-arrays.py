"""07-arrays.py

This script provides practice working with arrays.

We use them to process a tic-tac-toe board,
modeled as an array of cells.

Arrays start at 0, so our indices will be 0 to 8

[0][1][2]
[3][4][5]
[6][7][8]

"""
from browser import document, console, html
import math

board = ["", "", "", "", "", "", "", "", ""]

def chooseCell(lastPick):
  if board[4] == '':
    return 4
  else:
    for i in range(0,9):
      if board[i] == '':
        return i

def checkForWinner(mark):
  if board[0] == board[1] == board[2] == mark:
    return mark
  if board[3] == board[4] == board[5] == mark:
    return mark
  if board[6] == board[7] == board[8] == mark:
    return mark
  if board[0] == board[3] == board[6] == mark:
    return mark
  if board[1] == board[4] == board[7] == mark:
    return mark
  if board[2] == board[5] == board[8] == mark:
    return mark
  if board[0] == board[4] == board[8] == mark:
    return mark
  if board[2] == board[4] == board[6] == mark:
    return mark
  else:
    return None

def drawBoard(event):
  console.log('You clicked button 7!')
  document["output7-message"].text = 'Tic-Tac-Toe - You first!'
  for i in range(0,9):
    cellID = 'box'+str(i)
    document[cellID].classList.add("game-cell")

def updateGame(i, mark):
  board[i] = mark
  document['box'+str(i)].text = mark

def getIfromStringID(stringID):
  iIndex = len(stringID) - 1
  iChar = stringID[iIndex]
  i = int(iChar)
  return i

def processUserChoice(event):
  cellID = event.target.id
  console.log(f'You clicked in {cellID}')
  if document[cellID].text == '':
    i = getIfromStringID(cellID)
    updateGame(i,"X")
    winner = checkForWinner("X")
    if winner == "X":
      document["output7-message"].text = 'Tic-Tac-Toe - You WON!'
    else:
      j = chooseCell(i)
      updateGame(j,"O")
      winner = checkForWinner("O")
      if winner == "O":
        document["output7-message"].text = 'Tic-Tac-Toe - AI WON!'
      else:
        document["output7-message"].text = 'Tic-Tac-Toe - Your turn!'

document["input-btn7"].bind("click", drawBoard)
document["box0"].bind("click", processUserChoice)
document["box1"].bind("click", processUserChoice)
document["box2"].bind("click", processUserChoice)
document["box3"].bind("click", processUserChoice)
document["box4"].bind("click", processUserChoice)
document["box5"].bind("click", processUserChoice)
document["box6"].bind("click", processUserChoice)
document["box7"].bind("click", processUserChoice)
document["box8"].bind("click", processUserChoice)
