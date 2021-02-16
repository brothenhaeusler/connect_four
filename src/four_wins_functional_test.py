#! /usr/local/opt/python/bin/python3.8

from four_wins_functions_functional import (
create_board,
is_game_over,
check_whether_game_definitely_undecided, 
is_current_player_input_legitimate, 
does_column_has_space, 
one_to_zero_indexing,
insert_stone,
walk_through_pitch_replace_one_number
)
import numpy as np

def test_walk_through_pitch_replace_one_number():
    rows=7
    columns=4
    board = np.ones((rows,columns),dtype=np.int8)
    insert_row_0_indexed = rows-2
    insert_column_0_indexed= columns-3 
    to_be_inserted=97
    assert to_be_inserted == walk_through_pitch_replace_one_number(board, insert_row_0_indexed, insert_column_0_indexed, to_be_inserted)[insert_row_0_indexed][insert_column_0_indexed]

    #test 2
    rows_0=9
    columns_0=5
    board_0 = np.ones((rows_0,columns_0),dtype=np.int8)
    insert_row_0_indexed_0 = rows-3
    insert_column_0_indexed_0= columns-2
    to_be_inserted_0=94
    assert to_be_inserted_0 == walk_through_pitch_replace_one_number(board_0, insert_row_0_indexed_0, insert_column_0_indexed_0, to_be_inserted_0)[insert_row_0_indexed_0][insert_column_0_indexed_0]

    rows_1=5
    columns_1=9
    board_1 = np.ones((rows_1,columns_1),dtype=np.int8)
    insert_row_0_indexed_1 = rows-4
    insert_column_0_indexed_1= columns-3 
    to_be_inserted_1=64
    assert to_be_inserted_1 == walk_through_pitch_replace_one_number(board_1, insert_row_0_indexed_1, insert_column_0_indexed_1, to_be_inserted_1)[insert_row_0_indexed_1][insert_column_0_indexed_1]

    rows_2=6
    columns_2=7
    board_2 = np.ones((rows_2,columns_2),dtype=np.int8)
    insert_row_0_indexed_2 = rows-4
    insert_column_0_indexed_2= columns-2
    to_be_inserted_2=42
    assert to_be_inserted_2 == walk_through_pitch_replace_one_number(board_2, insert_row_0_indexed_2, insert_column_0_indexed_2, to_be_inserted_2)[insert_row_0_indexed_2][insert_column_0_indexed_2]


def test_check_whether_game_definitely_undecided():
    #test 1:
    rows=7
    columns=4
    board = np.ones((rows,columns),dtype=np.int8)
    assert bool(check_whether_game_definitely_undecided(board))
    # test 2:
    rows=5
    columns=3
    # create a board with a 'random' space being 0
    board = np.ones((rows,columns),dtype=np.int8)
    board[rows-1, columns-1]=0
    assert not check_whether_game_definitely_undecided(board)

def test_is_game_over():
    # Tests to check whether is_game_over function works
    #test1: no entries
    rows=6
    columns=7
    board = create_board(rows,columns)
    assert not is_game_over(board)

    # test 2: horizontal line
    rows_board_1=7
    columns_board_1=9
    board_1 = create_board(rows_board_1,columns_board_1)

    board_1[0,1] = 1
    board_1[0,2] = 1
    board_1[0,3] = 1
    board_1[0,4] = 1
    assert is_game_over(board_1)

    #test 3: vertical line
    rows_board_2=4
    columns_board_2=8
    board_2 = create_board(rows_board_2,columns_board_2)

    board_2[0,0] = 2
    board_2[1,0] = 2
    board_2[2,0] = 2
    board_2[3,0] = 2
    assert is_game_over(board_2)

    #test 4: diagonal_upper_left_to_lower_right
    rows_board_3=5
    columns_board_3=8
    board_3 = create_board(rows_board_3,columns_board_3)

    board_3[1,1] = 1
    board_3[2,2] = 1
    board_3[3,3] = 1 
    board_3[4,4] = 1
    assert is_game_over(board_3)

    #test 5: diagonal_lower_left_to_upper_right
    rows_board_4=6
    columns_board_4=8
    board_4 = create_board(rows_board_4,columns_board_4)

    board_4[0,3] = 2
    board_4[1,2] = 2
    board_4[2,1] = 2
    board_4[3,0] = 2
    assert is_game_over(board_4)

    #test 6: vertical line at the edge
    rows_board_5=4
    columns_board_5=8
    board_5 = create_board(rows_board_5,columns_board_5)

    board_5[0,columns_board_5 -1] = 2
    board_5[1,columns_board_5 -1] = 2
    board_5[2,columns_board_5 -1] = 2
    board_5[3,columns_board_5 -1] = 2
    assert is_game_over(board_5)

    # test 7: horizontal line at the edge
    rows_board_6=7
    columns_board_6=9
    board_6 = create_board(rows_board_6,columns_board_6)

    board_6[rows_board_6 -1,1] = 1
    board_6[rows_board_6 -1,2] = 1
    board_6[rows_board_6 -1,3] = 1
    board_6[rows_board_6 -1,4] = 1
    assert is_game_over(board_6)

def test_is_current_player_input_legitimate():
    #test 1
    player_input_1='927s'
    number_of_columns_1=4
    assert not is_current_player_input_legitimate(player_input_1,number_of_columns_1)
    #test 2
    player_input_2='3'
    number_of_columns_2=7
    assert is_current_player_input_legitimate(player_input_2,number_of_columns_2)

def test_does_column_has_space():
    board = create_board(5,5)
    # column 0 is full
    current_column_userinput_1=1
    board[:,one_to_zero_indexing(current_column_userinput_1)] = 1
    assert does_column_has_space(board,current_column_userinput_1) == False
    # column 2 is empty
    current_column_userinput_2=2
    assert does_column_has_space(board,current_column_userinput_2)

def test_insert_stone():
    # check whether insert function works - test visually: 
    rows=4
    columns=9
    board = create_board(rows,columns)
    # insert stone for player 1 in column 2
    column_input_1=2
    current_player_1=1

    board = insert_stone(board,column_input_1,current_player_1)
    column_number_1=one_to_zero_indexing(column_input_1)
    row_number_1=one_to_zero_indexing(rows)
    assert board[row_number_1][column_number_1]==current_player_1
    #visual test 1
    #board
    # insert stone for player 2 in column 0
    column_input_2=1
    current_player_2=2
    board = insert_stone(board,column_input_2,current_player_2)
    column_number_2=one_to_zero_indexing(column_input_2)
    row_number_2=one_to_zero_indexing(rows)
    assert board[row_number_2][column_number_2]==current_player_2
    #visual test 2
    #board

#visual test:
'''
def test_create_board():
    # as the original board with 7 columns and 6 rows
    number_of_rows=6
    number_of_columns=7
    board = create_board(number_of_rows, number_of_columns)
    #asserting doesn't seem to make too much sense here. So: visual verification:
    board
'''
