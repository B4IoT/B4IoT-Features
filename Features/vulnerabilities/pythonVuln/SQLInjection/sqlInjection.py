import sqlite3
import os

class User():
    def __init__(self, id, email, password):
        self.id = (id)
        self.email = email
        self.password = password
        self.authenticated = False

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id

conn = sqlite3.connect('login.db')
curs = conn.cursor()
data = input("Enter your email")
passw = input("Enter your password")
#print(" \"SELECT * FROM login where email = '%s' and password = '%s'\" " % (data, passw))
curs.execute("SELECT * FROM login where email = '%s' and password = '%s'" % (data, passw))
data = curs.fetchone()
#print(data)

def load_user(user_id):
    conn = sqlite3.connect('login.db')
    curs = conn.cursor()
    curs.execute("SELECT * from login where id = (?)", [user_id])
    lu = curs.fetchone()
    if lu is None:
        return None
    else:
        return User(int(lu[0]), lu[1], lu[2])

if data is not None:
    #user = list(curs.fetchone())
    Us = load_user(data[0])
    # if form.email.data == Us.email and form.password.data == Us.password:
    if data == Us.email and passw == Us.password:
        Umail = list({data})[0].split('@')[0]
        print("data does exist")
        print("personal secret")
        #   else:
        #       flash('Login Unsuccessfull.')
    else:
        print("User " + data + " does not exist")

else:
    print("User " + data + " does not exist")

