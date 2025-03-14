import sqlite3

def read_table(db_path, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the query to read the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows

if __name__ == "__main__":
    db_path = 'traffic_data.db'
    table_name = 'traffic_info'
    data = read_table(db_path, table_name)
    for row in data:
        print(row)