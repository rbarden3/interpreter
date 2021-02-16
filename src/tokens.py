
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

    
TOKEN_TYPES = ( # Match Keywords using Regex
    (re.compile(r'LET', re.IGNORECASE), Keywords.LET),
    (re.compile(r'DO', re.IGNORECASE), Keywords.DO),
    (re.compile(r'FOR', re.IGNORECASE), Keywords.FOR),
    (re.compile(r'WHILE', re.IGNORECASE), Keywords.WHILE),
    (re.compile(r'LOOP', re.IGNORECASE), Keywords.LOOP),
    (re.compile(r'END', re.IGNORECASE), Keywords.END),
    (re.compile(r'IF', re.IGNORECASE), Keywords.IF),
    (re.compile(r'THEN', re.IGNORECASE), Keywords.THEN),
    (re.compile(r'ELSE', re.IGNORECASE), Keywords.ELSE),
    (re.compile(r'PRINT', re.IGNORECASE), Keywords.PRINT),
    
    (re.compile(r'\".*\"', re.IGNORECASE), Literal.STRING),
    (re.compile(r'(\d+\.?\d*)|(\.?\d)', re.IGNORECASE), Literal.NUMBER),

    (re.compile(r'\+', re.IGNORECASE), MathOperator.M_ADD),
    (re.compile(r'\-', re.IGNORECASE), MathOperator.M_SUB),
    (re.compile(r'\*', re.IGNORECASE), MathOperator.M_MUL),
    (re.compile(r'\/', re.IGNORECASE), MathOperator.M_DIV),
    
    (re.compile(r'>', re.IGNORECASE), BoolOperator.B_GREATER),
    (re.compile(r'>=', re.IGNORECASE), BoolOperator.B_GREATER_EQUAL),
    (re.compile(r'<', re.IGNORECASE), BoolOperator.B_LESS),
    (re.compile(r'<=', re.IGNORECASE), BoolOperator.B_LESS_EQUAL),
    (re.compile(r'==', re.IGNORECASE), BoolOperator.B_EQL_EQL),
    
    (re.compile(r'\n', re.IGNORECASE), Delimiters.EOL),
    
    (re.compile(r'=', re.IGNORECASE), Other.EQL),
    (re.compile(r'\(', re.IGNORECASE), Other.LEFT_PAREN),
    (re.compile(r'\)', re.IGNORECASE), Other.RIGHT_PAREN),
    
    # identifiers added at the end to prevent catching other tokens
    (re.compile(r'[A-Za-z0-9_]{1,31}'), Literal.IDENTIFIER)
)
# Skip Whitespaces
WS_SKIP = re.compile(r"\s")