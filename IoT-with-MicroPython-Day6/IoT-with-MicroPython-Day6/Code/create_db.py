# create_db.py
import sqlite3

conn = sqlite3.connect("iot_data.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temperature REAL,
                    humidity REAL,
                    timestamp TEXT
                )''')

conn.commit()
conn.close()

print("Database and table created successfully!")
