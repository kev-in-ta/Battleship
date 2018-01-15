# Play a two-player Battleship game with turn limits!

from random import randint

# initialize variables
board1 =[]
board2 = []
ship_list1 = []
ship_list2 = []
hit = 0
numships1 = 0
numships2 = 0
generations = 1
turns_allowed = 15

for x in range(5):
  board1.append(["O"] * 5)
  board2.append(["O"] * 5)

# function: initialize board
def clear_board (board):
  del board[0:25]
  for x in range(5):
    board.append(["O"] * 5)

# function: displays board state
def print_board(board):
  for row in board:
    print (" ".join(row))
  print ("")

# function: returns a random row coordinate
def random_row(board):
  return randint(1, len(board))

# function: returns a random column coordinate
def random_col(board):

  return randint(1, len(board[0]))

# function: adds a ship coordinate
def generate_ship(list, numships, board):
  ship_row = random_row(board)
  ship_col = random_col(board)
  if (ship_row, ship_col) not in list:
      list.append((ship_row, ship_col))
  else:
      generate_ship(list, numships, board)
  return numships + 1

def generate_ship2(list, numships, board):
  ship_row = random_row(board)
  ship_col = random_col(board)
  direction = randint(1,4)
  if direction % 2 == 0:
    ship_col2 = ship_col
    if direction % 3 == 1:
        ship_row2 = ship_row + 1
    else:
        ship_row2 = ship_row - 1
  else:
    ship_row2 = ship_row
    if direction % 3 == 1:
        ship_col2 = ship_col + 1
    else:
        ship_col2 = ship_col - 1
  if (ship_row, ship_col) not in list and (ship_row2, ship_col2) not in list and ship_row2 > 0 and ship_row2 < 6 and ship_col2 > 0 and ship_col2 < 6:
    list.append((ship_row, ship_col))
    list.append((ship_row2,ship_col2))
  else:
      generate_ship2(list, numships, board)
  return numships + 2


def generate_ship3(list, numships, board):
  ship_row = random_row(board)
  ship_col = random_col(board)
  direction = randint(1,2)
  if direction % 2 == 0:
    ship_col2 = ship_col
    ship_col3 = ship_col
    ship_row2 = ship_row + 1
    ship_row3 = ship_row - 1
  else:
    ship_row2 = ship_row
    ship_row3 = ship_row
    ship_col2 = ship_col + 1
    ship_col3 = ship_col - 1
  if (((ship_row == 1 or ship_row == 5) and direction == 2) or ((ship_col == 1 or ship_col == 5) and direction == 1)):
    generate_ship3(list, numships, board)
  elif (ship_row, ship_col) not in list and (ship_row2, ship_col2) not in list and (ship_row3, ship_col3) not in list:
    list.append((ship_row, ship_col))
    list.append((ship_row2, ship_col2))
    list.append((ship_row3, ship_col3))
  else:
    generate_ship3(list, numships, board)
  return numships + 3

# function: repeated game
def guess_ship(board, ship_list, turn, turns_allowed, hit, numships):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if (guess_row, guess_col) in ship_list:
    ship_list.remove((guess_row, guess_col))
    print ("Congratulations! You sunk a battleship!")
    hit += 1
    if hit == numships:
      print ("My ships are destroyed!")
    board[guess_row-1][guess_col-1] = "+"
    print_board(board)
  else:
    if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row-1][guess_col-1] == "X" or board[guess_row-1][guess_col-1] == "+"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row-1][guess_col-1] = "X"  
    print_board(board)
    if turn == turns_allowed - 1:
      print ("Game Over")
  return hit

# function: initiates the game
def play_game(board1, board2, ship_list1, ship_list2, turns_allowed, numships1, numships2):
  ditto = "y"
  hit1 = 0
  hit2 = 0
  while ditto == "y":
      for turn in range(turns_allowed):
        print ("Turn", turn + 1)
        print ("Player 1 Guess")
        hit1 = guess_ship(board2, ship_list2, turn, turns_allowed, hit2, numships2)
        if hit2 == numships2:
          break
        print ("Player 2 Guess")
        hit1 = guess_ship(board1, ship_list1, turn, turns_allowed, hit1, numships1)
        if hit1 == numships1:
          break
      hit1 = 0
      hit2 = 0
      ditto = input("Would you like to play again? (y/n)")
      if ditto == "y":
        clear_board(board1)
        clear_board(board2)
        numships1 = 0
        numships2 = 0
        for i in range(generations):
          numships1 = generate_ship3(ship_list1, numships1, board1)
          numships1 = generate_ship2(ship_list1, numships1, board1)
          numships2 = generate_ship3(ship_list2, numships2, board2)
          numships2 = generate_ship2(ship_list2, numships2, board2)
        print (ship_list1)
        print (ship_list2)
        print_board(board1)
        print_board(board2)

# generate battleships
clear_board(board1)
clear_board(board2)
for i in range(generations):
  numships1 = generate_ship3(ship_list1, numships1, board1)
  numships1 = generate_ship2(ship_list1, numships1, board1)
  numships2 = generate_ship3(ship_list2, numships2, board2)
  numships2 = generate_ship2(ship_list2, numships2, board2)

print("Welcome to Battleship! Columns and rows are numbered 1 to 5.")

print ("Player 1 Board")
print (ship_list2, '\n')
print ("Player 2 Board")
print (ship_list1, '\n')

print_board(board1)
print_board(board2)

play_game(board1, board2, ship_list1, ship_list2, turns_allowed, numships1, numships2)
