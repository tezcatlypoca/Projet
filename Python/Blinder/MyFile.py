from icecream import ic
import json, os

class MyFile:
    
    def read_json(self, path, search):
        if not os.path.exists(path):
            raise BaseException({"Code:": "-001", "message": "File does not exist", "File": f"{path}"})
        elif os.path.getsize(path) == 0:
            raise BaseException({"Code:": "-002", "message": "File is empty."})
        
        with open(path, "r", encoding='utf-8') as file:
                parsed_json =json.load(file)[search]
                return parsed_json
    # END FUCNTION
    
    def read_data(self, path):
        if not os.path.exists(path):
            raise BaseException({"Code:": "-001", "message": "File does not exist", "File": f"{path}"})
        elif os.path.getsize(path) == 0:
            raise BaseException({"Code:": "-002", "message": "File is empty."})
        
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    # END FUNCTION
    
    def write_data(self, path, data):
        if not os.path.exists(path):
            raise BaseException({"Code:": "-001", "message": "File does not exist", "File": f"{path}"})
        elif os.path.getsize(path) == 0:
            raise BaseException({"Code:": "-002", "message": "File is empty."})
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)
            return True
    # END FUNCTION
    
    def rename(self, path):
        if '_bl' in path:
            os.rename(path, path[0: len(path)-3])
            return path[0: len(path)-3]
        new_path = path + '_bl' 
        os.rename(path, new_path)
        return  new_path  
# END CLASS
    