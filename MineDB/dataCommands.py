class DataCommands:
    currDB = "sample"
    currColl = "data"

#datatype and value validation commands
    def __checkIns(self, value=[], source=None):
        for v in value:
            if v == None:
                continue
            if not isinstance(v, str):
                print(f"\nError : valueError : {source} : Value should be string")
                return False
        return  True

    def __checkValueType(self, value, source=None):
        if type(value) == str:
            if len(value) > 1:
                return "text"
            else:
                return "chr"
        elif type(value) == int:
            return 'int'
        elif type(value) == float:
            return 'float'
        elif type(value) == bool:
            return 'bool'
        else:
            print(f"\nError : {source} : Invalid data type of value {value}")
            return None

    def __checkValue(self, loadData={}, source=None):
        #checking valiadation of loading/modifing data
        for key, value in loadData.items():
            if key in self.existing_db[self.currDB][self.currColl]:
                if value == None or value == "None":
                    continue
                if self.__checkValueType(value,source) != self.existing_db[self.currDB][self.currColl][key]["dataType"]:
                    print(f"\nError : {source} : Invalid data type of value {value}")
                    return False
            else:
                print(f"\nError : {source} : Field not exist")
                return False
        return True

#get and set commands
    def getDB(self):
        print(f"\nMineDB : Currrent Database : {self.currDB}")
        return self.currDB

    def getCollection(self):
        print(f"\nMineDB : Current Collection : {self.currColl}")
        return self.currColl

    def setDB(self, dbName):
        try:
            if not self.__checkIns([dbName],"setDB"):
                return
            if dbName.isidentifier():
                if dbName in self.existing_db:
                    self.currDB = dbName
                else:
                    print("\nError : setDB : Database not exist")
            else:
                print("\nError : setDB : Invalid identifier")
        except(AttributeError, TypeError, NameError):
            print("\nError : setDB : All parameters should be string")

    def setCollection(self, colName):
        try:
            if not self.__checkIns([colName],"setCollection"):
                return
            if colName.isidentifier():
                if colName in self.existing_db[self.currDB]:
                    self.currColl = colName
                else:
                    print("\nError : setCollection : Collection not exist")
            else:
                print("\nError : setCollection : Invalid identifier")
        except(AttributeError, TypeError, NameError):
            print("\nError : setDB : All parameters should be string")

#major data commands
    def load(self, **kwargs):
        try:
            if len(self.existing_db[self.currDB][self.currColl]) == len(kwargs):
                if not self.__checkValue(kwargs,"load"):
                    return
                for key, value in kwargs.items():
                    self.existing_db[self.currDB][self.currColl][key]['items'].append(value)
                print("\nMineDB : load : Data loaded")
            else:
                print("\nError : load : Incomplete loading")
        except(AttributeError, TypeError, NameError):
            print("\nError : load : All parameters should be string")

    def modify(self, search_by, search_value, update_field, new_value):
        if self.__checkValue({search_by:search_value,update_field:new_value},"modify"):
            isPresent=0
            value_array = self.existing_db[self.currDB][self.currColl][search_by]["items"]
            for search in range(0,len(value_array)):
                if value_array[search] == search_value:
                    isPresent += 1
                    pos = search
                    self.existing_db[self.currDB][self.currColl][update_field]["items"][pos] = new_value
                    
            if isPresent == 0:
                print("\nError : modify : search_value not exist")
            else:
                print(f"\nMineDB : modify : {isPresent} value(s) modified")
        else:
            return

    def remove(self, search_by, search_value):
        if self.__checkValue({search_by:search_value},"modify"):
            isPresent=0
            value_array = self.existing_db[self.currDB][self.currColl][search_by]["items"]
            for check in range(len(value_array)):
                if search_value in value_array:
                    isPresent += 1
                    pos = value_array.index(search_value)
                    for del_field in self.existing_db[self.currDB][self.currColl]:
                        self.existing_db[self.currDB][self.currColl][del_field]["items"].pop(pos)
                    
            if isPresent == 0:
                print("\nError : remove : search_value not exist")
            else:
                print(f"\nMineDB : remove : {isPresent} value(s) removed")
        else:
            return

    def explore(self,*args, condition=None):
        print(f"\nMineDB : Exploring : {self.currColl}")
        if condition == None:
            for value in args:
                if value in self.existing_db[self.currDB][self.currColl]:
                    print(value," : ",self.existing_db[self.currDB][self.currColl][value]["items"])
                else:
                    print("Error : explore : Field not exist")

    def exploreAll(self):
        try:
            print(f"\nMineDB : Exploring All : {self.currColl}")
            for value in self.existing_db[self.currDB][self.currColl]:
                print(value," : ",self.existing_db[self.currDB][self.currColl][value]["items"])
        except(TypeError):
            print("\nError : exploreAll : something went wrong, check setup of database and column")