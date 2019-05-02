#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 01:36:01 2018

@author: Iswariya Manivannan
"""

import sys
import os
import time


def maze_map_to_tree(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : list
        The list of the text

    Returns
    -------
    dict_tree :dictionary
        The keys of the dictionary are a tuple (row,col) representing the parent node.
        The values are the list of tuples (row,col) representing the corresponding children nodes.
        The list starts with the left node and ends at down node travelling clockwise
    """
    dict_tree = {}
    for row in range(0, len(maze_map)):
        for col in range(0, len(maze_map[row])):

            if maze_map[row][col] == ' ' or 's':
                left = (row, col - 1)
                right = (row, col + 1)
                up = (row - 1, col)
                down = (row + 1, col)
                dict_tree.update({(row, col): [left, up, right, down]})

    return dict_tree


def assign_character_for_nodes(maze_map, current_node, prev_node):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    maze_map : [type]
        [description]
    current_node : [type]
        [description]
    prev_node : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """



    raise NotImplementedError


def write_to_file(file_name, path):
    """Function to write output to console and a txt file.
    Please ensure that it should ALSO be possible to visualize each and every
    step of the tree traversal algorithm in the map in the console.
    This enables understanding towards the working of your
    tree traversal algorithm as to how it reaches the goals.

    Parameters
    ----------
    filen_name : string
        This parameter defines the name of the txt file.
    path : [type]
        [description]

    """

    raise NotImplementedError

def start_pose(maze_map):
    '''

    :param maze_map: list
            The list of the text
    :return: tuple
            The tuple (row,col) where the source is present
    '''
    for row in range(0,len(maze_map)):
        for col in range(0, len(maze_map[row])):
            if maze_map[row][col] == 's':
                 return (row,col)
