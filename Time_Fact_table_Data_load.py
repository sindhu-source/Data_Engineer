import psycopg2

#Database connection
con = None
    
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

    #Create a temp table to load time interval
        
    create_stmt = "CREATE TABLE IF NOT EXISTS time_temp (session_uuid VARCHAR NOT NULL,time_interval VARCHAR NOT NULL);"
    cur.execute(create_stmt)
    con.commit()

    #Inserting data into temp table 
    ins_temp = "insert into time_temp(session_uuid,time_interval) select e.session_uuid,max(created_at)-min(created_at) from events_dim e group by session_uuid;"
    cur.execute(ins_temp)
    con.commit()

    #Inserting data into Fact Table
    ins_fact = "insert into time_fact(country_uuid,verifier_uuid,session_uuid,events_uuid,time_interval) select distinct c.uuid,v.uuid,s.uuid,e.uuid,t.time_interval from countries_dim c inner join sessions_dim s on c.uuid = s.country_uuid inner join verifiers_dim v on v.uuid = s.verifier_uuid inner join events_dim e on e.session_uuid = s.uuid inner join time_temp t on t.session_uuid = s.uuid;"
    cur.execute(ins_fact)  
    con.commit()
    
    print("Data loaded Successfully into Fact table") 

    #Drop the temp table
    drop_temp = "DROP TABLE time_temp;"
    cur.execute(drop_temp)
    con.commit()

except psycopg2.DatabaseError as e:
    print("Error while loading data",e)
    quit()

finally:    
    #close the cursor
    cur.close()
    
    # Closing the Connection
    con.close()