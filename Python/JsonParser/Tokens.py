import re

class Tokens:
    
    def __init__(self):
        self.init_tokens()
        self.init_regex()
    # END FUNCTION
    
    def init_tokens(self) -> None:
        self.TOKEN_OPEN_BRACE = 'OPEN_BRACE'
        self.TOKEN_CLOSE_BRACE = 'CLOSE_BRACE'
        self.TOKEN_OPEN_BRACKET = 'OPEN_BRACKET'
        self.TOKEN_CLOSE_BRACKET = 'CLOSE_BRACKET'
        self.TOKEN_COLON = 'COLON'
        self.TOKEN_COMA = 'COMA'
        
        self.TOKEN_NULL = 'NULL'
        self.TOKEN_TRUE = 'TRUE'
        self.TOKEN_FALSE = 'FALSE'
        
        self.TOKEN_INTEGER = 'INTEGER'
        self.TOKEN_STRING = 'STRING'
        
    def init_regex(self) -> None:
        self.REGEX_OPEN_BRACE = re.compile(r'{')
        self.REGEX_CLOSE_BRACE = re.compile(r'}')
        self.REGEX_OPEN_BRACKET = re.compile(r'\[')
        self.REGEX_CLOSE_BRACKET = re.compile(r']')
        self.REGEX_COLON = re.compile(r':')
        self.REGEX_COMA = re.compile(r',')
        
        self.REGEX_NULL = re.compile(r'\bnull\b')
        self.REGEX_TRUE = re.compile(r'\bTrue\b')
        self.REGEX_FALSE = re.compile(r'\bFalse\b')
        
        self.REGEX_INTEGER = re.compile(r'\b\d+\b')
        self.REGEX_STRING = re.compile(r'^"([^"]+)"')
    
    def get_open_brace(self) -> str:
        return self.TOKEN_OPEN_BRACE
    
    def get_close_brace(self) -> str:
        return self.TOKEN_CLOSE_BRACE
    
    def get_open_bracket(self) -> str:
        return self.TOKEN_OPEN_BRACKET
    
    def get_close_bracket(self) -> str:
        return self.TOKEN_CLOSE_BRACKET
    
    def get_colon(self) -> str:
        return self.TOKEN_COLON
    
    def get_coma(self) -> str:
        return self.TOKEN_COMA
    
    def get_null(self) -> str:
        return self.TOKEN_NULL
    
    def get_true(self) -> str:
        return self.TOKEN_TRUE
    
    def get_false(self) -> str:
        return self.TOKEN_FALSE
    
    def get_integer(self) -> str:
        return self.TOKEN_INTEGER
    
    def get_string(self) -> str:
        return self.TOKEN_STRING
    
# END CLASS