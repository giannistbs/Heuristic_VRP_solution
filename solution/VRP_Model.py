import random
import math


class Model:

# instance variables
    def __init__(self):
        self.allNodes = []
        self.capacity = -1
        self.empty_vehicle_weight = -1
        self.customers = []
        self.matrix = []

    def load_model(self, file_name):
        all_nodes = []
        all_lines = list(open(file_name, "r"))

        separator = ','

        line_counter = 0

        ln = all_lines[line_counter]
        no_spaces = ln.split(sep=separator)
        capacity = int(no_spaces[1])

        line_counter += 1
        ln = all_lines[line_counter]
        no_spaces = ln.split(sep=separator)
        empty_vehicle_weight = int(no_spaces[1])

        line_counter += 1
        ln = all_lines[line_counter]
        no_spaces = ln.split(sep=separator)
        tot_customers = int(no_spaces[1])

        line_counter += 3
        ln = all_lines[line_counter]

        no_spaces = ln.split(sep=separator)
        x = float(no_spaces[1])
        y = float(no_spaces[2])
        depot = Node(0, x, y)
        all_nodes.append(depot)

        for i in range(tot_customers):
            line_counter += 1
            ln = all_lines[line_counter]
            no_spaces = ln.split(sep=separator)
            idd = int(no_spaces[0])
            x = float(no_spaces[1])
            y = float(no_spaces[2])
            demand = float(no_spaces[3])
            customer = Node(idd, x, y, demand)
            all_nodes.append(customer)

        rows = len(all_nodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0, len(all_nodes)):
            for j in range(0, len(all_nodes)):
                a = all_nodes[i]
                b = all_nodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist

        self.allNodes = all_nodes[:]
        self.customers = all_nodes[1:] # !
        self.capacity = capacity
        self.empty_vehicle_weight = empty_vehicle_weight


class Node:
    def __init__(self, idd, xx, yy, dem=0):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.demand = dem
        self.isRouted = False

class Route:
    def __init__(self, dp, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        self.sequenceOfNodes.append(dp)
        self.cost = 0
        self.capacity = cap
        self.load = 0