from Tokens import Tokens
from icecream import ic

class Lexer():
    
    def __init__(self):
        self.tokens = Tokens()
        
    def lexer(self, data: str):
        pos = 0
        
        while pos < len(data):
            if data[pos] == ' ':
                pos += 1
                continue
            elif match := self.tokens.REGEX_OPEN_BRACE.match(data, pos):
                value = match.group()
                ic(data[pos])
                yield (self.tokens.get_open_brace(), value)
                pos = match.end()
                continue
            elif match := self.tokens.REGEX_CLOSE_BRACE.match(data, pos):
                value = match.group()
                ic(data[pos])
                yield (self.tokens.get_close_brace(), value)
                pos = match.end()
                continue
            elif match := self.tokens.REGEX_STRING.match(data, pos):
                value = match.group()
                ic(data[pos])
                yield (self.tokens.get_string(), value)
                pos = match.end()
                continue
            elif match := self.tokens.REGEX_COLON.match(data, pos):
                value = match.group()
                ic(data[pos])
                yield (self.tokens.get_colon(), value)
                pos = match.end()
                continue
            
            raise ValueError(f"Caractère non reconnu à la position {pos}: '{data[pos]}'")
    # END FUNCTION