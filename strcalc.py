#!/usr/bin/env python3

SCRABBLE_VAL = {
    "A": 1, "E": 1, "I": 1, "L": 1, "N": 1, "O": 1, "R": 1, "S": 1, "T": 1, "U": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10,
}

def scrabble_val(arg: str) -> int:
    tot = 0
    arg = arg.upper()
    for char in arg:
        tot += SCRABBLE_VAL.get(char, 0)
    return tot

def ord_val(arg: str, zero_based: bool = False):
    tot = 0
    arg = arg.upper()
    for char in arg:
        if zero_based:
            tot += ord(char) - 65
        else:
            tot += ord(char) - 64
    return tot

PHONE_VAL = {
    "A": 2, "B": 2, "C": 2,
    "D": 3, "E": 3, "F": 3,
    "G": 4, "H": 4, "I": 4,
    "J": 5, "K": 5, "L": 5,
    "M": 6, "N": 6, "O": 6,
    "P": 7, "Q": 7, "R": 7, "S": 7,
    "T": 8, "U": 8, "V": 8,
    "W": 9, "X": 9, "Y": 9, "Z": 9,
}

def phone_val(arg: str):
    tot = 0
    arg = arg.upper()
    for char in arg:
        tot += PHONE_VAL.get(char, 0)
    return tot

