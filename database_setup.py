import mysql.connector


"""
#
cr = mysql.connector.connect(
    host='localhost',	#your host name
    user='root',	#your user name
    password='root' #your password
)
crcursor = cr.cursor()
crcursor.execute("CREATE DATABASE Car_Rental_Company")
"""

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='Car_Rental_Company'
)

mycursor = db.cursor()

# creates table users which contains all company users
mycursor.execute("CREATE TABLE users ("
	"user_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "name VARCHAR(50) NOT NULL,"
    "surname VARCHAR(50) NOT NULL,"
    "login VARCHAR(30) NOT NULL UNIQUE,"
    "password VARCHAR(30) NOT NULL,"
    "driving_licence VARCHAR(10),"
    "CONSTRAINT chk_licence CHECK (driving_licence IN ('B', 'C', 'C1'))"
");"
                 )

# creates cars table containing specific cars and number of those specific cars
mycursor.execute("CREATE TABLE cars ("
	"car_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "car_brand VARCHAR(50) NOT NULL,"
    "car_model VARCHAR(50) NOT NULL,"
    "car_number INTEGER NOT NULL,"
    "rent_cost INTEGER NOT NULL,"
    "driving_licence_required VARCHAR(3) NOT NULL,"
    "CONSTRAINT chk_licence_required CHECK (driving_licence_required IN ('B', 'C', 'C1'))"
");"
                 )

# creates tabl rents containing all cars which have been booked
mycursor.execute("CREATE TABLE rents ("
	"rent_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "user_id INTEGER NOT NULL,"
    "car_id INTEGER NOT NULL,"
    "first_date DATE,"
    "last_date DATE,"
    "FOREIGN KEY (user_id) REFERENCES users(user_id),"
    "FOREIGN KEY (car_id) REFERENCES cars(car_id)"
");"
                 )
