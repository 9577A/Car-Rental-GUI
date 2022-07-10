import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='Car_Rental_Company'
)
mycursor = db.cursor()


current_date = datetime.now()
date = current_date.date()
date_time = datetime.strptime(f'{date}', '%Y-%m-%d')


# function creates new user and adds him to dabatabse
def add_client(name, surname, login, password, driving_license): # dodać jeżeli nie istnieje
    mycursor.execute("INSERT INTO users (name, surname, login, password, driving_licence) VALUES(%s,%s,%s,%s,%s)",
                     (name.capitalize(), surname.capitalize(), login, password, driving_license))
    db.commit()


# dodanie osoby ze złymi danymi (nie doda się osoba, jednak doda się user_id)
class Client:
    def __init__(self, client_id):
        self.client_id = client_id
        mycursor.execute(f'SELECT name, surname, login, password, driving_licence FROM users WHERE user_id = "{client_id}"')
        data = mycursor.fetchall()[0]
        self.name = data[0]
        self.surname = data[1]
        self.login = data[2]
        self.password = data[3]
        self.driving_license = data[4]

    def rent_car(self, car_id, first_day, last_day):
        last_day = last_day[:-2] + '20' + last_day[-2:]
        first_day = first_day[:-2] + '20' + first_day[-2:]

        first_date = datetime.strptime(first_day, '%d/%m/%Y')
        last_date = datetime.strptime(last_day, '%d/%m/%Y')

        # set car_number to number of specific car
        mycursor.execute(f'SELECT car_number FROM cars WHERE car_id = {car_id}')
        car_number = mycursor.fetchone()[0]

        # set rented_number to number of cars already rented in given time phase
        rent_dates = [car_id, first_date, first_date, last_date, last_date, first_date, last_date]
        mycursor.execute("SELECT COUNT(car_id) FROM rents WHERE car_id = %s AND ((first_date <= %s AND %s <= last_date) OR (first_date <= %s AND %s <= last_date) OR (%s <= first_date AND last_date <= %s))", rent_dates)
        rented_number = mycursor.fetchone()[0]
        print(car_number, rented_number)
        if date_time <= first_date <= last_date and car_number > rented_number:
            # create INSERT of new row in table rents
            new_rents_row = "INSERT INTO rents(user_id, car_id, first_date, last_date) VALUES (%s, %s, %s, %s)"
            # create tuple containing data we insert into row rents
            inserted_data = [self.client_id, car_id, first_date, last_date]

            mycursor.execute(new_rents_row, inserted_data)
            db.commit()
            print("YES", car_id)
            return "You've rented a car"
        #inserted_data = [self.client_id, car_id, first_day, last_day]
        print("NO", car_id)
        return "Sorry, You can't do it"

    def all_rents(self):
        mycursor.execute('SELECT cars.car_brand, cars.car_model, first_date, last_date FROM rents, cars '
                         f'WHERE user_id = {self.client_id} AND cars.car_id = rents.car_id')
        rents_table = mycursor.fetchall()
        mycursor.execute(f'SELECT COUNT(user_id) FROM rents WHERE user_id = {self.client_id}')
        number_rents = mycursor.fetchone()[0]

        rents_table = [(rents_table[i][0] + ' ' + rents_table[i][1], rents_table[i][2].strftime("%d %b, %Y"),
                        rents_table[i][3].strftime("%d %b, %Y")) for i in range(number_rents)]
        return rents_table

    def password_change(self, new_password):
        mycursor.execute(f'UPDATE users SET password = "{new_password}" WHERE login = "{self.login}"')
        db.commit()

"""
class Car():
    def __init__(self, car_brand, car_model, production_year, driving_lic_required, car_type, weekday_cost):
        # car_id (klasa powinna przyjmować jedynie id auta, i automatycznie znajdywać pozostałe wartości)
        self.car_brand = car_brand
        self.car_model = car_model
        self.production_year = production_year
        self.driving_lic_required = driving_lic_required
        self.car_type = car_type
        self.weekday_cost = weekday_cost

    def remove(self):
        pass

    def is_avalible(self):
        pass

    def rent(self, first_day, last_day):
        mycursor.execute("INSERT INTO rents (")

    def cancel_rent(self):
        pass
"""

def log_me_in(login):
    mycursor.execute("SELECT user_id, login, password FROM users WHERE login = %s", [f"{login}"])
    id_user, lg, pssw = mycursor.fetchone()
    return id_user, lg, pssw


# !!!! NIE POTRZEBNE !!!!
def person_info(id_user):
    mycursor.execute("SELECT name, surname, login, password, driving_licence  FROM users WHERE user_id = %s", [id_user])
    name, surname, login, password, driving_licence = mycursor.fetchone()
    return name, surname, login, password, driving_licence


# returns brand, model, cost of rent and required licence of car with given id
def car_info(id_car):
    mycursor.execute("SELECT car_brand, car_model, car_number, rent_cost, driving_licence_required", [id_car])
    brand, model, number, cost, licence = mycursor.fetchone()
    return brand, model, cost, licence





# creates list of unique records of car brands (from TABLE cars)
def car_brand_all():
    mycursor.execute(f"SELECT DISTINCT car_brand FROM cars")
    col = [item[0] for item in mycursor.fetchall()]
    col.insert(0, 'ALL')
    return col


# creates list of unique records of car models or certain car brand (from TABLE cars)
def car_model_all(brand):
    if brand in ["ALL", None, '']:
        brand = "IS NOT NULL"
    else:
        brand = f'= "{brand}"'
    mycursor.execute(f"SELECT DISTINCT car_model FROM cars WHERE car_brand {brand}")
    col = [item[0] for item in mycursor.fetchall()]
    col.insert(0, 'ALL')
    return col


# returns a list of cars, which #(spełniają wymagania)
def car_table(marka='', model='', from_time='', to_time='', min_cost='', max_cost=''):
    table = [marka, model]
    # create list of ajusted arguments
    columns = ["IS NOT NULL" if item in ['', None, "ALL", "PY_VAR2"] else f'= "{item}"' for item in table]
    min_cost = "IS NOT NULL" if min_cost in ['', None, "ALL", "PY_VAR2"] else f">= {min_cost}"
    max_cost = "IS NOT NULL" if max_cost in ['', None, "ALL", "PY_VAR2"] else f"<= {max_cost}"
    # query database with adjusted arguments
    mycursor.execute(f"SELECT car_brand, car_model, rent_cost FROM cars WHERE car_brand {columns[0]} "
                     f"AND rent_cost {min_cost} AND rent_cost {max_cost}")#nie "BMW" tylko " = BMW" albo NOT NULL
    table = mycursor.fetchall()
    return table


# function takes car brand and model and return this specific car_id
def what_car_id(brand, model):
    mycursor.execute(f'SELECT car_id FROM cars WHERE car_brand = "{brand}" AND car_model = "{model}"')
    return mycursor.fetchone()[0]
