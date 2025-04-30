import sqlite3
import face_recognition
import os
import numpy as np

def create_database():
    # Connect to SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('faces.db')
    cursor = conn.cursor()

    # Create a table to store names and face encodings
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            face_encoding BLOB
        )
    """)
    conn.commit()
    conn.close()

def insert_face(name, image_path):
    # Load the image using face_recognition
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)

    if encoding:  # If a face is found
        # Convert the encoding to bytes for storage
        encoding_bytes = encoding[0].tobytes()

        # Connect to the SQLite database and insert the name and face encoding
        conn = sqlite3.connect('faces.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO faces (name, face_encoding) VALUES (?, ?)", (name, encoding_bytes))
        conn.commit()
        conn.close()

# Call create_database() to create the table if not already created
create_database()

# Insert example faces into the database
insert_face('Ena', 'image/ena1.jpg')  # Path to your first image
insert_face('mother', 'image/ammu.jpg')  # Path to your second image
insert_face('Alice', 'image/taylor.jpg')  # Path to your third image
