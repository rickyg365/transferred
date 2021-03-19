# !/bin/python/
import os
import sys

import json
import random
import time

"""
.-------.
| Goals |
'-------'

Using text file
________________________________________
    Example.txt
        .------------------------------.
        |fline1                        |  
        |fline2                        |  
        |fline3                        |  
        |...                           |  
        |+ # front/back seperator      |          
        |bline1                        |  
        |bline2                        |  
        |bline3                        |  
        |...                           |  
        |@ # Flash card separater      |
        |...                           |  
        '------------------------------'
     - set_data(filename) method
        
        
Using json file
________________________________________
    - Need Dump/load method
    - Need add and remove method
    - 
        
                                      
    
    - Change Card Title to an ID variable to be able to call on specific cards
    
    - Randomize cycle Order
    
    - Instead of using a text file and this weird format try doing a version where we use a json file 

"""


def clear_screen():
    os.system("clear")


def text_wrap(raw_text):
    """ Wraps text in
    .-------------------------------------------.
    |                                           |
    |                  line1                    |    # 45 char: 2 |, 2 " ", 42 text [2 ' ', line z, x * ' '
    |                  line2                    |
    |                  line3                    |
    |                  line4                    |
    |                  line5                    |
    |                  line6                    |
    |                                           |
    '-------------------------------------------'
    * limit of 6 lines of text... for now...

    To Use: # print(text_wrap(t))
    """
    # Variables
    output_array = []

    # Loop through lines (up to 6)
    for i in range(6):
        # Variables
        line = raw_text[i]

        # Makes sure line doesnt exceed flash card
        if len(line) > 40:
            line = line[0:40]

        text = line.ljust(40)
        new_line = f"|   {text} |"
        output_array.append(new_line)

    # Consolidate output array
    output_text = f".{44*'-'}.\n|{44*' '}|\n"

    # Join formatted output text into a single string : array -> str
    output_text += '\n'.join(output_array)

    output_text += f"\n|{44*' '}|\n'{44*'-'}'"

    return output_text


t = [
    'Title: Line 1',
    '   Guess who\'s that pokemon!',
    'line 3',
    ' line 4',
    '  line 5',
    '   It\'s Pikachu'
]

g = ['line 1: back', 'line 2: back', 'line 3: back', 'line 4: back', 'line 5: back'.center(38), 'line 6: back']


class Card:
    """
    Card Object to store individual flash cards

    To Use: # c = Card('Pokemon', t, s)
    """
    def __init__(self, id_num, front_data, back_data):
        self.id = id_num

        # Takes data in array form and uses textwrap func. to create flash card string
        self.front = text_wrap(front_data)
        self.back = text_wrap(back_data)

        # dict keeps track of which face is showing
        self.current_view = {'front': True, 'back': False}
        # Could just use 1 variable, True means front, False means back...

    def __str__(self):
        # Adds right justified ID above card
        identity = f"ID# {self.id}"
        txt = f"{identity.rjust(46)}\n"

        # Check current view
        if self.current_view['front']:
            txt += self.front
        elif self.current_view['back']:
            txt += self.back
        else:
            print("something went wrong card.__str__")

        return txt

    def flip(self):
        # Checks current view and flips states
        if self.current_view['front']:
            self.current_view['front'] = False
            self.current_view['back'] = True
        elif self.current_view['back']:
            self.current_view['front'] = True
            self.current_view['back'] = False
        else:
            print("something weird happened card.flip")
        # A single T/F variable would get rid of this


class StudyCards:
    def __init__(self, group_name):
        self.group_name = group_name
        self.card_list = []

        # TBI
        self.current = None
        self.next = None
        self.previous = None

    def __str__(self):
        # txt = ""
        txt = f"Group: {self.group_name}"
        for c in self.card_list:
            # txt += f"\n{c.title}"
            txt += f"\n"
            txt += f"\nFront:\n{c.front}"
            txt += f"\nBack:\n{c.back}"

        return txt

    def add_card(self, card_id, front, back):
        self.card_list.append(Card(card_id, front, back))

    def set_data(self, filename):
        # Using Text File
        id_num = 1
        with open(filename, 'r+') as f:
            new_obj = []
            card_data = []
            for line in f:
                # print(line)
                if line.strip() == '+':
                    card_data.append(new_obj)
                    new_obj = []
                elif line.strip() == '@':
                    card_data.append(new_obj)
                    current_id = f"00{id_num}"
                    new_card = Card(current_id, card_data[0], card_data[1])
                    self.card_list.append(new_card)

                    id_num += 1
                    new_obj = []
                    card_data = []
                else:
                    l = line.replace('\n' , '')
                    new_obj.append(f"{l}")

    def cycle(self):
        flip_choices = 'fF yY'
        not_flip = 'nN'

        for card in self.card_list:
            menu = True

            while menu:
                clear_screen()
                print(f"{self.group_name}:\n")
                print(card)

                u = input(">>> ")

                # Version 2
                if u in flip_choices:
                    card.flip()
                elif u in not_flip:
                    menu = False
                else:
                    print("Input Error")
                    time.sleep(1)


s = StudyCards('Sample')
# s.add_card('Card Title', t, g)
# s.add_card('Card Title2', t, g)
s.add_card('Card Title3', t, g)
s.set_data('sample_flash.txt')
s.cycle()
# clear_screen()
# print(s)

# menu = True
#
# while menu:
#     os.system("cls")
#     print(c)
#
#     u = input(">>> ")
#
#     flip_choices = 'fF yY'
#     not_flip = 'nN'
#
#     # Version 1
#     # if u.upper() == 'Y' or u == '':
#     #     c.flip()
#     # elif u.upper() == 'N':
#     #     pass
#     #     menu = False
#
#     # Version 2
#     if u in flip_choices:
#         c.flip()
#     elif u in not_flip:
#         menu = False
#     else:
#         print("Input Error")


"""
Combine this with database.
maybe make a container, look at container.py
"""
