import psycopg2
import csv
import os
import datetime as dt

#File path and File Name
file_path = 'C:\\Users\\Rehaansh\\Desktop\\data_engineer_veriff\\CSV_files\\'
file_name='Events.csv'

#Database  connection
con = None

#Check if File path Exists
if os.path.exists(file_path + file_name):
    try:
        #Connect to DB
        con = psycopg2.connect(
        host = "localhost",
        database="veriff_dwh_db",
        user = "postgres",
        password = "12345",
        port = "5433")

        #Creating a Cursor
        cur = con.cursor()
        
        print("Database connetion Successfull")

    except psycopg2.DatabaseError as e:
        print("Database Connection Unsuccesfull",e)
   
    try:
        #Assign CSV File to Reader
        csvFile = csv.DictReader(open(file_path + file_name))

        #Recordcount variable
        file_count = 0

        #Insert data into the table
        for row in csvFile:
            #time_var= dt.datetime.strptime(created_at,"%Y-%m-%d %H:%M:%S+%Z")
            sqlinsert = "INSERT INTO events_dim(uuid,session_uuid,event_type,created_at) VALUES(%s,%s,%s,%s);"
            cur.execute(sqlinsert,(row['uuid'],row['session_uuid'],row['event_type'],row['created_at']))
            con.commit()
            #Increment the Record Count
            file_count += 1

        print("Data loaded Successfully") 

    except psycopg2.DatabaseError as e:
        print("Error while importing data from File",e)
        quit()
    
    #Reconciliation Step - Check to ensure file and table counts are matching
    try:
        print("Number of rows from File:",file_count)
        cur.execute("select count(*) from events_dim;")
        Table_count = cur.fetchone()

        if file_count == Table_count[0]:
            print("File and Table counts are matched","Number of rows from file",file_count,"Number of rows from Table",Table_count[0])
        else:
            print("File and Table counts are not matched","Number of rows from file",file_count,"Number of rows from Table",Table_count[0])
    except psycopg2.DatabaseError as e:
        print("Reconciliation Error",e)

    finally:    
        #close the cursor
        cur.close()
    


        # Closing the Connection
        con.close()
else:
    print("File path doesn't exist")

