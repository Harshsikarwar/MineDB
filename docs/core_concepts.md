# Core Concepts of MineDB

This document explains the core ideas behind MineDB.
Understanding these concepts will help you use MineDB correctly
and avoid common mistakes.

MineDB is designed to be simple, predictable, and safe.
It focuses on correctness rather than convenience.

---

## What MineDB Is

MineDB is a local persistent storage library for Python.

It allows you to:
- Store data locally on disk
- Retrieve it across program runs
- Work with structured data
- Enforce data types
- Modify stored data safely

MineDB is intended for small to medium local data needs.

---

## What MineDB Is Not

MineDB is NOT:
- A full database system
- A replacement for SQLite, PostgreSQL, or MySQL
- Designed for concurrent multi-user access
- Optimized for large datasets or complex queries

MineDB focuses on local storage, not scalability.

---

## Databases and Collections

MineDB organizes data using two levels:

1. Database  
2. Collection  

A database is a logical container.
A collection stores structured records.

Each collection has a fixed schema.

---

## Schema

A schema defines:
- Field names
- Field data types

Example schema:

```python
db.createCollection(
    "app",
    "settings",
    theme="text",
    notifications="bool"
)
```

Once created:
- All records must follow this schema
- Missing fields are not allowed
- Extra fields are not allowed

This prevents inconsistent data.

---

## Records and Alignment

MineDB stores data in a column-oriented structure.

This means:
- Each field stores its own list of values
- All fields must always have the same number of items

MineDB enforces strict alignment:
- One record = one index across all fields
- Removing or modifying data affects all fields equally

This prevents index drift and corruption.

---

## Data Types

MineDB supports the following data types:

- text → string values
- int → integer values
- float → floating-point values
- bool → boolean values
- chr → single-character strings

Data types are enforced strictly.
Invalid values raise errors immediately.

---

## Loading Data

When loading data:
- All fields must be provided
- Values must match declared data types

Example:

```python
db.load(theme="dark", notifications=True)
```

Invalid or incomplete data is rejected.

---

## Modifying Data

Modification works by:
- Matching an existing value
- Updating another field at the same record index

Example:

```python
db.modify("theme", "dark", "notifications", False)
```

If the matching value does not exist, an error is raised.

---

## Removing Data

Removing data deletes an entire record.

Example:

```python
db.remove("theme", "dark")
```

MineDB ensures:
- All fields remain aligned
- No partial deletions occur

---

## Schema Changes

MineDB allows safe schema evolution.

You can:
- Add new fields
- Remove existing fields
- Change field data types

All schema changes:
- Preserve record alignment
- Validate data integrity
- Raise errors on unsafe operations

---

## Encryption

MineDB encrypts all stored data before writing it to disk.

Key points:
- Encryption is automatic
- Keys are generated on first use
- Keys are reused safely
- Keys are never shipped with the package

Encryption is intended for local protection.

---

## Persistence

Data persistence works as follows:
- Data is kept in memory during runtime
- Calling `save()` writes encrypted data to disk
- Data is automatically loaded on initialization

Users do not need to manage files manually.

---

## Error Philosophy

MineDB follows a strict error philosophy:

- Errors are raised immediately
- Silent failures are avoided
- Incorrect usage is rejected

This helps detect bugs early.

---

## Design Philosophy

MineDB is designed with these principles:

- Simplicity over features
- Safety over convenience
- Explicit errors over silent behavior
- Local-first storage

Understanding these principles helps use MineDB effectively.

---

End of Core Concepts
