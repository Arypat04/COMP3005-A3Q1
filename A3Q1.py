import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve database name and password from the .env file
DATABASE = os.getenv("DATABASE")
PASS = os.getenv("PASS")

# Function to establish a connection to the PostgreSQL database
def connect():
    return psycopg2.connect(
        host="localhost",        # Host where PostgreSQL is running
        database=DATABASE,       # Database name from .env
        user="postgres",         # Default PostgreSQL user
        password=PASS            # Password from .env
    )

# Establish the connection and create a cursor to execute SQL commands
conn = connect()
cur = conn.cursor()

# Function to retrieve and display all records from the students table
def getAllStudents():
    cur.execute("SELECT * FROM students")  # Execute SQL query to fetch all students
    for row in cur.fetchall():             # Loop through and print each record
        print(row)
    conn.close()                           # Close the database connection

# Function to insert a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()  # Save changes to the database
    conn.close()   # Close the connection

# Function to update a student's email address by their student_id
def updateStudentEmail(student_id, new_email):
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (new_email, student_id)
    )
    conn.commit()  # Save the update
    conn.close()   # Close the connection

# Function to delete a student record using their student_id
def deleteStudent(student_id):
    cur.execute(
        "DELETE FROM students WHERE student_id = %s",
        (student_id,)
    )
    conn.commit()  # Save the deletion
    conn.close()   # Close the connection

# Run the function to display all students when the script executes
getAllStudents()
