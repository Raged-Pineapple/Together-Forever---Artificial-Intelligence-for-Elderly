import sqlite3

# Connect to SQLite database (it will create it if it doesn't exist)
try:
    conn = sqlite3.connect('medicines.db')
    print("Database connected successfully.")
    
    # Create the table
    conn.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dose TEXT NOT NULL,
        schedule TEXT NOT NULL
    );
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
    print("Database and table created successfully!")

except sqlite3.Error as e:
    print("Error while creating database:", e)
