
# Class:       CS 4308 Section 2
# Term:        Spring 2021
# Name:        Raleigh Barden, James Rivett, Barrett Calhoun
# Instructor:   Deepa Muralidhar
# Project:  Deliverable 1 Scanner - Python

# Key Terms from:
# https://documentation.help/FreeBASIC/CatPgFullIndex.html

from enum import Enum, auto #import Enumeration package for tokens
import re #Import re for regular expresions (prevents hardcoding tokens)

class Tokens(Enum): #Base Tokens Class extends Enum
    pass

class Types(Enum):#Base Types Class extends Enum
    pass

class Keywords(Tokens): #Basic Keywords
    LET = auto()
    FOR = auto()
    DO = auto()
    WHILE = auto()
    LOOP = auto()
    END = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()

class Literal(Tokens): # Type for Identifiers like: float, int, bool, str, and variables
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    
class MathOperator(Tokens): # Type for mathmatic operators
    M_ADD = auto()
    M_SUB = auto()
    M_MUL = auto()
    M_DIV = auto()
    
class BoolOperator(Tokens): # Type for Boolean Operators
    B_GREATER = auto()
    B_GREATER_EQUAL = auto()
    B_LESS = auto()
    B_LESS_EQUAL = auto()
    B_EQL_EQL = auto()

class Other(Tokens): # Type for syntax tokens like: "(", ")", "="
    EQL = auto()
    P_LEFT = auto()
    P_RIGHT = auto()

    
