import mysql.connector
import pandas as pd
import Connection





class Main:

    bol=True
    while(bol):
        print("\n1 ->Create Database")
        print("2 ->show database")
        print("3 -> Drop Database ")
        print("4 ->Create a table")
        print("5 ->Select Database ")
        print("6 ->Show Tables")
        print("7 ->inserting value into tables ")
        print("8 ->Describe Tables")
        print("100 ->Exit ")
        choice = int(input("Enter the Choice : "))
        match choice:
            case 1:
                name=input("Enter name of the database :")
                Connection.create_database(name)
            case 2:
                Connection.Show_database()
            case 3:
                name=input("Enter name of the database :")
                Connection.Drop_database(name)
                print(".....................Database Deleted Successful")
            case 4:
                name_table=input("Enter the Name of the Table : ")
                number_of_data=int(input("Enter the number of data you have like id,name .. :"))
                list=""
                k=0
                for i in  range (0,number_of_data):
                    name=input("Enter the new/next data name : ")
                    if k==0:

                        primary = input("If you need to keep this dat as primary key(y/n)")
                        if(primary=='y'):
                            primary_yes=" PRIMARY KEY "
                            k=1
                        else:
                            primary_yes=" "
                    notnull = input("If you need to keep this dat as Not Null(y/n)")
                    if(notnull=='y'):
                        notnull_yes=" NOT NULL "
                    else:
                        notnull_yes=""
                    Autoincrement= input("If you need to keep this dat as Auto Intrement (y/n)")
                    if(Autoincrement=='y'):
                        Auto=" AUTO_INCREMENT "
                    else:
                        Auto=""
                    print("Data Type like : \nVARCHAR\nINT\n")

                    data_type= input("Enter your dataType : ")
                    if not data_type=='INT':
                        data_value = int(input("Enter the data Size : "))
                    if data_type=='INT':
                        if i == number_of_data -1:
                            list = list + name + " " + data_type + primary_yes + notnull_yes + Auto
                        else:
                            list = list + name + " " + data_type + primary_yes + notnull_yes + Auto + ","
                    else:
                        if i == number_of_data - 1:
                            list = list + name + " " + data_type + "(" + str(data_value) + ")" + primary_yes + notnull_yes + Auto
                        else:
                            list = list + data_type + "(" + str(data_value) + ")" + primary_yes + notnull_yes + Auto + ","
                    primary_yes=""
                Connection.Add_table(list,name_table)

            case 5:
                Connection.Show_database()
                database=input("Enter the Database Name: ")
                Connection.Use_database(database)
            case 6:
                Connection.Show_tables()
            case 7:
                Connection.Show_tables()
                names = input("Enter the Table name : ")
                k = Connection.Describe_tables(names)
                s=""
                for i in range(k):
                    val=input("Enter the Value : ")
                    if val.isdigit():
                        if i == 0:
                            s = s + val
                        else:
                            s = s + "," + val
                    else:
                        if i == 0:
                            s = s + "'"+val+"'"
                        else:
                            s = s + ",'" + val+"'"

                Connection.insert_into(s,names)

            case 8:
                Connection.Show_tables()
                name=input("Enter the Table name : ")
                k=Connection.Describe_tables(name)


            case 100:
                bol=False







