#! /usr/local/opt/python/bin/python3.8
'''

B) Make sure each Person has applied the following topics on the code which have been taught in the lecture:

UML at least 3 good diagrams. "good" means you can pump it up artificially as written in DDD. 
Please export the pics. I can not install all tools to view them!

DDD If your domain is too small, invent other domains around and document these domains 
(as if you have 5 Mio € from Edlich-Investment!) Develop a clear strategic design with mappings/relationships
Metrics at least two. Sonarcube would be great

Clean Code Development at least 5 points you can show me + 10 points for your cheat sheet

Build Management with any Build System as Ant, Maven, Gradle, etc. (only travis is perhaps not enough) Do e.g. generate Docs, call tests, etc.
Integrate some nice Unit-Tests in your Code to be integrated into the Build
Continuous Delivery show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, GitHub Action, GitLab CI, etc.
Use a good IDE and get fluent with it as e.g. IntelliJ. What are your favorite Key-Shortcuts?!
DSL Create a small DSL Demo example snippet in your code even if it does not contribute to your project
Functional Programming (prove that you have covered all functional aspects in your code as
only final data structures
(mostly) side effect free functions
the use of higher-order functions
functions as parameters and return values
use closures / anonymous functions
Please give me a hint as a checklist for each 1-9 where I can find the info for points 1-9 best as links in the README.md
It is quite tedious to search in a Github repo if it is not your repo...

The complete documentation must be found in the GitHub / GitLab doc e.g. ReadMe or Wiki. It should explain also part B in 1-2 paragraphs per point!

The contribution in Moodle is just a Link to GitHub in the comment section!



Todolist for your 4-wins-project to work:


# done:
# 1) write function to create board, function to insert stone, function to check whether player1 or player2 won the game
# 2) write loop: while game still running, wait for input of player, place stone, check whether game is over etc. 
# 3) test game engine. Including for words and larger numbers

#currenttodo:

# todo: 
# go for the Edlich tasks 
# rename the check functions. Insert some assert statements there, please. 
# 4) code can be organized in a game class, see for example https://gist.github.com/poke/6934842
# 5) ...?


from Edlich: what have I done so far:

A) Write a small pet project to get into coding again. You might want to 
use a language like Python which is also good for this Master! 
The code can be relatively simple (e.g. simple game with console output).


context info: quite a tough grading key. VS other projects vermutlich.
Notenschlüssel für das WS 20/21
100	% of the points is which grade?
97	1,00
94	1,30
91	1,70
88	2,00
85	2,30
82	3,70
79	3,00
76	3,30
73	3,70
70	4,00
                        
'''

import numpy as np
import random
import re

def create_board(rows, columns):
    board = np.zeros((rows,columns),dtype=np.int8)
    return board


def one_to_zero_indexing(number):
    return number-1

# does_column_has_space checks whether a stone can still be inserted in certain column (columns fill up)
def does_column_has_space(board, current_player_input_column):
    # user indexing to 0-indexing of matrices
    selected_column=one_to_zero_indexing(current_player_input_column)
    selected_column_array = board[:,selected_column]
    #np.any works on bool arrays
    if np.any(selected_column_array == 0):
        return True
    else:
        return False


# inserts stone, if possible, otherwise prints "move not permitted" and returns the board unchanged
# 3 values are possible on the board / matrix:
# 0 - nothing played here yet
# 1 - Player 1 has set a stone here
# 2 - Player 2 has set a stone here 
def insert_stone(board, current_player_input_column, current_player):
    # user indexing to 0-indexing of matrices
    selected_column=one_to_zero_indexing(current_player_input_column)
    
    #create a new board to gurantee final data structures
    new_board=board.copy()

    #slice out the column array
    selected_column_array = new_board[:,selected_column]
    
    #fill up board from 'max to min'
    empty_slot = np.max(np.where(selected_column_array == 0))
    new_board[empty_slot,selected_column] = current_player
    return new_board


#recursion without using mutable variables:
def check_whether_game_definitely_undecided(board_slice):
    #extract all zeros from the first row
    if board_slice.ndim == 2:
        zero_array= list(filter(lambda x : x ==0, board_slice[0]))
    #last slice returns a 1D array
    elif board_slice.ndim == 1:
        zero_array= list(filter(lambda x : x ==0, board_slice))

    if len(zero_array) == 0:
        #exit condition for recursion - the board has fully been walked through
        if len(board_slice[:,1]) == 1:
            return 'board is definitely undecided'
        else:
            #recursion with a smaller board
            return check_whether_game_definitely_undecided(board_slice[1:,:])
    else:
        # board has still some 'unplayed' spots
        return False

# checks whether four stones are in a row. Returns String with the respective answer to the Question.
def check_game_over(board):
    number_of_columns = board.shape[1]
    number_of_rows = board.shape[0]
    # check columns for 4-in-a-row
    for j in range(0,number_of_columns):
        for i in range(0,number_of_rows-3):
            #slicing: slice out relevant subarrays of size 4
            if np.all(board[i:(i+4),j] == np.array([1,1,1,1])):
                # Strings are recognized as True
                return "player1_wins"
            if np.all(board[i:(i+4),j] == np.array([2,2,2,2])): 
                # Strings are recognized as True
                return "player2_wins"
            

    # check rows for 4-in-a-column
    for i in range(0,number_of_rows):
        for j in range(0,number_of_columns-3):
            #slicing: slice out relevant subarrays of size 4
            if np.all(board[i,j:(j+4)] == np.array([1,1,1,1])):
                # Strings are recognized as True
                return "player1_wins"
            if np.all(board[i,j:(j+4)] == np.array([2,2,2,2])): 
                # Strings are recognized as True
                return "player2_wins"
    
    # check diagonals upwards 
    for i in range(0,number_of_rows - 3):
        for j in range(0,number_of_columns - 3):
            if board[i,j] == 1 and board[i+1,j+1] == 1 and board[i+2,j+2] == 1 and board[i+3,j+3] == 1:
                # Strings are recognized as True
                return "player1_wins"
            if board[i,j] == 2 and board[i+1,j+1] == 2 and board[i+2,j+2] == 2 and board[i+3,j+3] == 2:
                # Strings are recognized as True
                return "player2_wins"

    # check diagonals downwards (but maybe a bit from an unexpected direction)
    for i in range(0,number_of_rows-3):
        for j in range(0,number_of_columns - 3):
            if board[i,j+3] == 1 and board[i+1,j+2] == 1 and board[i+2,j+1] == 1 and board[i+3,j] == 1:
                # Strings are recognized as True
                return "player1_wins"
            if board[i,j+3] == 2 and board[i+1,j+2] == 2 and board[i+2,j+1] == 2 and board[i+3,j] == 2:
                # Strings are recognized as True
                return "player2_wins"

    result=check_whether_game_definitely_undecided(board)
    if result:
        #result is in fact a result string
        result_string=result
        return result_string
    else:
        #if every game check concerning the game being over turns out to be false, the game is not over
        return False

def is_current_player_input_legitimate(current_player_input, number_of_columns):
    #check length, only one character permitted
    if(len(current_player_input) > 1):
        return False
    #check regex: a number between 1 and number_of_columns
    elif re.match(r'[1-7]', current_player_input):
        return True
    else: 
        return False


def execute_game():
    # set the board parameters like in the original game with 7 columns and 6 rows
    number_of_rows=6
    number_of_columns=7
    
    #create new board
    board = create_board(number_of_rows,number_of_columns)
    
    #randomly choose the first player to start. There's player 1 and player 2. 
    current_player=random.randint(1, 2)
    print("Welcome to the game \'Connect Four\'")
    print("----------------------------------------------------")
    print("Empty positions on the board are depicted as 0")
    print("Player 1 positions on the board are depicted as 1")
    print("Player 2 positions on the board are depicted as 2")
    print("Have fun!")
    print()

    while not check_game_over(board):
        print()
        print("Player", current_player, "\'s turn!")
        print(board)
        print("Select a column between", 1, 'and', number_of_columns, " ")
        
        #prompt the player to insert column number
        current_player_input=input("Input: ")
        
        if is_current_player_input_legitimate(current_player_input, number_of_columns):
            #input is legitimate, we interpret it as the intended column of the current player
            current_player_input_column=int(current_player_input)
            
            if does_column_has_space(board, current_player_input_column):
                board=insert_stone(board, current_player_input_column, current_player)
                # change the current_player 
                if current_player==1:
                    current_player=2
                else:
                    current_player=1
            else:
                print("Column is already full! - Try again inserting into another column!")
                continue
        else:
            print("Input hasn\'t been properly recognized. Try again writing a number between", 
                  1, "and", number_of_columns, "!")
            continue 
    print()
    print(check_game_over(board))
    print(board)

