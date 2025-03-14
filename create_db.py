import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect("traffic_data.db")  # Creates 'traffic_data.db' in the current directory

# Create a cursor object to execute SQL commands
cursor = conn.cursor()
 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS traffic_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        road_type TEXT,
        city TEXT,
        road_name TEXT,
        current_speed REAL,
        free_flow_speed REAL,
        traffic_level TEXT,
        longitude REAL,
        latitude REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()  # Save changes
conn.close()
