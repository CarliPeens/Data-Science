# ===IMPORTS===
import sqlite3

# ===DATABASE SETUP===
"""Function to create the book and author tables if they do not exist."""
def create_database():
    with sqlite3.connect('ebookstore.db') as conn:
        cursor = conn.cursor()

        # Create the book table
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS book(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                authorID INTEGER NOT NULL,
                qty INTEGER NOT NULL
                )
            """) 
        except sqlite3.Error as e:
            print("Database error: ", e)
    
        # Create the author table
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS author(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                country TEXT NOT NULL
                )
            """)
        except sqlite3.Error as e:
            print("Database error: ", e)

        conn.commit()


"""Function to populate the book and author tables with initial data."""
def populate_database():
    # Store original data of the book table in a list
    books = [(3001, "A Tale of Two Cities", 1290, 30),
            (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
            (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
            (3004, "The Lord of the Rings", 6380, 37),
            (3005, "Alice's Adventures in Wonderland", 5620, 12)]  
    
    # Store original data of the author's table in a list
    authors = [(1290, "Charles Dickens", "England"),   
               (8937, "J.K. Rowling", "England"),
               (2356, "C.S. Lewis", "Ireland"),
               (6380, "J.R.R. Tolkien", "South Africa"),
               (5620, "Lewis Carroll", "England")] 

    # Insert the data into the ebookstore database
    try:
        with sqlite3.connect('ebookstore.db') as conn:
            cursor = conn.cursor()
            cursor.executemany('INSERT OR IGNORE INTO author VALUES (?, ?, ?)', authors)
            cursor.executemany('INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)', books)
            conn.commit()
    except sqlite3.Error as e:
        print("Database error: ", e) 
    


# ===VALIDATION===
def get_valid_int(prompt, length=4):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and len(value) == length:
            return int(value)
        print(f"Invalid input. Please enter a {length}-digit integer.")

# ===FUNCTIONS===
"""Function to add a new book to the database."""
def add_book():
    book_id = int(input("Enter the new book's id(4 digits): \n"))
    title = input("Enter the new book's title: \n")
    author_id = int(input("Enter the new book's author id(4 digits): \n"))
    qty = get_valid_int("Enter quantity: ", length=1)

    try:
        with sqlite3.connect('ebookstore.db') as conn:
            cursor = conn.cursor()
            # Check if author exists
            cursor.execute("SELECT * FROM author WHERE id = ?", (author_id,))
            author = cursor.fetchone()
            if not author:
                name = input("Author not found. Enter author's name: ").strip()
                country = input("Enter author's country: ").strip()
                cursor.execute("INSERT INTO author VALUES (?, ?, ?)", (author_id, name, country))
            # Add new book to the book table
            cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (book_id, title, author_id, qty))
            conn.commit()
        print("Book added successfully.")
    except sqlite3.Error as e:
        print("Database error: ", e) 


"""Function to update a book's or author's details."""    
def update_book():
    # Get the ID of the book that needs to be updated
    book_id = get_valid_int("Enter the book ID to update: \n")

    try:
        with sqlite3.connect('ebookstore.db') as conn:
            cursor = conn.cursor()
            # Select the information of the book whose id was entered
            cursor.execute('''
                SELECT b.title, a.name, a.country, b.authorID, b.qty
                FROM book b
                JOIN author a ON b.authorID = a.id
                WHERE b.id = ?
            ''', (book_id,))
            result = cursor.fetchone()

            if not result:
                print("Book not found.")
                return

            # Store each element into objects
            title, author_name, country, author_id, qty = result
            print(f"\nCurrent Book Info:\nTitle: {title}\nAuthor: {author_name}\nCountry: {country}\nQuantity: {qty}")

            # Get the field that needs to be upgraded
            print("\nWhat would you like to update?")
            print("1. Title\n2. Author ID\n3. Quantity\n4. Author's name\n5. Author's country")
            choice = input("Enter your choice: ")

            # Update the selected field
            if choice == '1':
                new_title = input("Enter new title: ").strip()
                cursor.execute("UPDATE book SET title = ? WHERE id = ?", (new_title, book_id))
            elif choice == '2':
                new_author_id = get_valid_int("Enter new author ID: ")
                cursor.execute("UPDATE book SET authorID = ? WHERE id = ?", (new_author_id, book_id))
            elif choice == '3':
                new_qty = get_valid_int("Enter new quantity: ", length=1)
                cursor.execute("UPDATE book SET qty = ? WHERE id = ?", (new_qty, book_id))
            elif choice == '4':
                new_name = input("Enter new author's name: ").strip()
                cursor.execute("UPDATE author SET name = ? WHERE id = ?", (new_name, author_id))
            elif choice == '5':
                new_country = input("Enter new author's country: ").strip()
                cursor.execute("UPDATE author SET country = ? WHERE id = ?", (new_country, author_id))
            else:
                print("Invalid choice.")
                return
            conn.commit()
            print("Update successful.")    
    except sqlite3.Error as e:
        print("Database error: ", e)  
    

"""Function to delete a book from the database."""   
def delete_book():
    # Get the ID of the book that needs to be updated
    book_id = get_valid_int("Enter the book ID to delete: \n")
    
    try:
        with sqlite3.connect('ebookstore.db') as conn:
            cursor = conn.cursor()
            # Delete te book
            cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
            if cursor.rowcount == 0:
                print("Book not found.")
            else:
                conn.commit()
                print("Book deleted successfully.")
    except sqlite3.Error as e:
        print("Database error: ", e)


"""Function to search for books by title keyword."""        
def search_book():
    # Get the keyword of the book
    keyword = input("Enter title keyword to search: ").strip()
    
    try:
        with sqlite3.connect('ebookstore.db') as conn:
            cursor = conn.cursor()
            # Select the books found using the given keyword
            cursor.execute('''
                SELECT b.title, a.name, b.qty
                FROM book b
                JOIN author a ON b.authorID = a.id
                WHERE b.title LIKE ?
            ''', (f"%{keyword}%",))
            results = cursor.fetchall()
            # Display the results
            if results:
                for title, author, qty in results:
                    print(f"\nTitle: {title}\nAuthor: {author}\nQuantity: {qty}")
            else:
                print("No books found.")
    except sqlite3.Error as e:
        print("Database error: ", e)


"""Function to display all books with author and country details."""    
def view_all():
    try:
        # Select all the books' title, author name and country
        with sqlite3.connect('ebookstore.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT b.title, a.name, a.country
                FROM book b
                INNER JOIN author a ON b.authorID = a.id
            ''')

            # Show all the books' title, author name and country
            results = cursor.fetchall()
            if results:
                for title, name, country in results:
                    print("\n--------------------------------------------------")
                    print(f"Title: {title}\nAuthor's Name: {name}\nAuthor's Country: {country}")
                    print("--------------------------------------------------")
            else:
                print("No book details to display.")
    except sqlite3.Error as e:
        print("Database error: ", e)
    

# ===MAIN MENU===
def main():
    create_database()
    populate_database()

    while True:
        print("\n========== BOOKSTORE MENU ==========")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("5. View details of all books")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            view_all()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
