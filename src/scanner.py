
# Class:       CS 4308 Section 2
# Term:        Spring 2021
# Name:        Raleigh Barden, James Rivett, Barrett Calhoun
# Instructor:   Deepa Muralidhar
# Project:  Deliverable 1 Scanner - Python

import re              # import re to match regx
from tokens import *   # import the basic subset to be used

class Token:

        # Constructor for token class
        def __init__(self, type: Tokens, lexeme: str, pos: tuple):
            self.type = type
            self.lexeme = lexeme
            self.pos = pos
        
        # Returns Token as a string
        def __str__(self):
            str_form = ("Line: {:<3} Column: {:<4} Token: {:<30} Lexemme: {:<20}")
            return str_form.format(self.pos[0], self.pos[1], self.type, repr(self.lexeme))


class ScannerError(Exception):
    def __init__(self, pos: tuple):
        self.pos = pos
