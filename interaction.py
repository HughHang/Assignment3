import psycopg2
from psycopg2 import sql

#------CONNECTION SETUP------#
#Set up database connection
connection = psycopg2.connect(
    #Replace the strings inbetween " " with your database information
    dbname = "yourDatabaseName",
    user = "yourUsername",
    password = "yourPassword",
    host = "yourHost",
    port = "yourPort"
)

#Create cursor to run SQL queries
cursor = connection.cursor()

#-----TABLE SETUP-----#
#Make the table if not already exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        enrollment_date DATE
        );
    """)
connection.commit()

#Check if already has data
cursor.execute("SELECT COUNT(*) FROM students")

#If data does not exist populate the table
if (cursor.fetchone()[0] == 0):
    cursor.execute(
        """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
        """)
    connection.commit()

#-----FUNCTIONS-----#

#Get all students in table
def getAllStudents():
    
    #Get all students
    cursor.execute("""SELECT * FROM STUDENTS""")

    #Print info of each student
    for student in cursor.fetchall():
        print("- - - - - - - - - -")
        print("Student ID:     ", student[0])
        print("First Name:     ", student[1])
        print("Last Name:      ", student[2])
        print("Email:          ", student[3])
        print("Enrollment Date:", student[4])

    print("\n")

#Add new student to table
def addStudent(fName, lName, email, enrollDate):

    #Insert the new student info into the students table
    cursor.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES 
                (%s, %s, %s, %s)""", (fName, lName, email, enrollDate))
    connection.commit()

    print("\nStudent", fName, lName, "added\n")
        

#Update a student's email
def updateStudentEmail(email, id):

    #Update the students email based on student's id
    cursor.execute("""UPDATE students 
                   SET email=%s 
                   WHERE student_id=%s""", (email, id))
    connection.commit()

    print("\nStudent email updated \n")

#Delete student from table
def deleteStudent(id):
    cursor.execute("""DELETE FROM students
                   WHERE student_id=%s""", id)
    connection.commit()

    print("\nStudent deleted \n")

while True:
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    operation = int(input("1. List all students \n2. Add a student \n3. Update student email \n4. Delete a student\n5. Quit\n\nPlease choose an operation: "))

    match(operation):
        #List all students
        case 1: 
            getAllStudents()

    #     #Add a student
        case 2:
            first_name = input("New student's first name:      ")
            last_name = input("New student's last name:       ")
            email = input("New student's email:           ")
            enrollment_date = input("New student's enrollment date: ")
            addStudent(first_name, last_name, email, enrollment_date)

    #     #Update student email
        case 3:
            id = input("Student's id:    ")
            newEmail = input("Enter new email: ")
            updateStudentEmail(newEmail, id)

    #     #Delete a student
        case 4:
            id = input("ID of student to delete: ")
            deleteStudent(id)

    #     #Quit the app
        case 5:
            break


cursor.close()
connection.close()