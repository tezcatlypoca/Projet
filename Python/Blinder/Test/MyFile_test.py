from .. import MyFile
import os

myfile = MyFile.MyFile()

# read json file
# and return the dictionnary search
# raise exception if error occured
def test_should_read_json_characters():
    temp = None
    try: 
        temp = myfile.read_json("Bin\\alpha.json", "characters")
    except BaseException as e:
        print(e)
        
    assert temp['a'] == "!"
# END FUNCTION
    
def test_should_read_json_specials():
    temp = None
    try: 
        temp = myfile.read_json("Bin\\alpha.json", "specials")
    except BaseException as e:
        print(e)
        
    assert temp['!'] == "a"
# END FUNCTION
    
# read any type of files
# return the content to be encrypt or decrypt
# raise exception if error occured
def test_should_read_data():
    temp = None
    try:
        temp = myfile.read_data("Test_files\\basic.txt")
    except BaseException as e:
        print(e)
        
    assert temp == "Bonjour comment ca va\naujourd'hui ?"
# END FUNCTION
    
# write data on file
# return True or False
# raise exception if error occured
def test_should_write_data():
    temp = None
    try:
        print("test")
        temp = myfile.write_data("Test_files\\write_test.txt", "coucou")
    except BaseException as e:
        print(e)
        
    assert temp == True
# END FUNCTION

# rename the file opened for encrypt/decrypt
# return the new name with path
def test_should_rename_file_encrypt():
    temp = None
    with open("Test_files\\rename_test.txt", "w", encoding='utf-8') as file:
        file.write('')
        
    try:
        temp = myfile.rename("Test_files\\rename_test.txt")
    except BaseException as e:
        print(e)
        
    assert temp == "Test_files\\rename_test.txt_bl"
# END FUNCTION

def test_should_rename_file_decrypt():
    temp = None
        
    try:
        temp = myfile.rename("Test_files\\rename_test.txt_bl")
    except BaseException as e:
        print(e)
        
    assert temp == "Test_files\\rename_test.txt"
    os.remove("Test_files\\rename_test.txt")
# END FUNCTION