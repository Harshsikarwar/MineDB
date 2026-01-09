# MineDB

PyPI: https://pypi.org/project/minedb/

MineDB is a lightweight Python library that provides local persistent storage
for Python applications. It allows you to store data on disk, retrieve it later,
and work with it safely without using an external database.

MineDB is designed to be simple, predictable, and safe. It focuses on local
storage use cases such as application state, configuration data, and small
datasets that need to persist between program runs.

---------------------------------------------------------------------

## What MineDB does

MineDB provides:
- Persistent local storage
- Structured data storage with schemas
- Type validation
- Encrypted storage on disk
- Safe modification and removal of stored data

MineDB does NOT aim to replace full database systems. It is intended for
lightweight, local use cases.

---------------------------------------------------------------------

## Installation

Install MineDB using pip:

pip install minedb

---------------------------------------------------------------------

## Basic Usage

### Create a MineDB instance:

from MineDB import MineDB

db = MineDB()

Create a database and a collection with a defined structure:

db.createDB("app")
db.createCollection(
    "app",
    "settings",
    theme="text",
    notifications="bool"
)

### Store data:

db.load(theme="dark", notifications=True)

Modify stored data:

db.modify("theme", "dark", "notifications", False)

Remove stored data:

db.remove("theme", "dark")

Save data to disk:

db.save()

---------------------------------------------------------------------

## How MineDB works

- Data is stored locally on disk
- Data is encrypted before being written to disk
- Each collection has a fixed structure (schema)
- All fields in a collection always stay aligned
- Invalid data types raise errors immediately
- Partial writes and silent corruption are prevented

MineDB prioritizes correctness and safety over convenience.

---------------------------------------------------------------------

## Schema and Data Types

Supported data types:
- text
- int
- float
- bool
- chr

MineDB enforces data types strictly. Attempting to store an invalid type
will raise an error.

---------------------------------------------------------------------

## Schema Changes

You can safely change the structure of a collection:

Add a new field:

db.alterAddField("app", "settings", "font_size", "int")

Remove a field:

db.alterDropField("app", "settings", "font_size")

Change a field type (with safe conversion):

db.alterFieldType("app", "settings", "notifications", "int")

---------------------------------------------------------------------

## Encryption

MineDB encrypts all stored data using cryptography. The encryption key is
generated automatically on first use and reused for future sessions.

Encryption is intended to protect local data from casual inspection. It is
not designed for high-threat security environments.

---------------------------------------------------------------------

## Error Handling

MineDB raises errors when invalid operations are performed. Examples include:
- Using invalid data types
- Accessing missing fields or collections
- Attempting unsafe schema changes

Errors are raised explicitly to prevent silent failures.

---------------------------------------------------------------------

## Testing

MineDB is fully tested using pytest. Tests cover:
- Schema integrity
- Data insertion and removal
- Type validation
- Index alignment
- Safe schema modification

---------------------------------------------------------------------

## Requirements

- Python 3.9 or higher
- cryptography

---------------------------------------------------------------------

## License

MineDB is released under the MIT License. See the LICENSE file for details.

---------------------------------------------------------------------

## Author

Harsh Singh Sikarwar

---------------------------------------------------------------------

## Disclaimer

MineDB is intended for lightweight local storage use cases. It is not designed
to replace full database systems or distributed storage solutions.
