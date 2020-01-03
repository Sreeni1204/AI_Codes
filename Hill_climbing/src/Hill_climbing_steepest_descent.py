#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018

@author: iswariya
"""
import argparse
import os
import random
import timeit

from helper import *


def hill_climb_steepest_descent(start_seq, distance_matrix):
    """ Function to implement steepest descent hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    print the results for every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    start_seq : [type]
        [description]
    distance_matrix : [type]
        [description]

    Returns
    -------
    [type]
    """

    best_cost = float('inf')
    best_seq = None
    cost = [0]
    seen_states = []
    curr_seq = start_seq
    curr_seq.append(start_seq[0])
    curr_dist = 0
    restarts_count = 0
    cost_sequence = list([])
    best_cost_list = list([]) #list to store the best costs after each 2000 iterations.

    # FILL IN YOUR CODE HERE
    dist_matrix = get_distance_matrix(coordinates) #gets the distance matrix for the cooordinates

    while restarts_count < 5:
        
        start_sequence = curr_seq
        main_dist = get_distance(dist_matrix, start_sequence) # main distance for the start sequence

        for j in range(2000):
            del cost_sequence[:]
            successors_list = get_successors(start_sequence) # gets 100 successors for the start sequence

            for sequence in successors_list:
                curr_dist = get_distance(dist_matrix, sequence) #provides the distance for each and every sequence
                cost_sequence.append((curr_dist, sequence)) #list appending of cost and sequence
            # this could also be done using the priority queue as well for getting the least value by sorting the queue
            cost_sequence.sort(key=lambda tup: tup[0]) #sorting the list to get the least cost sequence
            if cost_sequence[0][0] < main_dist: #to check for the first least cost sequence when compared to parent sequence

                best_cost = cost_sequence[0][0] #updating best cost as current distance
                best_seq = cost_sequence[0][1] #updating best sequence as current sequence
                start_sequence = cost_sequence[0][1] #changing the start sequence to current sequence
                main_dist = cost_sequence[0][0] # changing the main distance to current distance
                # cost.append(main_dist)
                
                
            cost.append(main_dist) #appending the best costs
                

            

                    #update the cost and all here


        best_cost_list.append(best_cost) #stroing the best cost after 2000 iterations                
        curr_seq = random.sample(range(0, len(list_of_cities[1:])), len(list_of_cities[1:])) #creating the random sequence
        curr_seq.append(curr_seq[0]) #creating a complete loop for travelling to all cities
        restarts_count += 1 # incrementing the restart count


                 
    plot_cost_function(cost)
    print("Best cost list:")
    print(best_cost_list)
    return best_cost, best_seq


if __name__ == '__main__':

    # Reading txt file from command line
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

    # Generating a random soln.
    random_seq = random.sample(range(0, len(list_of_cities[1:])),
                               len(list_of_cities[1:]))

    # Calculating the least dist using steepest descent hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_steepest_descent(random_seq,
                                                           coordinates)
    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Least distance from Steepest Ascent:", least_distance)
    print("Time: {}s".format(end_time-start_time))
