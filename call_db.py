import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect("traffic_data.db")  # Creates 'traffic_data.db' in the current directory

# Create a cursor object to execute SQL commands
cursor = conn.cursor()


def add(data):
    pass
def delete(data):
    pass
def update(data):
    pass
def get(data):
    pass
def list(data):
    pass