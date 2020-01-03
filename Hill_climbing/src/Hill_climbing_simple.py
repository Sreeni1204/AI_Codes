#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018

@author: iswariya/sreenivasa
"""

import argparse
import random
import timeit
import os
from helper import *


def hill_climb_simple(start_seq, coordinates):
    """ Function to implement simple hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    randomly restarting at every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    start_seq : [list]
        [random list of cities]
    coordinates : [list of lists]
        [coordinates of the cities]

    Returns
    -------
    [best_cost]
        [total distance for the best sequence]
    [best_seq]
        [best sequence with least cost]
    """

    best_cost = float('inf')
    best_seq = None
    cost = [0]
    seen_states = []
    curr_seq = start_seq
    curr_seq.append(start_seq[0])
    curr_dist = 0
    restarts_count = 0
    best_cost_list = list([]) #list to store the best costs after each 2000 iterations.

    # FILL IN YOUR CODE HERE
    dist_matrix = get_distance_matrix(coordinates) #gets the distance matrix for the cooordinates

    while restarts_count < 5:
        
        start_sequence = curr_seq
        main_dist = get_distance(dist_matrix, start_sequence) # main distance for the start sequence

        for j in range(2000):

            successors_list = get_successors(start_sequence) # gets 100 successors for the start sequence

            for sequence in successors_list:
                curr_dist = get_distance(dist_matrix, sequence) #provides the distance for each and every sequence
                if curr_dist < main_dist: #to check for the first least cost sequence when compared to parent sequence

                    best_cost = curr_dist #updating best cost as current distance
                    best_seq = sequence #updating best sequence as current sequence
                    start_sequence = sequence #changing the start sequence to current sequence
                    main_dist = curr_dist # changing the main distance to current distance
                    # cost.append(main_dist)
                    break #breaking the loop as soon as the best sequence is found
                
            cost.append(main_dist) #appending the best costs

        best_cost_list.append(best_cost) #stroing the best cost after 2000 iterations    
        curr_seq = random.sample(range(0, len(list_of_cities[1:])), len(list_of_cities[1:])) #creating the random sequence
        curr_seq.append(curr_seq[0]) #creating a complete loop for travelling to all cities
        restarts_count += 1 # incrementing the restart count


                 
    plot_cost_function(cost) #calling function for plotting the best costs
    print("Best cost list:")
    print(best_cost_list)
    return best_cost, best_seq


if __name__ == '__main__':

    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    # Getting the list of cities and their coordinates
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]

    # Generating a random intial sequence
    random_start_seq = random.sample(range(0, len(list_of_cities[1:])),
                                     len(list_of_cities[1:]))

    # Calculating the least dist using simple hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_simple(random_start_seq,
                                                 coordinates)
    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Least distance from Simple hill climbing:", least_distance)
    print("Time: {}".format(end_time - start_time))
