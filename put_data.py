import mysql.connector
from mysql.connector import Error
import json

# Function to determine the MySQL data type based on Python type
def get_data_type(value):
    if isinstance(value, int):
        return 'INT'
    elif isinstance(value, float):
        return 'DECIMAL(9, 6)'  # Adjust precision and scale as needed for float values
    elif isinstance(value, str):
        return 'VARCHAR(255)'  # Adjust length as needed for string values
    else:
        return 'VARCHAR(255)'  # Default to VARCHAR for unknown types

# Function to flatten nested dictionaries
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Replace these values with your MySQL server details
host = 'localhost'
user = 'root'
password = ''
database = 'weatherapi'
table_name = 'hello'

# JSON file path
json_file_path = 'C:/Users/DELLL/Desktop/h/api_data.json'

# Read JSON data from file
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

# Flatten the JSON data
flat_json_data = flatten_dict(json_data)

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create table with the same structure as 'hello'
        create_table_query = f"CREATE TABLE IF NOT EXISTS `hello` ("
        create_table_query += "`id` INT AUTO_INCREMENT PRIMARY KEY, "
        for key, value in flat_json_data.items():
            create_table_query += f"`{key}` {get_data_type(value)}, "
        create_table_query = create_table_query.rstrip(', ') + ")"

        print(f"SQL Query: {create_table_query}")
        cursor.execute(create_table_query)

        # Insert values into the table
        insert_query = f"INSERT INTO `hello` ({', '.join(flat_json_data.keys())}) VALUES ({', '.join(['%s'] * len(flat_json_data))})"
        values = tuple(flat_json_data[key] if not isinstance(flat_json_data[key], list) else json.dumps(flat_json_data[key]) for key in flat_json_data)

        cursor.execute(insert_query, values)
        connection.commit()


        print("Data inserted successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
