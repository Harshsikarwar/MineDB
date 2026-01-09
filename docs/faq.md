# Frequently Asked Questions (FAQ)

This document answers common questions about MineDB.
It is intended to clarify usage, limitations, and design decisions.

---

## What is MineDB used for?

MineDB is designed for local persistent storage in Python applications.
It is useful for:
- Application state
- Configuration storage
- Small datasets that must persist between runs
- Scripts and developer tools

It focuses on simplicity, safety, and correctness.

---

## Is MineDB a database?

MineDB is not a full database system.
It does not aim to replace SQLite, PostgreSQL, or other database engines.

MineDB is a lightweight local storage library with structure and persistence.

---

## Can MineDB be used in production?

MineDB can be used in production for appropriate use cases,
such as local tools or applications with limited data size.

It is not recommended for:
- High concurrency
- Multi-user environments
- Large-scale data workloads

---

## Is MineDB thread-safe?

MineDB is not designed for concurrent access.
It assumes a single-process, single-user usage model.

If multiple processes modify the same data files,
data corruption may occur.

---

## Where is data stored?

MineDB stores data locally on disk.
All data is encrypted before being written.

The storage location is managed internally,
and users do not need to handle files manually.

---

## How is data protected?

MineDB uses encryption to protect stored data.
An encryption key is generated automatically on first use
and reused for subsequent runs.

Encryption is intended for local protection,
not for high-security threat environments.

---

## What happens if I forget to call save()?

If `save()` is not called:
- Data remains only in memory
- Changes are lost when the program exits

Always call `save()` after making changes.

---

## Can I change the schema after inserting data?

Yes.
MineDB supports safe schema evolution.

You can:
- Add new fields
- Remove existing fields
- Change field data types

MineDB ensures record alignment and raises errors
if a schema change would break data integrity.

---

## What data types are supported?

MineDB supports:
- text
- int
- float
- bool
- chr

Values are strictly validated against the schema.

---

## What errors should I expect?

MineDB raises errors explicitly when:
- Data types do not match the schema
- Required fields are missing
- Databases or collections do not exist
- Unsafe operations are attempted

This behavior is intentional to prevent silent bugs.

---

## Can I inspect the source code?

Yes.
MineDB is open source.

The source code is available via the project repository
linked on the PyPI page.

---

## Will MineDB receive future updates?

MineDB is a learning-driven project.
Improvements may be added over time,
especially based on real usage and feedback.

---

End of FAQ
