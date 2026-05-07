#Name: Katlyn Lucis
#Assignment: SQL and Python
#Reflection:  Share what you liked about this assignment:  I enjoyed the creation of the db along with the usefulness
#             of our last lesson (classes) showing up here.  It really helped understand using the different properties of SQLite3.

#             Share what you struggled with:  At first I was really struggling with Join not appearing to join anything.  I was using
#             DB Browser to verify what was happening in the DB, and did not realize join doesnt physcially change the tables unless used in
#             conjuction with create.

#             In your own words how does the DDL and DML Statments work and how you used them:  DDL (Data Definition Language) statements
#             in the project were all the ones that define the database and its creation.  The execute statements with CREATE TABLE all work
#             in defining the tables by stating what values their columns will include, and what form those values will take.  ALTER is also
#             included in DDL since it changes the defintion of the original table (in this case it is used to add a column).  DML (Data
#             Manipulation Language) was used to add data to our previously defined tables, and then to further manipulate said data.  JOIN,
#             INSERT, and UPDATE are all considered DML.   

#             In your own words describe how the SQL Select Joins work in your code:  After the initial tables are created from the supplied
#             .txt document, Select and Left Join were used in conjunction with Create make a new table.  In the statement, the tables are all 
#             assigned a, b, or c to simplify referring to their matching columns.  The FROM table is considered the "left" table, and the
#             LEFT JOIN refers to what is the "right" table.  In the case of the first portion of the statement, the Employee is joined to
#             the Pay table from the left, using the EmployeeID column as the reference.  After, the two joined tables are left joined again
#             to the SocialSecurityMin table, using the Year column as a reference.

#             Share exactly 2 things you learned on this assignment:
#             1. There are far more than just 2, but the two primary ones would be learning all of the string statements that are passed
#             sqlite3 to manipulate the database.  It almost reminds me of writing out psuedo code since the logic and syntax seem
#             much more general than typical sytax of other languages I have seen thus far.
#             2. I had read about SQL Injection attacks prior to this in my Windows course, but actually writing code and understanding
#             variables better, it makes sense how an attack could utilize an input to inject malicious code.  Understanding the "why"
#             has always been very important to my learning process so I really appreciate gaining a deeper understanding of how it all works.
import sqlite3

def main():

    conn = sqlite3.connect('Project.db')
    cur = conn.cursor()

    #Tables are created with a try method to avoid duplication.  If the tables exist, this section will throw an exception and pass.
    try:
        cur.execute('''CREATE TABLE Employee(EmployeeID INTEGER, Name TEXT)''')
        cur.execute('''CREATE TABLE Pay(EmployeeID INTEGER, Year INTEGER, Earnings INTEGER)''')
        cur.execute('''CREATE TABLE SocialSecurityMin(Year INTEGER, Minimum INTEGER)''')
        #Tables are populated with the PopulateTable function.
        PopulateTable(cur, 'Employee', 'EmployeeID, Name', '?,?')
        PopulateTable(cur, 'Pay', 'EmployeeID, Year, Earnings', '?,?,?')
        PopulateTable(cur, 'SocialSecurityMin', 'Year, Minimum', '?,?')
        #The existing tables are joined together to create a results table for easier manipulation and reporting.
        cur.execute('''CREATE TABLE Results AS
                    SELECT a.EmployeeID, a.Name, b.Year, b.Earnings, c.Minimum
                    FROM Employee AS a
                    LEFT JOIN Pay AS b ON a.EmployeeID = b.EmployeeID
                    LEFT JOIN SocialSecurityMin AS c ON b.Year = c.Year;''')
        #The newly created results table is given an Include column for the yes/no results.
        cur.execute('''ALTER TABLE Results ADD COLUMN Include TEXT''')
        #The Include column is updated include a Yes or No based on the relation of the Earnings column to the Minimum column.
        cur.execute('''UPDATE Results
                    SET Include = CASE
                    WHEN Earnings >= Minimum THEN 'Yes'
                    WHEN Earnings < Minimum THEN 'No'
                    END;''')

    #Exception order matters!
    #The SocialSecurityMinimum file was changed to SocialSecurityMin to allow the function to work. This exception
    #will handle if the old file is attempted to be used.  
    except FileNotFoundError as Error:
        #The error message is printed showing which file was not found.
        print(Error)
        #All of the tables are cleared to prevent other duplication errors when program is rerun.
        cur.execute('''DROP TABLE IF EXISTS Employee''')
        cur.execute('''DROP TABLE IF EXISTS Pay''')
        cur.execute('''DROP TABLE IF EXISTS SocialSecurityMin''')
        conn.commit()
        conn.close()
        raise SystemExit()
    #This exception will handle if the tables were already created and pass to the reporting section of the program.
    except sqlite3.OperationalError:
        pass

    #All of the data is selected and ordered alphabetically based on the Name column.
    cur.execute("SELECT * FROM Results ORDER BY Name")
    #The header variable is created with the .description of each column.
    header = [header[0] for header in cur.description]
    #The headers are printed for the respective columns.  Position [0] is skipped as it is the Employee ID.
    print(f"{header[1]:16} {header[2]:6} {header[3]:11} {header[4]:7} {header[5]:3}")
    #The report for each row is assigned to row.
    row = cur.fetchone()
    while row != None:
        #While there are existing rows, the program repeats through each column.
        print(f"{row[1]:15} {row[2]:5} {row[3]:10} {row[4]:10} {row[5]:3}")
        row = cur.fetchone()

    #Changes are committed and the connection to the database is closed.
    conn.commit()
    conn.close()

#PopulateTable is defined.  This function receives the cur variable, the FileName to be accessed,
#The VariablesString that will include the column names, and the ValueNumber which represents the
#number of ? values to be passed to the table.
def PopulateTable(cur, FileName, VariablesString, ValueNumber):
    with open(FileName+'.txt', 'r') as fileIn:
        #The first line of the text file is passed so as to not add the headers.
        passHeading = fileIn.__next__()
        for row in fileIn:
            #The information from the text is stripped of any blank spaces, and split based on the "," that were used for seperation.
            info = row.strip().split(',')
            #The data is inserted into its corrisponding table, column, and values into the row based on the number of lines in the text document.
            cur.execute(f"INSERT INTO {FileName} ({VariablesString}) VALUES ({ValueNumber})",(info))

main()

