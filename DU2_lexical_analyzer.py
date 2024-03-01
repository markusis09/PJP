from enum import Enum


class TokenType(Enum):
    IDENTIFIER = 0
    NUMBER = 1
    OPERATOR = 2
    DELIMITER = 3
    KEYWORDS = 4
    EOF = 5

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
class Scanner:
    def __init__(self, input):
        self.input = input
        self.current = 0

    def next_token(self):
        #leng = len(self.input)
        #tmp = self.input[self.current]
        if self.current >= len(self.input) -1:
            return Token(TokenType.EOF, '')
        next = self.input[self.current + 1]
        self.current += 1
        while next == ' ':
            next = self.input[self.current + 1]
            self.current += 1
        if next in ['+', '-', '*', '/']:
            if next == '/' and self.input[self.current + 1] == '/':
                while self.input[self.current + 2] != '\n':
                    self.current += 1
                return self.next_token()
            return Token(TokenType.OPERATOR, next)
        elif next in ['(', ')', ';']:
            return Token(TokenType.DELIMITER, next)
        elif next.isdigit():
            number = int(next)
            while self.input[self.current + 1].isdigit():    
                number = number * 10 + int(self.input[self.current + 1])
                self.current += 1
            return Token(TokenType.NUMBER, number)
        elif self.input[self.current:self.current + 3] in ['div', 'mod']:
            self.current += 2
            return Token(TokenType.KEYWORDS, self.input[self.current - 2:self.current +1])
        elif next.isalpha():
            identifier = next
            while self.input[self.current + 1] != ' ':
                identifier += self.input[self.current + 1]
                self.current += 1
            return Token(TokenType.IDENTIFIER, identifier)    
        elif next == '\n':
            self.current += 1
            return self.next_token()

input = open('tokens.txt', 'r').read()

scanner = Scanner(input)
token = scanner.next_token()
while(token.type != TokenType.EOF):
    print(str(TokenType(token.type).name) + ':' + str(token.value))
    if(token.type == TokenType.EOF):
        break
    token = scanner.next_token()