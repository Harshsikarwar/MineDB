# Getting Started with MineDB

This guide helps you start using MineDB step by step.
By the end of this guide, you will be able to create local storage,
store data, modify it, and persist it safely on disk.

---

## Installation

Install MineDB using pip:

```bash
pip install minedb
```

---

## Importing MineDB

Import the MineDB class:

```python
from MineDB import MineDB
```

Create an instance:

```python
db = MineDB()
```

---

## Creating a Database

A database is the top-level container.

```python
db.createDB("app")
```

---

## Creating a Collection

A collection defines a fixed structure (schema).
Each field must be declared with a data type.

Supported data types:
- text
- int
- float
- bool
- chr

Example:

```python
db.createCollection(
    "app",
    "settings",
    theme="text",
    notifications="bool"
)
```

---

## Selecting the Active Database and Collection

MineDB operates on the currently selected database and collection.

```python
db.useDB("app")
db.useCollection("settings")
```

---

## Storing Data

All fields defined in the collection must be provided.

```python
db.load(
    theme="dark",
    notifications=True
)
```

If a required field is missing or the data type is incorrect,
MineDB raises an error immediately.

---

## Modifying Stored Data

Modify existing records by matching a field value.

Example: change `notifications` where `theme` is `"dark"`.

```python
db.modify(
    "theme",
    "dark",
    "notifications",
    False
)
```

If the matching value does not exist, an error is raised.

---

## Removing Stored Data

Remove records by matching a field value.

```python
db.remove(
    "theme",
    "dark"
)
```

This removes the entire record safely while preserving schema integrity.

---

## Saving Data to Disk

Persist all data to disk:

```python
db.save()
```

All stored data is encrypted automatically before saving.

---

## Automatic Loading

MineDB automatically loads existing data when initialized,
as long as encrypted data files are present.

No manual loading step is required.

---

## Changing the Collection Schema

### Adding a Field

```python
db.alterAddField(
    "app",
    "settings",
    "font_size",
    "int"
)
```

Existing records receive a default value.

---

### Removing a Field

```python
db.alterDropField(
    "app",
    "settings",
    "font_size"
)
```

---

### Changing a Field Type

```python
db.alterFieldType(
    "app",
    "settings",
    "notifications",
    "int"
)
```

If conversion is not possible, MineDB raises an error.

---

## Error Handling

MineDB raises errors explicitly to prevent silent failures.

Common error cases:
- Invalid data types
- Missing required fields
- Accessing non-existent databases or collections
- Unsafe schema modifications

---

## When to Use MineDB

MineDB is suitable for:
- Local application state
- Configuration storage
- Small persistent datasets
- Scripts and utilities

MineDB is not designed for:
- Large-scale databases
- Concurrent multi-user systems
- High-performance query workloads

---

## Next Steps

- Review core concepts
- Explore the API reference
- Check test cases for real usage examples

---

End of Getting Started
