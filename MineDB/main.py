from .basicCommands import BasicCommands
from cryptography.fernet import Fernet
import json
import os
class MineDB(BasicCommands):
    version = "1.1v"
    existing_db={"sample":{"data":{"version":"1.1v","developer":"hrs_developers"}}}
    __path = os.path.join(os.getcwd(), "MineDB", "secure.dat")
    __key = None
    __cipher = None

    def __init__(self):
        print(f"MineDB - version - {self.version}")
        try:
            #if dbfile and key already created
            with open(os.path.join(os.getcwd(), "MineDB", "MineDBKey.key"),"rb") as f:
                self.__key = f.read()
            self.__cipher = Fernet(self.__key) 

        except(FileNotFoundError):
            #if dbfile and key nots created
            self.__key = Fernet.generate_key()
            with open(os.path.join(os.getcwd(), "MineDB", "MineDBKey.key"),"wb") as f:
                f.write(self.__key)
            self.__cipher = Fernet(self.__key)
            print("\nMineDB : Setup is ready")
            self.save()

        encrypted_data = ""
        with open(self.__path,"rb") as f:
            encrypted_data = f.read()
        
        decrypted_data = self.__cipher.decrypt(encrypted_data)
        self.existing_db = json.loads(decrypted_data)    

    def save(self):
        json_data = json.dumps(self.existing_db).encode()
        encrypted_data = self.__cipher.encrypt(json_data)
        with open(self.__path,"wb") as f:
            f.write(encrypted_data)
        
        print("\nMineDB : Save Successfully")