import os
import sys

import time
import random


""" 
Program: Matrix
Author: rickyg3
Date: 03/08/2021
"""


def clear_screen():
    os.system("clear")


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

        # Store flattened data for easier access?
        self.flat_matrix = []

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
        # Inititalize list of new flattened data
        data = []

        y = matrix_list.m  # Height or num of rows (m)
        x = matrix_list.n  # Length or num of cols (n)

        # Iterate through matrix and append to new list
        for i in range(y):
            for j in range(x):
                data.append(matrix_list.matrix[i][j])

        return data

    def set_matrix(self, flattened_matrix):
        # Tracker, used to map flattened matrix to regular matrix using already established dimensions
        count = 0
        for num_row in range(self.m):
            for num_cols in range(self.n):
                self.matrix[num_row][num_cols] = flattened_matrix[count]
                count += 1

    def update(self, size_m, size_n):
        # Tracker var used to assign default values to each spot of the matrix
        count = 1

        # Create Matrix
        for size_m in range(self.m):
            row = []
            for size_n in range(self.n):
                row.append(count)
                count += 1
            self.matrix.append(row)

        # Finds the length of the longest element (uses current max as reference)
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
        # Transforms the matrix into the identity matrix
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


if __name__ == "__main__":
    def parse_size(raw_input):
        valid_sep = ['x', ' ', '.', ',']
        split_input = []

        for char in raw_input:
            if char in valid_sep:
                split_input = raw_input.split(char)

        new_output = []
        for item in split_input:
            new_output.append(int(item))

        return new_output


    active = True

    Matrices = []
    current_matrix = []

    while active:

        # Display
        clear_screen()
        # print(37*'_')
        print(current_matrix)
        # print(37 * '_')

        action = input("\nWhat would you like to do?:\n \n [C]: Change Matrix\n [A]: Add Matrix\n [Q]: Quit\n>>> ")

        if action.upper() == 'Q' or action.upper() == 'QUIT':
            active = False
        elif action.upper() == 'C':
            new_matrix = {}
            en = 1
            for matri in Matrices:
                new_matrix[f"{en}"] = matri
                print(f"{en}:\n{matri}")
                en += 1

            change = input("\nWhich matrix would you like to use?: ")

            if change in new_matrix.keys():
                current_matrix = new_matrix[change]
            else:
                print("Something went wrong the number you input did not match any of the keys")
        elif action.upper() == 'A':
            size = input("\nWhat size matrix?: ")
            m, n = parse_size(size)

            current_matrix = Matrix(m, n)
            Matrices.append(current_matrix)

        else:
            print("Invalid Input")


m = Matrix(3, 3)
k = Matrix(3, 3)
m.identity()


# print(m.matrix)
print(m)

print(k)

# k.add(m)
newest = k + m
print(newest)
