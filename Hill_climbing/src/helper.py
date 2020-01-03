#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:49:06 2018

@author: Sreenivasa
"""
import copy
import math
import random
import matplotlib.pyplot as plt


def plot_cost_function(cost):
    """ Function to plot the no. of iterations (x-axis) vs
    cost (y-axis). X-axis of the plot should contain xticks
    from 0 to 10000 in steps of 2000.
    Use matplotlib.pyplot to generate the plot as .png file and store it
    in the results folder. An example plot is
    there in the results folder.

    Parameters
    ----------
    cost : [list]
        [list of costs]
    """
    plt.title("Distance VS Number of iterations")
    plt.xlabel("Number of iterations")
    plt.ylabel("Distance")
    plt.plot(cost)
    plt.show()


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any cities. Please note that the first and last city
    should remain unchanged since the traveller starts and ends in
    the same city.

    Parameters
    ----------
    curr_seq : [list]
        [list of cities]

    Returns
    -------
    [list of list]
        [list of list of random cities]
    """
    successor_list = list([])
    A = 0  #index variable for swapping
    B = 0 #index variable for swapping
    copy_list = list([])
    for i in range(100):
        copy_list = curr_seq[:]
        A = random.randint(1, len(curr_seq) - 2) 
        B = random.randint(1, len(curr_seq) - 2)

        sequence = swap(copy_list, A, B)
        successor_list.append(sequence)

    return successor_list
    


def get_distance(distance_matrix, seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.
    HINT : Keep adding the distances between the cities in the
    sequence by referring the distances from the distance matrix

    Parameters
    ----------
    distance_matrix : [matrix]
        [matrix of euclidien distance for each cities]
    seq : [list]
        [list of cities]

    Returns
    -------
    [float]
        [total distance from start city to end city]
    """

    total_distance = 0
    seq_length = len(seq)
    for i in range(seq_length):
        j = (i + 1)%seq_length

        I = seq[i]
        J = seq[j]

        total_distance += distance_matrix[I][J]

    return total_distance


def get_distance_matrix(coordinates):
    """ Function to generate a distance matrix. The distance matrix
    is a square matrix.
    For eg: If there are 3 cities then the distance
    matrix has 3 rows and 3 colums, with each city representing a row
    and a column. Each element of the matrix represents the euclidean
    distance between the coordinates of the cities. Thus, the diagonal
    elements will be zero (because it is the distance between the same city).

    Parameters
    ----------
    coordinates : [list of list]
        [has the coordinates of the cities]

    Returns
    -------
    [matrix]
        [matrix of euclidien distance for each cities]
    """

    a, b = 0, 0

    EC_Dist_matrix = [[0 for x in range(len(coordinates))] for y in range(len(coordinates))]
    for idx, (x1, y1) in enumerate(coordinates):
        a = (float(x1), float(y1))
        for jdx, (x2, y2) in enumerate(coordinates):
            b = (float(x2), float(y2))
            ec_dist = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            EC_Dist_matrix[idx][jdx] = ec_dist
            
    # print (EC_Dist_matrix)
    return EC_Dist_matrix


def swap(seq, i, j):
    '''function to swap the two random cities of the sequence based on the i and j value '''
    seq[i], seq[j] = seq[j], seq[i]

    return seq
