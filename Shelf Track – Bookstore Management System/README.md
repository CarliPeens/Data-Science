# 📚 Shelf Track – Bookstore Management System

Shelf Track is a command-line application written in Python that allows a bookstore clerk to manage book inventory using an SQLite database. This project was created as part of a Capstone Project for demonstrating applied knowledge in Python, relational databases, SQL operations, and clean coding practices.

---

## 🔧 Features

- 📘 Add new books to the inventory
- ✏️ Update book or author information
- ❌ Delete books from the system
- 🔍 Search for books by title keyword
- 🗂️ View all books with detailed author information
- 🧠 Data validation and error handling
- ✅ Uses best practices like modular functions and context managers for database safety

---

## 🗃️ Database Structure

### `book` Table

| Field     | Type     | Description                  |
|-----------|----------|------------------------------|
| id        | INTEGER  | Primary key (4-digit number) |
| title     | TEXT     | Book title                   |
| authorID  | INTEGER  | Foreign key to `author.id`   |
| qty       | INTEGER  | Quantity in stock            |

### `author` Table

| Field     | Type     | Description              |
|-----------|----------|--------------------------|
| id        | INTEGER  | Primary key              |
| name      | TEXT     | Author's name            |
| country   | TEXT     | Country of origin        |

---

## 📥 Getting Started

### Prerequisites

- Python 3.x (https://www.python.org/)
- No additional packages are required (uses built-in `sqlite3`)

### Running the Program

1. Clone or download the project files.
2. Open a terminal or command prompt.
3. Run the program:
   ```bash
   python shelf_track.py
   ```

4. Follow the on-screen menu to interact with the database.

---

## 📑 Example Menu

```
========== BOOKSTORE MENU ==========
1. Enter book
2. Update book
3. Delete book
4. Search books
5. View details of all books
0. Exit
```

---

## ✅ Best Practices Used

- Context managers (`with sqlite3.connect(...)`)
- `try/except` error handling
- Input validation
- Modular function design
- Docstrings and inline comments for clarity
- SQLite constraints and foreign keys

---

## 📌 Notes

- The database file `ebookstore.db` is created automatically on first run.
- Initial data is seeded once, using `INSERT OR IGNORE` to prevent duplicates.
- Data persists between program sessions.

---

## 🧑‍💻 Author

Capstone Project – Databases  
HyperionDev Bootcamp  
2025

---

## 📝 License

This project is free to use for educational and personal learning purposes.
