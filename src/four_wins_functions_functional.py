#! /usr/local/opt/python/bin/python3.8


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


# essentially gives back the transformed 2D board (with the inserted value) in the form of a 1D array.
# functional! Unfortunately not KISS
def give_recursively_back_one_d_array_with_one_replaced_number(board, one_d_array, current_row, current_column, rows, columns, insert_row_0_indexed, insert_column_0_indexed, to_be_inserted):
    # fundamental decision: what gets inserted into the new _to be array new_one_d_array?
    if current_column == insert_column_0_indexed and current_row == insert_row_0_indexed:
        #push on a new number
        new_one_d_array=np.append(one_d_array, to_be_inserted)
    else:
        #push on a new number
        new_one_d_array=np.append(one_d_array, board[current_row][current_column])

    # walking one step further through the board now..
     # walked till the end of the row?
    if current_column + 1 == columns:
        # are you at the lower end of the matrix? - then you can't walk any further
        if current_row +1 ==  rows:
            return new_one_d_array 
        else:
            #only set the new variables in calling the new function. Because: functional
            # go one row down (rows are in the first dimension)
            return give_recursively_back_one_d_array_with_one_replaced_number(board, new_one_d_array, current_row+1, 0, rows, columns, insert_row_0_indexed, insert_column_0_indexed, to_be_inserted)
    else:
        #only set the new variables in calling the new function. Because: functional
        # just walk down the board one column further
        return give_recursively_back_one_d_array_with_one_replaced_number(board, new_one_d_array, current_row, current_column + 1, rows, columns, insert_row_0_indexed, insert_column_0_indexed, to_be_inserted)


# Preparation and postpreparation function for give_recursively_back_one_d_array_with_one_replaced_number(..) 
# functional!
# essentially returns a new 2D board with to_be_inserted at the right place for the (old board and the indexes and the to_be_inserted)
def give_back_new_board_with_one_replaced_number(board, insert_row_0_indexed, insert_column_0_indexed, to_be_inserted):
    rows=board.shape[0]
    columns=board.shape[1]
    # trick: 2D to 1D in order to get functional
    one_d_array=np.zeros(0, dtype=np.int8)
    # we need to call the recursive function with the walking variable current_column (instantiated with 0)
    # as well as a one_d_array --- a 1D data structure that allows push and pop (in contrast to 2D data structures)
    new_one_d_array=give_recursively_back_one_d_array_with_one_replaced_number(board, one_d_array, 0, 0, rows, columns, insert_row_0_indexed, insert_column_0_indexed,  to_be_inserted)
    return new_one_d_array.reshape(board.shape[0], board.shape[1])



# 3 values are possible on the board / matrix:
# 0 - nothing played here yet
# 1 - Player 1 has set a stone here
# 2 - Player 2 has set a stone here 
def insert_stone(board, current_player_input_column, current_player):
    # user indexing to 0-indexing of matrices
    selected_column_zero_indexed=one_to_zero_indexing(current_player_input_column)
    
    #slice out the column array
    selected_column_array = board[:,selected_column_zero_indexed]
    
    #find empty slot
    empty_slot_zero_indexed = np.max(np.where(selected_column_array == 0))

    # functional! - analogue to board[empty_slot_zero_indexed][selected_column_zero_indexed]=current_player
    # I tend to say: this is not KISS!
    return give_back_new_board_with_one_replaced_number(board, empty_slot_zero_indexed, selected_column_zero_indexed, current_player)


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
            print('board is definitely undecided')
            return True
        else:
            #recursion with a smaller board
            return check_whether_game_definitely_undecided(board_slice[1:,:])
    else:
        # board has still some 'unplayed' spots
        return False

def are_there_consecutive_four_in_a_line(line):
    if len(line) >3:
        #are the first 4 entries the same? and if they are: are they entries of either player 1 or player 2?
        player_1=1
        player_2=2
        if line[0] == line[1] and line[1] == line[2] and line[2] == line[3] \
            and (line[0] == player_1 or line[0] == player_2):
            #Congrat messages
            print()
            print('------------------------------')
            if line[0] == player_1:
                print('Player 1 wins, congrats :)') 
            else: 
                print('Player 2 wins, congrats :)') 
            print('------------------------------')
            return True
        else:
            return are_there_consecutive_four_in_a_line(line[1:])
    else:
        return False 

# functional! -> recursion
def are_there_consecutive_four_horizontally(board_slice):
    if board_slice.shape[0] > 0:
        line= list(board_slice[0])
        if are_there_consecutive_four_in_a_line(line):
            return True
        else:
            return are_there_consecutive_four_horizontally(board_slice[1:])
    else:
        return False

# functional
def are_there_consecutive_four_vertically(board):
    #reuse code: transpose matrix and use the _horizontally function:
    return are_there_consecutive_four_horizontally(np.transpose(board))

def recursive_diagonal_upper_left_to_lower_right_line_checker(board,i):
    #abortion, if the diagonal plane is just empty
    if board.diagonal(i).shape[0]==0: 
        return False
    else:  
        if are_there_consecutive_four_in_a_line(board.diagonal(i)):
            return True
        else: 
            return recursive_diagonal_upper_left_to_lower_right_line_checker(board,i+1)

def are_there_four_diagonal_upper_left_to_lower_right(board):
    # starting point is negative, because we want to s
    start_int_recursive_line_checker= - len(board[:,0]) + 1
    return recursive_diagonal_upper_left_to_lower_right_line_checker(board,start_int_recursive_line_checker)

def are_there_four_diagonal_lower_left_to_upper_right(board):
    #mirroring the board at the horizontal, middle axis, one can use the
    # are_there_four_diagonal_upper_left_to_lower_right - function 
    # (please visualize it graphically for you)
    return are_there_four_diagonal_upper_left_to_lower_right(np.flip(board,axis=0))

def is_game_over(board):
    return are_there_four_diagonal_upper_left_to_lower_right(board) \
        or are_there_four_diagonal_lower_left_to_upper_right(board) \
        or are_there_consecutive_four_horizontally(board) \
        or are_there_consecutive_four_vertically(board) \
        or check_whether_game_definitely_undecided(board)
    
   
def is_current_player_input_legitimate(current_player_input, number_of_columns):
    #check length, only one character permitted
    if(len(current_player_input) > 1):
        return False
    #check regex: a number between 1 and number_of_columns
    elif re.match(r'[1-7]', current_player_input):
        return True
    else: 
        return False

# This is a recursive function that checks whether the game is over and runs a new round of the game if the game is not yet over
# Otherwise it prints the winning board
def recursive_new_round(board,current_player):
    
    if not is_game_over(board):
        number_of_columns = board.shape[1]
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
                new_board=insert_stone(board, current_player_input_column, current_player)
                # change the current_player 
                if current_player==1:
                    new_current_player=2
                else:
                    new_current_player=1
                recursive_new_round(new_board,new_current_player)
            else:
                print("Column is already full! - Try again inserting into another column!")
                recursive_new_round(board,current_player)
        else:
            print("Input hasn\'t been properly recognized. Try again!")
            recursive_new_round(board,current_player)
    else:
        print("Winning board:")
        print(board)

    

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
    recursive_new_round(board,current_player)
