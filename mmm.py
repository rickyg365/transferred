import os
import sys

import time
import random


""" 
Program: Matrix
Author: rickyg3
Date: 03/08/2021
"""


class Matrix:
    def __init__(self, rows=1, cols=1):
        # Size (mxn)
        self.m = rows
        self.n = cols
        self.size = (self.m, self.n)

        # Length of the longest element
        self.max_char_length = 0

        # Create Matrix
        self.matrix = []
        self.update(self.m, self.n)

    def __str__(self):
        # Top Line
        line = '\n'  # ".-     -.\n"
        # In Between
        for row in self.matrix:
            # line += '| '
            for item in row:
                line += f" {item}" + (self.max_char_length - (len(f"{item}"))) * ' '
            line += '\n'
            line += '\n'  # '|\n'
        # Footer
        # line += "'-     -'"
        return line

    def __add__(self, other):
        # Add the add function here
        # Assuming both matrices have exact same dimensions
        new_m = []

        # Flatten 1st Matrix
        m1 = self.flatten(self)
        # Flatten 2nd Matrix
        m2 = self.flatten(other)

        # Total number of entries
        l = len(m1)

        # Displaying (Can comment this out to not print the addition)
        rower = []
        c = 0
        for si in range(self.m):
            row = ""
            for ci in range(self.n):
                row += f" ({m1[c]} + {m2[c]}) "
                c += 1
            rower.append(row)

        # Printing
        for row in rower:
            print(row)
            print('\n')

        # Creating new flattened matrix by adding entries
        for i in range(l):
            new_m.append(m1[i] + m2[i])

        # Create new matrix object and set size
        new_matrix = Matrix(self.m, self.n)

        # Set values of matrix using new flattened matrix
        new_matrix.set_matrix(new_m)

        return new_matrix

    def flatten(self, matrix_list):
        data = []

        y = matrix_list.m  # Height or num of rows (m)
        x = matrix_list.n  # Length or num of cols (n)

        for i in range(y):
            for j in range(x):
                data.append(matrix_list.matrix[i][j])

        return data

    def set_matrix(self, flattened_matrix):
        count = 0
        for num_row in range(self.m):
            for num_cols in range(self.n):
                self.matrix[num_row][num_cols] = flattened_matrix[count]
                count += 1

    def update(self, size_m, size_n):
        count = 1

        for size_m in range(self.m):
            # Row
            row = []
            for size_n in range(self.n):
                # Column
                row.append(count)
                count += 1
            self.matrix.append(row)

        # Finds the length of the longest element
        current_max = self.max_char_length
        for r in self.matrix:
            for item in r:
                char_length = len(f"{item}")
                if char_length > current_max:
                    current_max = char_length
                else:
                    pass
        # plus 1 so theres an extra space between entries
        self.max_char_length = current_max + 1

    def identity(self):
        # transforms the matrix into the identity matrix
        # Instead of having to loop through a 2d list each time to update lets try having one list data
        # with the entries in order but flattened
        for i in range(self.m):
            for j in range(self.n):
                if i == j:
                    self.matrix[i][j] = 1
                else:
                    self.matrix[i][j] = 0

    # def add(self, matrix_obj):
    #     m1 = self.flatten(self)
    #     m2 = self.flatten(matrix_obj)
    #     new_m = []
    #
    #     l = len(m1)
    #
    #     # displaying
    #     rower = []
    #     c = 0
    #     for si in range(self.m):
    #         row = ""
    #         for ci in range(self.n):
    #
    #             row += f" ({m1[c]} + {m2[c]}) "
    #             c += 1
    #         rower.append(row)
    #
    #     for row in rower:
    #         print(row)
    #         print('\n')
    #
    #     #
    #     for i in range(l):
    #         new_m.append(m1[i] + m2[i])
    #
    #     self.set_matrix(new_m)


m = Matrix(3, 3)
k = Matrix(3, 3)
m.identity()


# print(m.matrix)
print(m)

print(k)

# k.add(m)
newest = k + m
print(newest)