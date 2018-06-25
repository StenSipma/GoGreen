from random import random
from flaskr.db import get_db


# class User:
#     """User class for information which is relevant for representation"""
#     _START_SCORE = 0

#     def __init__(self, name):
#         self.name = name
#         self.score = self._START_SCORE


class AccountUser():
    """User class for all account information, not relevant for other users"""
    _START_SCORE = 0

    def __init__(self, username, password, name, email,
                 street_name, street_number, city, postcode,
                 ean_energy, ean_gas):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.street_name = street_name
        self.street_number = street_number
        self.city = city
        self.postcode = postcode
        self.ean_energy = ean_energy
        self.ean_gas = ean_gas
        self.score = random() * 100

    def insert_in_db(self):
        db = get_db()
        db.execute("""INSERT INTO Users (username, password, name, email,
        street_name, street_number, city, postcode, ean_energy,
        ean_gas, score) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.username, self.password, self.name, self.email,
              self.street_name, self.street_number, self.city,
              self.postcode, self.ean_energy, self.ean_gas, self.score)
        )
        db.commit()


def parse_user_request(request):
    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    email = request.form['email']
    street_name = request.form['street_name']
    street_number = request.form['street_number']
    city = request.form['city']
    postcode = request.form['postcode']
    ean_energy = request.form['ean_energy']
    ean_gas = request.form['ean_gas']

    error = None
    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif not name:
        error = 'Name is required.'
    elif not email:
        error = 'Email is required.'
    elif not street_name:
        error = 'Street Name is required.'
    elif not street_number:
        error = 'Street Number is required.'
    elif not city:
        error = 'City is required.'
    elif not postcode:
        error = 'Postcode is required.'
    elif not ean_energy:
        error = 'EAN Energy number is required.'
    elif not ean_gas:
        error = 'EAN Gas number is required.'

    if error is None:
        return (AccountUser(username, password, name, email,
                            street_name, street_number, city, postcode,
                            ean_energy, ean_gas), None)
    return (None, error)


def query_user_rank(user_id):
    db = get_db()
    print(type(user_id))
    row = db.execute(
        "SELECT name, score FROM Users WHERE id = ?",
        (user_id,)
    ).fetchone()
    return row
