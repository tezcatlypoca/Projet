from Blinder import Blinder
import os

blinder = Blinder()

# get a path
# browse file and encrypt him
# return true if all goes well
def test_should_encrypt_file():
    assert blinder.obfuscate(["Test_files\\2encrypt_test.txt"]) == (True,)
    
    os.remove("Test_files\\2encrypt_test.txt_bl")
    
    with open("Test_files\\2encrypt_test.txt", 'w', encoding='utf-8') as file:
        file.write('Bonjour Comment allez-vous ?\nJe vais bien ')
# END FUNCTION
    
# get severals paths
# browse them and encrypt the corresponding file
# return tuple of bool
def test_should_encrypt_files():
    paths = ["Test_files\\2encrypt_test.txt", "Test_files\\2encrypt_test2.txt"]
    assert blinder.obfuscate(paths) == (True, True)
    
    os.remove("Test_files\\2encrypt_test.txt_bl")
    os.remove("Test_files\\2encrypt_test2.txt_bl")
    
    with open("Test_files\\2encrypt_test.txt", 'w', encoding='utf-8') as file:
        file.write('Bonjour Comment allez-vous ?\nJe vais bien ')
        
    with open("Test_files\\2encrypt_test2.txt", 'w', encoding='utf-8') as file:
        file.write('Je teste si tout fonctionne bien\n\nBon après ca devrait le faire, non ?!')
# END FUNCTION

# get a path
# browse file and decrypt him
# return true if all goes well
def test_should_decrypt_file():
    assert blinder.clarify(["Test_files\\2decrypt_test.txt_bl"]) == (True,)
    
    os.remove("Test_files\\2decrypt_test.txt")
    
    with open("Test_files\\2decrypt_test.txt_bl", 'w', encoding='utf-8') as file:
        file.write('Ö©•ù©æ§ Ð©µµ%•ß !èè%ÿ-ø©æ¥ ?✽♦% ø!é¥ @é%• ')
# END FUNCTION
    
# get severals paths
# browse them and decrypt the corresponding file
# return tuple of bool
def test_should_decrypt_files():
    paths = ["Test_files\\2decrypt_test.txt_bl", "Test_files\\2decrypt_test2.txt_bl"]
    for file in paths:
        assert blinder.clarify(file) == (True, True)
    
    os.remove("Test_files\\2decrypt_test.txt")
    os.remove("Test_files\\2decrypt_test2.txt")
    
    with open("Test_files\\2decrypt_test.txt_bl", 'w', encoding='utf-8') as file:
        file.write('Ö©•ù©æ§ Ð©µµ%•ß !èè%ÿ-ø©æ¥ ?✽♦% ø!é¥ @é%• ')
        
    with open("Test_files\\2decrypt_test2.txt_bl", 'w', encoding='utf-8') as file:
        file.write('Ö©•ù©æ§ Ð©µµ%•ß !èè%ÿ-ø©æ¥ ?✽♦% ø!é¥ @é%• Ö©•ù©æ§ Ð©µµ%•ß !èè%ÿ-ø©æ¥ ?✽♦% ø!é¥ @é%• ')
# END FUNCTION