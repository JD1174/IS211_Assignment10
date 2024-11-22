import sqlite3

print("Running create_pets_db.py")

# Create and connect to pets.db
connection = sqlite3.connect('pets.db')
cursor = connection.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    breed TEXT NOT NULL,
    age INTEGER NOT NULL,
    dead INTEGER NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    PRIMARY KEY (person_id, pet_id),
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (pet_id) REFERENCES pet(id)
);
""")

# Commit changes and close connection
connection.commit()
connection.close()

print("Database and tables have been initialized.")