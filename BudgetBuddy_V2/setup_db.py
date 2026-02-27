import sqlite3

def setUp_db():
    connection = sqlite3.connect("Budget.db")
    cursor = connection.cursor()
    
    sql_query = """CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT); """
        
    cursor.execute(sql_query)
    connection.commit()
    connection.close()
    
    print("Database setup completed successfully and the 'expenses' table has been created.")
    


if __name__ == "__main__":
    setUp_db()
        