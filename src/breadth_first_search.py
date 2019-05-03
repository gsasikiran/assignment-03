#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:15:04 2018

@author: Iswariya Manivannan
"""
import sys
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes
from helper import start_pose, print_maze, clear_screen
import time


def breadth_first_search(maze_map):
    """Function to implement the BFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : [type]
        [description]
    start_pos : [type]
        [description]
    goal_pos : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """


    start = start_pose(maze_map)
    iterable = maze_map_to_tree(maze_map)

    # queue = deque([(iterable, start)])

    # Fill in your BFS algorithm here
    fringe = [start]
    visited = []

    fringe.extend(iterable[start])

    while fringe:
        # print(fringe)
        parent_node = fringe.pop(0)
        # print(fringe)
        for child_node in iterable[parent_node]:
            if child_node not in visited and maze_map[parent_node[0]][parent_node[1]] != '=' and maze_map[parent_node[0]][parent_node[1]]!= '|':
                new_map = assign_character_for_nodes(maze_map, child_node, parent_node)
                print_maze(new_map)
                fringe.append(child_node)
                visited.append(child_node)
    return new_map





if __name__ == '__main__':

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()


    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()

    breadth_first_search(maze_map_map2)


    # CALL THIS FUNCTIONS after filling in the necessary implementations
    # path_map1 = breadth_first_search(maze_map_map1)
    # write_to_file("bdf_map1", path_map1)

    # path_map2 = breadth_first_search(maze_map_map2)
    # write_to_file("bdf_map2", path_map2)

    # path_map3 = breadth_first_search(maze_map_map3)
    # write_to_file("bdf_map3", path_map3)
