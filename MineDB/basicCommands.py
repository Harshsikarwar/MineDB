class BasicCommands:

    def __checkIns(self, value=[], source=None):
        for v in value:
            if v == None:
                continue
            if not isinstance(v, str):
                print(f"\nError : valueError : {source} : Value should be string")
                return False
        return  True

#database commands

    def createDB(self,dbName:str):
        if not self.__checkIns([dbName], "createDB"):
            return
        try:
            checkName = dbName.isidentifier()
            if checkName == False:
                print("\nError : createDB : Invalid identifier")
                return
            elif dbName in self.existing_db:
                print("\nError : createDB : Database is already exists")
            else:
                self.existing_db[dbName]={}
                print("\nMineDB : Database created")
        except(AttributeError, TypeError, ValueError):
            print("Error : CreateDB : All parameters should be string")

    def showDB(self,dbName:str=None):
        if not self.__checkIns([dbName], "showDB"):
            return
        try:
            print("\ndatabases : ")
            if dbName != None:
                if dbName in self.existing_db:
                    print(f"{dbName} exist")
                else:
                    print("\nError : showDB : Database not exist")
            else:
                print("| ",end="")
                for db in self.existing_db.keys(): 
                    print(db, end=" | ")
                print()
        except(AttributeError, TypeError, ValueError):
            print("\nError : showDB : All parameters should be string")
    
    def dropDB(self,dbName:str):
        if dbName == "sample":
            print("MineDB : sample database is not dropable")
            return
        if not self.__checkIns([dbName], "dropDB"):
            return
        try:
            if dbName in self.existing_db:
                self.existing_db.pop(dbName)
            else:
                print("\nError : dropDB : Database not exist")
        except(AttributeError, TypeError, ValueError):
            print("Error : dropDB : All parameters should be string")
    
    def renameDB(self, dbName:str, newName:str):
        if not self.__checkIns([dbName, newName], "renameDB"):
            return
        if dbName == "sample":
            print("MineDB : sample database is not renameable")
            return
        try:
            tempDB = {}
            if dbName in self.existing_db:
                checkName = newName.isidentifier()
                if checkName == True:
                    for key, value in self.existing_db.items():
                        if key == dbName:
                            tempDB[newName] = value
                        else:
                            tempDB[key]=value
                    self.existing_db = tempDB
                    print("\nMineDB : renameDB : Database name changed")
                else:
                    print("\nError : renameDB : Invalid identifier")
            else:
                print("\nError : renameDB : Database not exist")
                return
        except(AttributeError, TypeError, ValueError):
            print("Error : renameDB : All parameters should be string")

#collection commands

    def createCollection(self,dbName:str,colName:str,**kwargs):
        if not self.__checkIns([dbName, colName], "createCollection"):
            return
        try:
            if dbName in self.existing_db:
                checkName = colName.isidentifier()
                if colName in self.existing_db[dbName]:
                    print("\nError : createCollection : Collection is already exists")
                    return
                if checkName == True:
                    temp = {}
                    for key, value in kwargs.items():
                        if(key.isidentifier()):
                            if(value in ["text", "int", "float", "bool", "chr"]):
                                temp[key]={"dataType" : value, "items" : []}
                            else:
                                print(f"\nError : createCollection : invalid data type it should be : {["text", "int", "float", "bool", "chr"]}")
                                return
                        else:
                            print("\nError : createCollection : Invalid Identifier Of Attribute")
                            return
                    self.existing_db[dbName][colName]=temp
                    print("\nMineDB : Collection created")
                else:
                    print("\nError : createCollection : Invalid Identifier")
                    return
            else:
                print("\nError : createCollection : Database not exist")
                return
        except(AttributeError, TypeError, ValueError):
            print("Error : createCollection : All parameters should be string")

    def showCollection(self,dbName:str,colName=None):
        if not self.__checkIns([dbName,colName],"showCollection"):
            return
        try:
            if dbName in self.existing_db:
                if colName != None:
                    if colName in self.existing_db[dbName]:
                        print(f"\ncollection of {dbName} : {colName}",)
                        for value in self.existing_db[dbName][colName]:
                            print(f"{value} : {self.existing_db[dbName][colName][value]["dataType"]}")  
                    else:
                        print("\nError : showCollection : Collection not exist")
                        return
                else:
                    print(f"\ncollections of {dbName} :",)
                    for col in self.existing_db[dbName]:
                        print(col, end=" ")
            else:
                print("\nError : showCollection : Database not exist")
        except(AttributeError, TypeError, ValueError):
            print("Error : showCollection : All parameters should be string")
    
    def dropCollection(self, dbName:str, colName:str):
        if not self.__checkIns([dbName,colName], "dropCollection"):
            return -1
        try:
            if dbName in self.existing_db:
                if colName in self.existing_db[dbName]:
                    self.existing_db[dbName].pop(colName)
                else:
                    print("\nError : dropCollection : Collection not exist")
                    return
            else:
                print("\nError : dropCollection : Database not exist")
        except(AttributeError, TypeError, ValueError):
            print("Error : dropCollection : All parameters should be string")
    
    def renameCollection(self, dbName:str, colName:str, newName:str):
        if not self.__checkIns([dbName, colName, newName], "renameCollection"):
            return
        try:
            tempCol = {}
            if dbName in self.existing_db:
                if colName in self.existing_db[dbName]:
                    checkName = newName.isidentifier()
                    if checkName == True:
                        for key, value in self.existing_db[dbName].items():
                            if key == colName:
                                tempCol[newName] = value
                            else:
                                tempCol[key]=value
                        self.existing_db[dbName] = tempCol
                        print("\nMineDB : renameCollection : Collection name changed")
                    else:
                        print("\nError : renameCollection : Invalid identifier")
                        return
                else:
                    print("\nError : renameCollection : Collection not exist")
                    return
            else:
                print("\nError : renameCollection : Database not exist")
                return
        except(AttributeError, TypeError, ValueError):
            print("Error : renameCollection : All parameters should be string")

 #Alter Commands

    def alterFieldType(self, dbName:str, colName:str, fieldName:str, dataType:str):
        if not self.__checkIns([dbName, colName, fieldName, dataType], "alterFieldType"):
            return
        try:
            if dbName in self.existing_db:
                if colName in  self.existing_db[dbName]:
                    if fieldName in self.existing_db[dbName][colName]:
                        if(dataType in ["text", "int", "float", "bool", "chr"]):
                                self.existing_db[dbName][colName][fieldName]["dataType"] = dataType
                                print(f"\nMineDB : alterFiledType : {fieldName} data Type changed")
                        else:
                            print(f"\nError : alterFiledType : invalid data type it should be : {["text", "int", "float", "bool", "chr"]}")
                            return
                    else:
                        print("\nError : alterFieldType : Field not exist")
                        return
                else:
                    print("\nError : alterFieldType : Collection not exist")
                    return
            else:
                print("\nError : alterFieldType : Database not exist")
                return
        except(AttributeError, TypeError, ValueError):
            print("Error : alterFieldType : All parameters should be string")
    
    def alterFieldName(self, dbName:str, colName:str, fieldName:str, newName:str):
        if not self.__checkIns([dbName,colName,fieldName,newName], "alterFieldName"):
            return
        try:
            if dbName in self.existing_db:
                if colName in  self.existing_db[dbName]:
                    if fieldName in self.existing_db[dbName][colName]:
                        tempFiled = {}
                        checkName = newName.isidentifier()
                        if checkName == True:
                            for key, value in self.existing_db[dbName][colName].items():
                                if key == fieldName:
                                    tempFiled[newName] = value
                                else:
                                    tempFiled[key] = value
                            self.existing_db[dbName][colName] = tempFiled 
                            print(f"\nMineDB : alterFiledName : {fieldName} name changed to {newName}")
                        else:
                            print("\nError : alterFieldType : Invalid identifier")
                            return
                    else:
                        print("\nError : alterFieldType : Field not exist")
                        return
                else:
                    print("\nError : alterFieldType : Collection not exist")
                    return
            else:
                print("\nError : alterFieldType : Database not exist")
                return
        except(AttributeError, TypeError, ValueError):
            print("Error : alterFieldType : All parameters should be string")
    
    def alterDropField(self, dbName:str, colName:str, fieldName:str):
        if not self.__checkIns([dbName, colName, fieldName]):
            return
        try:
            if dbName in self.existing_db:
                if colName in self.existing_db[dbName]:
                    if fieldName in self.existing_db[dbName][colName]:
                        self.existing_db[dbName][colName].pop(fieldName)
                        print(f"\nMineDB : alterDropField : {fieldName} droped")
                    else:
                        print("\nError : alterDropFiled : Field not exist")
                        return
                else:
                    print("\nError : alterDropFiled : Collection not exist")
                    return
            else:
                print("\nError : alterDropFiled : Database not exist")
                return  
        except(ValueError, NameError, TypeError):
            print("Error : alterFieldType : All parameters should be string")

    def alterAddFiled(self, dbName:str, colName:str, fieldName:str, dataType:str):
        if not self.__checkIns([dbName, colName, fieldName]):
            return
        try:
            if dbName in self.existing_db:
                if colName in self.existing_db[dbName]:
                    if(dataType in ["text", "int", "float", "bool", "chr"]):
                        self.existing_db[dbName][colName][fieldName]={"dataType":dataType,"items":[]}
                        print(f"\nMineDB : alterAddField : {fieldName} added")
                    else:
                        print(f"\nError : alterAddField : invalid data type it should be : {["text", "int", "float", "bool", "chr"]}")
                        return
                else:
                    print("\nError : alterAddFiled : Collection not exist")
                    return
            else:
                print("\nError : alterAddFiled : Database not exist")
                return  
        except(ValueError, NameError, TypeError):
            print("Error : alterFieldType : All parameters should be string")