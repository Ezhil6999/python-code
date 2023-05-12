import mysql.connector
from mysql.connector import Error
import pandas as pd

class Connection:
    connection = mysql.connector.connect(host="localhost", user="root", password="ezhil6999")
def create_database(name):
    cursor = Connection.connection.cursor()
    cursor.execute("create database " + name)
    print("Database created successfully....! ")
    cursor.close()

def Show_database():
    cursor = Connection.connection.cursor()
    cursor.execute("Show databases;")
    for x in cursor:
        print(x)
    cursor.close()
def Drop_database(name):
    try:
        cursor = Connection.connection.cursor()
        cursor.execute("Drop Database "+ name)
        cursor.close()
    except Error as e:
        print(e)
def Add_table(list,name):
    try:
        cursor = Connection.connection.cursor()
        cursor.execute("Create table "+name+"("+list+")")
        cursor.close()
        Connection.connection.commit()
        print("Table Created Successfully.................")
    except Error as e:
        print(e)
def Use_database(name):
    try:
        cursor = Connection.connection.cursor()
        cursor.execute("use "+name)
        cursor.close()
        print(name+ "Database Selected....................")
    except Error as e:
        print(e)
def Show_tables():
    try:
        cursor = Connection.connection.cursor()
        cursor.execute("Show tables")
        for i in cursor:
            print(i)
        cursor.close()
    except Error as e:
        print(e)
def Describe_tables(name):
    try:
        cursor = Connection.connection.cursor()
        cursor.execute("Describe "+name)
        k=0
        for i in cursor:
            print(i)
            k=k+1
        return k
    except Error as e:
        print(e)
def insert_into(s,name):
    try:
        cursor = Connection.connection.cursor()
        cursor.execute("INSERT INTO "+name+" value("+s+")")
        cursor.close()
        print("Insertion Successful.................")


    except Error as e:
        print(e)
