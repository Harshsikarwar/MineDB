# API Reference – MineDB

This document describes the public API of MineDB.
Only user-facing methods are documented here.
Internal and private methods are intentionally omitted.

---

## MineDB()

Creates a new MineDB instance.

```python
from MineDB import MineDB
db = MineDB()
```

When initialized:
- Existing encrypted data is loaded automatically (if present)
- A new encryption key is generated on first use

---

## createDB(dbName)

Creates a new database.

```python
db.createDB("app")
```

Parameters:
- dbName (str): Name of the database

Raises:
- ValueError if the database already exists

---

## useDB(dbName)

Selects an existing database as the active database.

```python
db.useDB("app")
```

Parameters:
- dbName (str): Name of the database

Raises:
- KeyError if the database does not exist

---

## createCollection(dbName, colName, **fields)

Creates a new collection with a fixed schema.

```python
db.createCollection(
    "app",
    "settings",
    theme="text",
    notifications="bool"
)
```

Parameters:
- dbName (str): Database name
- colName (str): Collection name
- fields (keyword arguments): Field names with data types

Raises:
- ValueError if the collection already exists
- ValueError if an invalid data type is provided

---

## useCollection(colName)

Selects an existing collection as the active collection.

```python
db.useCollection("settings")
```

Parameters:
- colName (str): Collection name

Raises:
- KeyError if the collection does not exist

---

## load(**values)

Inserts a new record into the active collection.

```python
db.load(
    theme="dark",
    notifications=True
)
```

Rules:
- All fields must be provided
- Values must match the schema data types

Raises:
- ValueError for missing fields
- ValueError for invalid data types

---

## modify(matchField, matchValue, targetField, newValue)

Modifies records by matching a field value.

```python
db.modify(
    "theme",
    "dark",
    "notifications",
    False
)
```

Parameters:
- matchField (str): Field used for matching
- matchValue: Value to match
- targetField (str): Field to update
- newValue: New value to set

Raises:
- ValueError if no matching record exists
- ValueError if the new value has an invalid type

---

## remove(matchField, matchValue)

Removes records by matching a field value.

```python
db.remove(
    "theme",
    "dark"
)
```

Parameters:
- matchField (str): Field used for matching
- matchValue: Value to match

Raises:
- ValueError if no matching record exists

---

## save()

Persists all data to disk.

```python
db.save()
```

Behavior:
- Encrypts all data
- Writes data to local storage
- Overwrites existing stored data safely

---

## alterAddField(dbName, colName, fieldName, dataType)

Adds a new field to an existing collection.

```python
db.alterAddField(
    "app",
    "settings",
    "font_size",
    "int"
)
```

Parameters:
- dbName (str)
- colName (str)
- fieldName (str)
- dataType (str)

Raises:
- ValueError for invalid data type
- RuntimeError if schema integrity is compromised

---

## alterDropField(dbName, colName, fieldName)

Removes a field from a collection.

```python
db.alterDropField(
    "app",
    "settings",
    "font_size"
)
```

Parameters:
- dbName (str)
- colName (str)
- fieldName (str)

Notes:
- Removing all fields is allowed
- Record alignment is preserved

---

## alterFieldType(dbName, colName, fieldName, newType)

Changes the data type of an existing field.

```python
db.alterFieldType(
    "app",
    "settings",
    "notifications",
    "int"
)
```

Behavior:
- Attempts safe type conversion
- Raises an error if conversion is not possible

Raises:
- ValueError for incompatible conversions

---

## renameDB(oldName, newName)

Renames an existing database.

```python
db.renameDB("old_db", "new_db")
```

Raises:
- KeyError if the database does not exist
- ValueError if the new name already exists

---

## renameCollection(dbName, oldName, newName)

Renames an existing collection.

```python
db.renameCollection("app", "settings", "config")
```

Raises:
- KeyError if the collection does not exist
- ValueError if the new name already exists

---

## Version Information

The MineDB instance exposes a version string:

```python
db.version
```

This value matches the installed package version.

---

End of API Reference
