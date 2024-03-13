from MyFile import MyFile
from icecream import ic

class Blinder:
    
    myfile = None
    characters = None
    specials = None
    
    def __init__(self):
        self.myfile = MyFile()
        self.characters = self.myfile.read_json("Bin\\alpha.json", "characters")
        self.specials = self.myfile.read_json("Bin\\alpha.json", "specials")
        
    # get table of paths
    # encrypt each of them
    def obfuscate(self, file):
        encrypted_data = ''
        resultat = tuple()
        
        data = self.myfile.read_data(file)
        for char in data:
            if char in self.characters.keys():
                encrypted_data += self.characters[char]
            else:
                encrypted_data += char
                
        self.myfile.write_data(file, encrypted_data)
        self.myfile.rename(file)
        resultat = resultat + (True,)
        
        return resultat
    # END FUNCTION
    
    # get table of paths
    # decrypt each of them
    def clarify(self, file):
        decrypted_data = ''
        resultat = tuple()
        
        data = self.myfile.read_data(file)
        
        for char in data:
            if char in self.specials.keys():
                decrypted_data += self.specials[char]
            else:
                decrypted_data += char
        
        self.myfile.write_data(file, decrypted_data)
        self.myfile.rename(file)
        resultat = resultat + (True,)
        
        return resultat
    # END FUNCTION
    
# END CLASS