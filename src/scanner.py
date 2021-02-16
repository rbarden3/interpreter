
# Class:       CS 4308 Section 2
# Term:        Spring 2021
# Name:        Raleigh Barden, James Rivett, Barrett Calhoun
# Instructor:   Deepa Muralidhar
# Project:  Deliverable 1 Scanner - Python

import re              # import re to match regx
from tokens import *   # import the basic subset to be used

class Token:
        # Constructor for token class
        def __init__(self, type: TokenType, lexeme: str, pos: tuple):
            self.type = type
            self.lexeme = lexeme
            self.pos = pos
        
        # Returns Token as a string
        def __str__(self):
            return f"Line: {self.pos[0]}, Column: {self.pos[1]}, Token: {self.type}, Lexemme: {repr(self.lexeme)}"


class ScannerError(Exception):
    def __init__(self, pos: tuple):
        self.pos = pos

    def __str__(self):
        return f"ScannerError: Unknown lexeme at Ln:{self.pos[0]} Col:{self.pos[1]}"

class Scanner:
    def __init__(self, source_file):
        self.source_file = source_file

    def match(self, group):
        match = None
        for regex, type in group:
            match=regex.match(self.line, self.pos)
            if match:
                token = Token(type, match.group(0), (self.line_num+1, self.pos+1))
                self.pos = match.end()
                return token
        if not match:
            raise ScannerError((self.line_num+1, self.pos+1))

    def lex(self):
        for self.line_num, self.line in enumerate(self.source):
            self.pos = 0
            while self.pos < len(self.line):
                ws = WS_SKIP.search(self.liune, self.pos)
                if ws:
                    self.pos = ws.start()
                else:
                    yield self.match(TOKEN_TYPES)
        yield Token(Delimiters.EOF,"/Z", (self.line_num+1, self.pos+1))