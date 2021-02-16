
# Class:       CS 4308 Section 2
# Term:        Spring 2021
# Name:        Raleigh Barden, James Rivett, Barrett Calhoun
# Instructor:   Deepa Muralidhar
# Project:  Deliverable 1 Scanner - Python

# Key Terms from:
# https://documentation.help/FreeBASIC/CatPgFullIndex.html

from enum import Enum, auto #import Enumeration package for TokenType
import re #Import re for regular expresions (prevents hardcoding TokenType)

class TokenType(Enum): #Base TokenType Class extends Enum
    pass

class Keywords(TokenType): #Basic Keywords
    LET = auto()
    DO = auto()
    FOR = auto()
    WHILE = auto()
    LOOP = auto()
    END = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    PRINT = auto()

class Literal(TokenType): # Type for Identifiers like: float, int, bool, str, and variables
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    
class MathOperator(TokenType): # Type for mathmatic operators
    M_ADD = auto()
    M_SUB = auto()
    M_MUL = auto()
    M_DIV = auto()
    
class BoolOperator(TokenType): # Type for Boolean Operators
    B_GREATER = auto()
    B_GREATER_EQUAL = auto()
    B_LESS = auto()
    B_LESS_EQUAL = auto()
    B_EQL_EQL = auto()

class Delimiters(TokenType):
    EOL = auto()
    EOF = auto()

class Other(TokenType): # Type for syntax TokenType like: "(", ")", "="
    EQL = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()

    
