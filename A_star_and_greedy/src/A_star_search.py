#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:39:47 2018

@author: iswariya
"""

import sys
import timeit
from heapq import *
from Queue import PriorityQueue
from helper import *


def Astar_search(board, opt):
    """Function to implement the A-star search algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : [object]
        [includes the puzzle configurations and methods]
    opt : [int]
        [command line argument]

    Returns
    -------
    [printing puzzle]
        [puzzle configurations from initial state to goal]
    """

    priority_queue = []
    f_score = 0  # evaluation function value
    g_score = 0  # cost function value
    h_score = 0  # heuristic function value
    Steps = 0
    # Creating a heap from list to store the nodes with the priority h_score
    heappush(priority_queue, (f_score, g_score, h_score, board.get_initial_state()))

    # FILL IN YOUR CODE HERE
    explored_nodes = list([])
    initialstate = board.get_initial_state()
    goalstate = board.get_goal_state()
    if board.goal_test(initialstate):
        return initialstate

    while not board.goal_test(initialstate):
        searchnode = heappop(priority_queue)

        possible_moves = get_possible_moves(initialstate)
        for i in possible_moves:
            if not board.is_explored(i):
                if opt == 1:
                    h_score = get_manhattan_distance(i)
                elif opt == 2:
                    h_score = no_of_misplaced_tiles(i)
                else:
                    print("please provide a valid argument")
                    break

                f_score = h_score + g_score
                heappush(priority_queue, (f_score,g_score,h_score,i))
                priority_queue.sort(key=lambda tup: tup[1])

                board.explored_states.append(i)
            
        
        Steps += 1
        g_score += 1
        initialstate = priority_queue[0][3]
        print_puzzle(initialstate)
        # print(" {0} | {1} | {2} \n {3} | {4} | {5}\n {6} | {7} | {8} \n ----------".format(initialstate[0],initialstate[1],initialstate[2],initialstate[3],initialstate[4],initialstate[5],initialstate[6],initialstate[7],initialstate[8]))
        print('steps :',Steps)
        print('explored nodes:',len(board.explored_states))


    return 


if __name__ == '__main__':       
    # puzzle_8 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
    # puzzle_8 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
    puzzle_8 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing

    print("Initial Configuration")
    board = Puzzle(puzzle_8)
    print_puzzle(puzzle_8)
    opt = int(sys.argv[1])

    if opt == 1 or opt == 2:

        if opt ==1:
            print("\nRunning A star search with Manhattan Dist heuristic\n")
        else:
            print("\nRunning A star search with Misplaced Tiles heuristic\n")

        start_time = timeit.default_timer()
        Astar_search(board, opt)
        end_time = timeit.default_timer()
        print('Time: {}s'.format(end_time-start_time))
    else:
        print("Invalid Choice")
