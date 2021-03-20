""" Tentei adicionar "try" e "execpt" para não aceitar strings mas não consegui encontrar uma solução """

from funcs import *

userlist = []

def list_size_input(input):
    """ accepts an integer and set the list size"""
    try:
        size = int(input)                                  #checks if size is a int
    except TypeError:
        size = int(input('Must be a number!: '))           #asks again the user for an int
        

### User input - list size ###
size = int(input('Choose a list size: '))
list_size_input(size)


### User inputs - int for the list ###
while len(userlist) < size:
    try:
        x = int(input('Choose a number for the list: '))    #user input
        userlist.append(x)                                  #appends to userlist
    except ValueError:
        x = int(input('Must be a number!: '))               #asks again the user for an int


### Functions ###
list_big_number(userlist)

delete_small_num(userlist)
