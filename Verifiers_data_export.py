import psycopg2
import csv
import os

#File path and File Name
file_path = 'C:\\Users\\Rehaansh\\Desktop\\data_engineer_veriff\\CSV_files\\'
file_name='Verifiers.csv'

#Database  connection
con = None

#Check if File path Exists
if os.path.exists(file_path):
    try:
        #Connect to DB
        con = psycopg2.connect(
        host = "localhost",
        database="Trans_DB",
        user = "postgres",
        password = "12345",
        port = "5433")

        #Creating a Cursor
        cur = con.cursor()

    except psycopg2.DatabaseError as e:
        print("Database Connection succesfull",e)


    sqlSelect = "select uuid,verifier_name from verifiers;"

    try:
        #Execute the Query
        cur.execute(sqlSelect)
        results = cur.fetchall()
    
        #Extract table Header
        header = [i[0] for i in cur.description]
        #Open CSV File
        csvFile = csv.writer(open(file_path + file_name,'w'),delimiter=',')
        csvFile.writerow(header)
        csvFile.writerows(results)

        #Success Message
        print("Data export Successfull")
    except psycopg2.DatabaseError as e:
        #Unsuccessful Message
        print("Data export Unsuccessful",e)
        quit()
    finally:

        #close the cursor
        cur.close()

        # Closing the Connection
        con.close()
else:
    print("File path doesn't exist")
