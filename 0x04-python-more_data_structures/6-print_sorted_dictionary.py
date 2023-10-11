#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for x in range(len(matrix[a])):
            if x != 0:
                print(" ", end='')
            print("{:d}".format(matrix[a][x]), end='')
        print()
