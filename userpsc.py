import psycopg2
import flask

# Replace these with your PostgreSQL connection details
dbname = 'usrpsc'
user = 'postgres'
password = 'Kapoor@007'
host = 'localhost'
port = '5432'  # Default is usually 5432

try:
    # Establish a connection to the database
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example: Execute a simple query
    cursor.execute("SELECT * FROM usrpsc;")

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
