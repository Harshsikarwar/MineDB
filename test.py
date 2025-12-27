from MineDB import MineDB

mdb = MineDB()

mdb.showCollection("Disha_College","Teachers")
mdb.alterAddFiled("Disha_College", "Teachers","Bonus","float")
mdb.showCollection("Disha_College","Teachers")





'''mdb.createDB(True)
mdb.showDB(123)
mdb.dropDB(123)
mdb.renameDB(123,True)
print("---")
mdb.showCollection(None)
print("---")
mdb.createCollection(123,"Disha_College")
mdb.dropCollection("Disha_College",False)
mdb.renameCollection(123,"Teachers",123)
mdb.alterFieldName("Disha_College",123,"phone","mobile")
mdb.alterFieldType("Disha_College",123,"phone",True)'''