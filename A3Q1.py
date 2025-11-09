import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
PASS = os.getenv("PASS")



def connect():
    return psycopg2.connect(
        host="localhost",
        database=DATABASE,
        user="postgres",
        password= PASS
    )
conn = connect()
cur = conn.cursor()

def getAllStudents():

    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):

    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email,enrollment_date))
    conn.commit()
    conn.close()

def updateStudentEmail(student_id, new_email):

    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id))
    conn.commit()
    conn.close()

def deleteStudent(student_id):

    cur.execute("DELETE FROM students WHERE student_id = %s",
                (student_id,))
    conn.commit()
    conn.close()

getAllStudents()