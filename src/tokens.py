
from enum import Enum, auto #import Enumeration package for tokens
import re #Import re for regular expresions (prevents hardcoding tokens)

class Tokens(Enum): #Base Tokens Class extends Enum
    pass

class Types(Enum):#Base Types Class extends Enum
    pass

class Keywords(Tokens):
    LET = auto()
    FOR = auto()
    DO = auto()
    WHILE = auto()
    LOOP = auto()
    END = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()

class Type(Types):
    DataType = auto()
    Syntax = auto()
    MathOperator = auto()
    BoolOperator = auto()

class DataType(Tokens):
    D_BOOL = auto()
    D_FLOAT = auto()
    D_INT = auto()

class Syntax(Tokens):
    GET = auto()
    NAME = auto()
    P_LEFT = auto()
    P_RIGHT = auto()
    
class MathOperator(Tokens):
    M_ADD = auto()
    M_SUB = auto()
    M_MUL = auto()
    M_DIV = auto()
    
class BoolOperator(Tokens):
    B_GREATER = auto()
    B_NOT_GREATER = auto()
    B_LESS = auto()
    B_NOT_LESS = auto()
    B_EQL = auto()

    
