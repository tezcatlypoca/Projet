from Lexer import Lexer

lexer = Lexer()

def test_should_get_basic_token():
    generator = lexer.lexer("{}")
    
    assert next(generator) == ("OPEN_BRACE", '{')
    assert next(generator) == ("CLOSE_BRACE", '}')
# END FUNCTION

def test_should_get_basic_token():
    generator = lexer.lexer("{\"key\": \"value\"")
    
    assert next(generator) == ("OPEN_BRACE", "{")
    assert next(generator) == ("STRING", "key")
    assert next(generator) == ("COLON", ":")
    assert next(generator) == ("STRING", "value")
    assert next(generator) == ("CLOSE_BRACE", "}")
# END FUNCTION