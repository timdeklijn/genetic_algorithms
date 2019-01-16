"""Traveling Salesman setup

"""

__author__ = "Tim de Klijn"

import sys
import random
import numpy as np
import argparse
import itertools
import time
from typing import Tuple, List
import matplotlib.pyplot as plt

location = Tuple[float, float]
route_list = List[int]

N_LOCATIONS = 7
WIDTH = 10
HEIGHT = 10


def random_locations() -> List[location]:
    """Create a list of locations withing WIDTH and HEIGHT"""
    location_list: List[location] = []
    for i in range(N_LOCATIONS):
        l: location = (
            # i,
            WIDTH * np.random.random_sample(),
            HEIGHT * np.random.random_sample()
            )
        location_list.append(l)
    return location_list


def plot_route(location_list: List[location], 
               route: route_list) -> None:
    """Plot locations + route"""
    x = [i[0] for i in location_list]
    y = [i[1] for i in location_list]

    # Plot locations
    plt.scatter(x, y)

    # Plot lines between points
    for i in range(len(route)-1):

        x1, x2 = x[route[i]], x[route[i+1]]
        y1, y2 = y[route[i]], y[route[i+1]]

        plt.plot([x1, x2], [y1, y2])

    # show plot
    plt.show()


def location_distance(l1: location, l2: location) -> float:
    """Return the cartesian distance between locations"""
    return (np.linalg.norm(np.array(l2) - np.array(l1)))
    

def calc_distance(location_list: List[location], 
                  route: route_list) -> float:
    """Calculate total distance of route"""
    acc = 0
    for i in range(len(route)-1):
        acc += location_distance(
            location_list[route[i]],
            location_list[route[i+1]])
    return acc


def generate_random_route() -> route_list:
    """Create a random route based on N_LOCATIONS"""

    # Create random sequence lists
    options = list(range(N_LOCATIONS))
    random.shuffle(options)

    return options + [options[0]]


def main() -> None:

    parser = argparse.ArgumentParser(
        description="{}".format("Traveling Salesman framework")
    )

    parser.add_argument("--random", 
        action = "store_true",
        help = "Show example")
    parser.add_argument("--brute", 
        action = "store_true",
        help = "Do bruteforce method")
    parser.add_argument("--genetic", 
        action = "store_true",
        help = "Do genetic algorithm")

    args = parser.parse_args()

    # Locations to visit
    location_list = random_locations()

    if args.random:

    #########################
    #                       #
    # Plot locations        #
    # Generate random route #
    # Plot random route     #
    # print route distance  #
    #                       #
    #########################

        print("Showing traveling salesman example")

        random_route = generate_random_route()
        plot_route(location_list, random_route)
        route_distance = calc_distance(
            location_list, 
            random_route
            )
        print(f"Route distance: {route_distance}")

    if args.brute:

    ######################################
    #                                    #
    # Time the operation                 #
    # Create initial route               #
    # Set a high min distance            #
    # Loop over permutations             #
    # Calculate distance                 #
    # Save route and distance if shorter #
    # Print results                      #
    #                                    #
    ######################################

        print("Bruteforcing the answer")

        t_start = time.time()

        route = list(range(N_LOCATIONS))
        min_distance = 1e6

        for route in itertools.permutations(route):
            # Always append start to route
            route = list(route) + [route[0]]
            route_distance = calc_distance(
                location_list, 
                route
            )
            # Save if distance is shorte
            if route_distance < min_distance:
                shortest_route = route
                min_distance = route_distance

        # print results
        print(f"Shortest distance: {min_distance}")
        print(f"Route: {shortest_route}")
        print(f"Time: {time.time()-t_start}")

        plot_route(location_list, shortest_route)


    if args.genetic:

        print("Performing genetic algorithm")

        t_start = time.time()

    ########################################
    #                                      #
    # IMPLEMENT YOUR GENETIC ALGORITH HERE #
    #                                      #
    ########################################

        print(f"Time: {time.time()-t_start}")

if __name__ == "__main__":
    main()