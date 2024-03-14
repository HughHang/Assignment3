import psycopg2
import os
from psycopg2 import sql

def getDatabaseCredentials():
    #Get environments to initialize connection
    databaseName = os.environ.get('DB_NAME')
    username = os.environ.get('USER')
    password = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    port = os.environ.get('PORT')
    return databaseName, username, password, host, port

#Set up the database connection
databaseName, username, password, host, port = getDatabaseCredentials()
connection = psycopg2.connect(
    dbname = databaseName,
    user = username,
    password = password,
    host = host,
    port = port
)

#Create cursor to run SQL queries
cursor = connection.cursor()

#Create table
def createTable():
    cursor.execute(
        """CREATE TABLE Students (
	
        student_id SERIAL PRIMARY KEY, 
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        enrollment_date DATE DEFAULT CURRENT_DATE
	
        );
        """)
    

#Populate table
def populateTable():

    #Check if already has data
    cursor.execute("SELECT COUNT(*) FROM Students")

    #If data does not exist populate the table
    if (cursor.fetchone()[0] == 0):
        cursor.execute(
            """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
            ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
            ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
            ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
            """)


#Main process starts here
createTable()
populateTable()

print("test")
