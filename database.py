import sqlite3

connection = sqlite3.connect('SalebotBase.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS complex'
            '(complex_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'rooms INTEGER,'
            'floor INTEGER,'
            'sq_meters INTEGER,'
            'price INTEGER,'
            'photo TEXT);')
connection.commit()

sql.execute('CREATE TABLE IF NOT EXISTS clients'
            '(user_id INTEGER,'
            'number INTEGER,'
            'reg_date DATETIME);')
connection.commit()


class Data:
    def __init__(self):
        self.connection = sqlite3.connect('SalebotBase.db')
        self.sql = self.connection.cursor()

    # Registration
    def registration(self, user_id, number, reg_date):
        self.sql.execute('INSERT INTO clients VALUES (?,?,?);', (user_id, number, reg_date))
        self.connection.commit()

    # Check user in base
    def check_user(self, user_id):
        checker = self.sql.execute('SELECT user_id FROM clients WHERE user_id = ?;', (user_id))

        if checker.fetchone():
            return True
        else:
            return False

    # Add complex to base from admin side

    def complex_add(self, name, rooms, floor, sq_meters, price, photo):
        self.sql.execute('INSERT INTO complex(name,rooms,floor,sq_meters,price,photo) VALUES (?,?,?,?,?,?);',
                         (name, rooms, floor, sq_meters, price, photo))
        self.connection.commit()

    # Complex delite

    def delite_comlex(self, name, complex_id):
        self.sql.execute('DELETE FROM complex WHERE name = ? AND complex_id = ?;', (name, complex_id))
        self.connection.commit()
    # Show base

    def show_all(self):
        complex = self.sql.execute('SELECT * FROM complex;', ).fetchall()
        return complex

    # Clients base
    def show_clients(self):
        clients = self.sql.execute('SELECT * FROM clients;').fetchall()
        return clients
