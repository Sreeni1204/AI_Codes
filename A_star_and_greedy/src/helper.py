#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:28:19 2018

@author: iswariya
"""

import copy
import math
from heapq import *

PUZZLE_TYPE = 8
ROW_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))


class Puzzle:
    """ Class for creating N puzzle game environment.
    This class has been implemented to provide a minimalistic
    game environment to you. Please try to avoid modifying this
    class unless absolutely necessary.
    """

    def __init__(self, init_state):
        """Class Construction for initializing the board

        Parameters
        ----------
        init_state : list
            Initial position of the board obtained from user
        """

        self.initial_state = init_state
        self.goal_state = [i for i in range(0, PUZZLE_TYPE + 1)]
        self.explored_states = []

    def get_goal_state(self):
        """Class method to get the goal state of the board

        Returns
        -------
        list
            Configuration of board when goal state has been reached
        """

        return self.goal_state

    def get_initial_state(self):
        """Class method to get the initial state of the board

        Returns
        -------
        list
            Initial configuration of board during start of search
        """

        return self.initial_state

    def goal_test(self, node):
        """Class method to test if goal state is reached and 
        appends the particular board configuration to the list
        of explored states. Returns true if goal state is reached.

        Parameters
        ----------
        node : list
            Board configuration obtained from the search tree

        Returns
        -------
        boolean
            Returns true if the passed configuration is equal to
            goal configuration
        """

        self.explored_states.append(node)
        return node == self.goal_state

    def is_explored(self, node):
        """Class method to check if a particular board configuration
        has already been explored

        Parameters
        ----------
        node : list
            Board configuration obtained from the search tree

        Returns
        -------
        boolean
            Returns true if a particular configuration has already been explored
        """

        return node in self.explored_states


def print_puzzle(puzzle):
    """Function to print the puzzle to console

    Parameters
    ----------
    puzzle : list
        8 puzzle configuration
    """

    for idx, val in enumerate(puzzle):

        if (idx + 1) % ROW_SIZE == 0:     
            print("  ", val)
        else:
            print("  ", val)

    return


def move_left(node):
    """Function to move one position left in 8 puzzle if possible

    Parameters
    ----------
    position : [list]
        [takes the node configuration from the possible moves as input]

    Returns
    -------
    [list]
        [based on the position of 0, it returns the node by swapping the 0 towards the left position]
    """

    node = list(node)
    i_0 = node.index(0)
    if (i_0 - 1) % 3 != 2:
        node[i_0], node[i_0 - 1] = node[i_0 - 1], node[i_0]
        return node
    else:
        return []


def move_right(node):
    """Function to move one position right in 8 puzzle if possible

    Parameters
    ----------
    position : [list]
        [takes the node configuration from the possible moves as input]

    Returns
    -------
    [list]
        [based on the position of 0, it returns the node by swapping the 0 towards the right position]
    """

    node = list(node)
    i_0 = node.index(0)
    if (i_0 + 1) % 3 != 0:
        node[i_0], node[i_0 +1] = node[i_0 + 1], node[i_0]
        return node
    else:
        return []


def move_down(node):
    """Function to move one position up in 8 puzzle if possible

    Parameters
    ----------
    position : [list]
        [takes the node configuration from the possible moves as input]

    Returns
    -------
    [list]
        [based on the position of 0, it returns the node by swapping the 0 towards the down position]
    """

    node = list(node)
    i_0 = node.index(0)
    if i_0 + 3 <= 8:
        node[i_0], node[i_0 + 3] = node[i_0 +3], node[i_0]
        return node
    else:
        return []


def move_up(node):
    """Function to move one position down in 8 puzzle if possible

    Parameters
    ----------
    position : [list]
        [takes the node configuration from the possible moves as input]

    Returns
    -------
    [list]
        [based on the position of 0, it returns the node by swapping the 0 towards the up position]
    """

    node = list(node)
    i_0 = node.index(0)
    if i_0 - 3 >= 0:
        node[i_0], node[i_0 - 3] = node[i_0 - 3], node[i_0]
        return node
    else:
        return []


def get_possible_moves(node):
    """Function to check whether a move is possible in left,
    right, up, down direction and store it.

    Parameters
    ----------
    node : [list]
        [node to check for the possible movements of 0]

    Return
    ------
    [list of lists]
        [consists of possible moves based on the 0 position]
    """

    possible_moves = []
    if move_left(node) != []:
        possible_moves.append(move_left(node))
    if move_right(node) != []:
        possible_moves.append(move_right(node))
    if move_up(node) != []:
        possible_moves.append(move_up(node))
    if move_down(node) != []:
        possible_moves.append(move_down(node))
    

    return possible_moves
    # HINT :
    # 1. Convert the list to a heap and push the possible moves
    # to the heap based on priority.
    # 2. Please note priority depends on your search algorithm
    # For Eg: A-star uses f_score as priority while greedy search
    # uses h_score as priority




def no_of_misplaced_tiles(node):
    """Function to get the number of misplaced tiles for a
    particular configuration

    Parameters
    ----------
    node : [list]
        [list to check for the heuristics]

    Return
    ------
    [int]
        [returns the heuristic distance for a particular node]
    """
    h_score = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for idx, i in enumerate(goal_state):
        if goal_state[idx] != node[idx]:
            h_score += 1
    return h_score


def misplaced_tile_heuristic(nodes, possible_moves):
    """Function to implement misplaced tiles heuristic in
    combination with no_of_misplaced_tiles() for each of
    the search algorithms

    Parameters
    ----------
    node : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """
    raise NotImplementedError

def get_manhattan_distance(node):
    """Function to calculate the manhattan distance for a
    particular configuration

    Parameters
    ----------
    node : [list]
        [list to check for the heuristics]

    Return
    ------
    [int]
        [returns the heuristic distance for a particular node]
    """
    h_score = 0
    node = list(node)
    for i in range(9):
        h_score += abs( node[i]/3 - (i%3) ) + abs( node[i] % 3 - (i/3) )

    return h_score


def manhattan_distance_heuristic(nodes, possible_moves):
    """Function to implement manhattan distance heuristic in
    combination with get_manhattan_distance() for each of
    the search algorithms

    Parameters
    ----------
    node : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """

    raise NotImplementedError
