import mysql.connector

#Admin Module
#Global Variables Declaration
mydb=''
cursor=''
username=''
passwd=''
roomprice= 0
restaurentbill= 0
facilitiesbill= 0
venuebill= 0
total= 0
CID=0

#Module to check MySQL connectivity
def sqlconnection():
    global mydb
    global username
    global passwd
    username= input("\nEnter your MqSQL server's username:")
    passwd= input("\nEnter your MySQL server's password:")
    mydb= mysql.connector.connect(host= 'localhost', user= username, password= passwd)
    if mydb:
        print('\nYour MySQL connection has been established!')
        cursor= mydb.cursor()
        cursor.execute('Create database if not exists Pavitra')
        cursor.execute('COMMIT')
        cursor.close()
        return mydb
    else:
        print('\nError establishing MySQL connection! Check Username and Password.')

def mysqlconnect():
    global username
    global passwd
    global mydb
    global CID
    mydb= mysql.connector.connect(host= 'localhost', user=username, password= passwd, database= 'Pavitra', auth_plugin='mysql_native_password')
    if mydb:
        return mydb
    else:
        print('\nError establishing MySQL connection! Check Username and Password.')
        mydb.close()     
        
def userentry():
    global CID
    if mydb:
        cursor= mydb.cursor()
        createtable= '''create table if not exists Rambagh_CDet(CID varchar(20), C_NAME varchar(50),
C_ADDRESS varchar(30), C_AGE varchar(5), C_COUNTRY varchar(20), C_CONTACT varchar(30), C_EMAIL varchar(40))'''
        cursor.execute(createtable)
        CID= input("Enter Customer Identification Number:")
        Name= input("Enter Customer's Name: ")
        Address= input("Enter Customer's Address: ")
        Age= input("Enter Customer's Age: ")
        Nationality= input("Enter Customer's Nationality: ")
        Contactno= input("Enter Customer's Phone Number: ")
        Email= input("Enter Customer's Email Address: ")
        sql= "insert into Rambagh_CDet values(%s,%s,%s,%s,%s,%s,%s)"
        values= (CID, Name, Address, Age, Nationality, Contactno, Email)
        cursor.execute(sql, values)
        cursor.execute('COMMIT')
        print('\nNew Customer record entered in the system successfully.')
        cursor.close()
    else:
        print('\nError establishing MySQL connection! Check Username and Password.') #check message

def searchc():
    global CID
    if mydb:
        cursor= mydb.cursor()
        CID= input('Enter Customer ID:')
        sql= "select * from Rambagh_CDet where CID=%s"
        cursor.execute(sql,(CID,))
        data= cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print('Record not found. Try Again!')
            return False
        cursor.close()
    else:
        print('\nError establishing MySQL connection! Please Try Again.')
    
def bookingrec():
    global CID
    customer= searchc()
    if customer:
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Bookingrec(CID varchar(20),CHECKIN date,
CHECKOUT date)'''
            cursor.execute(createtable)
            checkin= input("\nEnter Customer's Check-in date [YYYY-MM-DD]: ")
            checkout= input("\nEnter Customer's Check-out date [YYYY-MM-DD]: ")
            sql= "insert into Rambagh_Bookingrec values(%s,%s,%s)"
            values= (CID, checkin, checkout)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print('\nCheck-in and Check-out entered successfully.')
            cursor.close()
        else:
            print('Error establishing MySQL connection! Please try again.')

def rooms():
    global CID
    customer= searchc()
    if customer:
        global roomprice
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Rooms(CID varchar(20),ROOM_CHOICES int,
DAYS int, ROOM_NO int, PRICE int)'''
            cursor.execute(createtable)
            print('\n======= We have the following rooms for you =======')
            print('===========     1. Palace Room (Rs. 37200)               ===========')
            print('===========     2. Historical Suite (Rs.46160)           ===========')
            print('===========     3. Royal Suite (Rs. 120000)              ===========')
            print('===========     4. Grand Royal Suite (Rs. 200000)        ===========')
            print('===========     5. Grand Presidential Suite (Rs. 760000) ===========')
            print('===========     6. Luxury Room (On request)              ===========')

            choice= int(input('Enter your choice: '))
            roomno= int(input('Enter Customer room no.: '))
            days= int(input('Enter no. of days of stay: '))
            if choice==1:
                roomprice= days*37200
                print('\nPalace Room price: ', roomprice)
            elif choice==2:
                roomprice= days*46160
                print('\nHistorical Suite price: ', roomprice)
            elif choice==3:
                roomprice= days*120000
                print('\nRoyal Suite price: ', roomprice)
            elif choice==4:
                roomprice= days*200000
                print('\nGrand Royal Suite price: ', roomprice)
            elif choice==5:
                roomprice= days*760000
                print('\nGrand Presidential Suite price: ', roomprice)
            elif choice==6:
                roomprice= 'Price upon request.'
                print('\nLuxury Room price: ', roomprice)
            else:
                print('Sorry. Please enter your choice correctly.')
                return
            sql= 'insert into Rambagh_Rooms values(%s,%s,%s,%s,%s)'
            values= (CID, choice, roomno, days, roomprice)
            cursor.execute(sql,values)
            cursor.execute('COMMIT')
            print('We hope you enjoy your stay.')
            cursor.close()
        else:
            print('\nError establishing MySQL connection! Please Try Again.')

def restaurent():
    global CID
    customer= searchc()
    if customer:
        global restaurentbill
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Dine(CID varchar(20), CUISINE varchar(30),
SERVING varchar(30), BILL varchar(30))'''
            cursor.execute(createtable)
            print('===========    1. Vegetarian Meal (Rs. 12000)     ===========')
            print('===========      a. Suvarna Mahal                 ===========')
            print('===========      b. Rajput Room                   ===========')
            print('===========    2. Non-vegetarian Meal (Rs. 15000) ===========')
            print('===========      a. Steam                         ===========')
            print('===========      b. Verandah Cafe                 ===========')
            print('===========      c. Polo Bar                      ===========')

            choice= input('Enter your choice: ')
            serving= 'BUFFET'
            if choice== '1a':
                restaurentbill= 12000
                print('\nDining at Suvarna Mahal: ', restaurentbill)
            elif choice== '1b':
                restaurentbill= 12000
                print('\nDining at Rajput Room: ', restaurentbill)
            elif choice== '2a':
                restaurentbill= 15000
                print('\nDining at Steam: ', restaurentbill)
            elif choice== '2b':
                restaurentbill= 15000
                print('\nDining at Verrandah Cafe: ', restaurentbill)
            elif choice== '2c':
                restaurentbill= 15000
                print('\nDining at Polo Bar: ', restaurentbill)
            else:
                print('Sorry. Please enter your choice correctly.')
                return
            sql= 'insert into Rambagh_Dine values(%s,%s,%s,%s)'
            values= (CID, choice, serving, restaurentbill)
            cursor.execute(sql,values)
            cursor.execute('COMMIT')
            print('Your Dining Bill is: Rs', restaurentbill)
            print('We hope you enjoy your meal.')
            cursor.close()
        else:
            print('\nError establishing MySQL connection! Please Try Again.')

def facilities():
    global CID
    customer= searchc()
    if customer:
        global facilitiesbill
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Facilities(CID varchar(20), FACILITY varchar(30),
HOURS varchar(30), BILL varchar(30))'''
            cursor.execute(createtable)
            print('===========      1. Polo       ===========')
            print('===========      2. Golf       ===========')
            print('===========      3. Swimming   ===========')
            print('===========      4. Billiards  ===========')
            print('===========      5. Bowling    ===========')
            print('===========      6. Quit       ===========')
            choice= int(input('Enter your choice: '))
            hours= int(input('Enter the number of hours: '))
            if choice==1:
                print('\nFacility: Polo')
                facilitiesbill= hours* 3000
            elif choice==2:
                print('\nFacility: Golf')
                facilitiesbill= hours* 1500
            elif choice==3:
                print('\nFacility: Swimming')
                facilitiesbill= hours* 1500
            elif choice==4:
                print('\nFacility: Billiards')
                facilitiesbill= hours* 2000
            elif choice==5:
                print('\nFacility: Bowling')
                facilitiesbill= hours* 2500
            elif choice==6:
                print('\nFacility: None')
                facilitiesbill= hours* 0
            else:
                print('Sorry. Please enter your choice correctly.')
                return
            sql= 'insert into Rambagh_Facilities values(%s,%s,%s,%s)'
            values= (CID, choice, hours, facilitiesbill)
            cursor.execute(sql,values)
            cursor.execute('COMMIT')
            print('\nYour facilities bill is: ', facilitiesbill)
            print('We hope you enjoy our facilities.')
            cursor.close()
        else:
            print('\nError establishing MySQL connection! Please Try Again.')

def venues():
    global CID
    customer= searchc()
    if customer:
        global venuebill
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Venues(CID varchar(20), VENUE varchar(50),
PRICE varchar(30), BILL varchar(30))'''
            cursor.execute(createtable)
            print('=============    1. Maharani Mahal      =============')
            print('=============    2. Panghat Lawn        =============')
            print('=============    3. Mughal Garden       =============')
            print('=============    4. Chamber of Princes  =============')
            print('=============    5. Oriental Garden     =============')
            print('=============    6. Chandra Mahal       =============')
            print('=============    7. Quit                =============')
            choice= int(input('Enter your choice: '))
            hours= int(input('Enter the number of hours you want to book the venue for: '))
            if choice==1:
                print('\nVenue: Maharani Mahal')
                venuebill= hours* 10000
            elif choice==2:
                print('\nVenue: Panghat Lawn')
                venuebill= hours* 6000
            elif choice==3:
                print('\nVenue: Mughal Garden')
                venuebill= hours* 4500
            elif choice==4:
                print('\nVenue: Chamber of Princes')
                venuebill= hours* 3000
            elif choice==5:
                print('\nVenue: Oriental Garden')
                venuebill= hours* 8000
            elif choice==6:
                print('\nVenue: Chandra Mahal')
                venuebill= hours* 9000
            elif choice==7:
                print('\nVenue: None')
                venuebill= hours* 0
            else:
                print('Sorry. Please enter your choice correctly.')
                return
            sql= 'insert into Rambagh_Venues values(%s,%s,%s,%s)'
            values= (CID, choice, hours, venuebill)
            cursor.execute(sql,values)
            cursor.execute('COMMIT')
            print('\nYour Venue bill is: ', venuebill, 'for Venue no.: ', choice)
            print('We hope you enjoy the occassion.')
            cursor.close()
        else:
            print('\nError establishing MySQL connection! Please Try Again.')

def totalbill():
    global CID
    customer= searchc()
    if customer:
        global total
        global roomprice
        global restaurentbill
        global facilitiesbill
        global venuebill
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Total(CID varchar(20), C_NAME varchar(30), ROOM_PRICE int,
RESTAURENT_BILL int, FACILITIES_BILL int, VENUE_BILL int, TOTAL_AMOUNT int)'''
            cursor.execute(createtable)
            sql= 'insert into Rambagh_Total values(%s,%s,%s,%s,%s,%s,%s)'
            name= input("Enter Customer's Name: ")
            grandtotal= roomprice+ restaurentbill+ facilitiesbill+ venuebill
            values= (CID, name, roomprice, restaurentbill, facilitiesbill, venuebill, grandtotal)
            cursor.execute(sql,values)
            cursor.execute('COMMIT')
            cursor.close()
            print('\n*************** Rambagh Palace Hotel, Jaipur ***************')
            print('***************         BILL          ***************')
            print("Customer's Name: ", name)
            print("Room bill: Rs.", roomprice)
            print("Restaurent bill: Rs.", restaurentbill)
            print("Facilities bill: Rs.", facilitiesbill)
            print("Venue bill: Rs.", venuebill)
            print('-------------------------------------------------')
            print('Net bill: Rs.', grandtotal)
            cursor.close()
        else:
            print('\nError establishing MySQL connection! Please Try Again.')

def searcholdbill():
    global CID
    customer= searchc()
    if customer:
        if mydb:
            cursor= mydb.cursor()
            sql= 'select * from Rambagh_Total where CID=%s'
            cursor.execute(sql,(CID,))
            data= cursor.fetchall()
            if data:
                print(data)
            else:
                print('Record Not Found. Try Again!')
                cursor.close()
        else:
            print('\nError establishing MySQL connection! Please Try Again.')
    


def adminmode():
    mydb= sqlconnection()
    if mydb:
        mysqlconnect()
        while(True):
            print('''
*************  1. Enter Customer Details    *************
*************  2. Booking Record            *************
*************  3. Calculate Room Price      *************
*************  4. Calculate Restaurent Bill *************
*************  5. Calculate Facilities Bill *************
*************  6. Calculate Venue Bill      *************
*************  7. Display Customer Details  *************
*************  8. Calculate total bill      *************
*************  9. Search old bills          *************
*************  10. Exit                     *************''')
            choice= int(input('Enter your choice: '))
            if choice==1:
                userentry()
            elif choice==2:
                bookingrec()
            elif choice==3:
                rooms()
            elif choice==4:
                restaurent()
            elif choice==5:
                facilities()
            elif choice==6:
                venues()
            elif choice==7:
                searchc()
            elif choice==8:
                totalbill()
            elif choice==9:
                searcholdbill()
            elif choice==10:
                break
            else:
                print('Sorry. Please enter your choice correctly.')
    else:
        print('\nError establishing MySQL connection! Please Try Again.')
        

def cuserentry():
    global CID
    if mydb:
        cursor= mydb.cursor()
        createtable= '''create table if not exists Rambagh_CDet(CID varchar(20), C_NAME varchar(50),
C_ADDRESS varchar(30), C_AGE varchar(5), C_COUNTRY varchar(20), C_CONTACT varchar(30), C_EMAIL varchar(40))'''
        cursor.execute(createtable)
        CID= input("Enter Customer Identification Number:")
        Name= input("Enter your Name: ")
        Address= input("Enter Customer's Address: ")
        Age= input("Enter your Age: ")
        Nationality= input("Enter your Nationality: ")
        Contactno= input("Enter your Phone Number: ")
        Email= input("Enter your Email Address: ")
        sql= "insert into Rambagh_CDet values(%s,%s,%s,%s,%s,%s,%s)"
        values= (CID, Name, Address, Age, Nationality, Contactno, Email)
        cursor.execute(sql, values)
        cursor.execute('COMMIT')
        print('\nNew Customer record entered in the system successfully.')
        cursor.close()
    else:
        print('\nError establishing MySQL connection! Check Username and Password.') #check message

def cbookingrec():
    global CID
    customer= searchc()
    if customer:
        if mydb:
            cursor= mydb.cursor()
            createtable= '''create table if not exists Rambagh_Bookingrec(CID varchar(20),CHECKIN date,
CHECKOUT date)'''
            cursor.execute(createtable)
            checkin= input("/n Enter your Check-in date [YYYY-MM-DD]: ")
            checkout= input("/n Enter your Check-out date [YYYY-MM-DD]: ")
            sql= "insert into Rambagh_Bookingrec values(%s,%s,%s)"
            values= (CID, checkin, checkout)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print('\nCheck-in and Check-out entered successfully.')
            cursor.close()
        else:
            print('Error establishing MySQL connection! Please try again.')

def customermode():
    mydb= sqlconnection()
    if mydb:
        mysqlconnect()
        while(True):
            print('''
*************  1. Create an account                *************
*************  2. Book a Stay                      *************
*************  3. Check Details of recent Booking  *************
*************  4. Check Details of older Bookings  *************
*************  5. Exit                             *************''')
            choice= int(input('Enter your chhoice: '))
            if choice==1:
                cuserentry()
            if choice==2:
                cbookingrec()
                rooms()
                restaurent()
                facilities()
                venues()
                totalbill()
            if choice==3:
                totalbill()
            if choice==4:
                searcholdbill()
            if choice==5:
                print('Thank you for booking with us. We hope you enjoy!')
                break

while True:
    print("*************************************************************")
    print("=========== WELCOME TO RAMBAGH PALACE HOTEL, JAIPUR ============")
    print("=========== PROJECT BY- PAVITRA BHARGAVI ALLAMARAJU ============")
    print("===========               GRADE-XII A               ============")
    print("===========   BRIGHT RIDERS SCHOOL, ABU DHABI, UAE  ============")
    print("*************************************************************")
    print('''\n
*************   1. Admin Mode     *************
*************   2. Customer Mode  *************''')
    choice= int(input('Enter your choice: '))
    if choice==1:
        adminmode()
    if choice==2:
        customermode()
            

    
