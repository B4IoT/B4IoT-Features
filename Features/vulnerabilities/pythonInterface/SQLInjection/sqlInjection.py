import sqlite3
import os
import sys

path = os.path.realpath(__file__)
path = os.path.dirname(path)
os.chdir(path)

def convert_args(a):
    args = {}
    for i in range(0, len(a), 2) :
        name = a[i][1:] if a[i][0] == "-" else a[i]
        args[name] = a[i+1]
    return args


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

args = convert_args(sys.argv[1:])
if args['M'] == 'GET':
    print("Enter your username and password to get acces to your personal data")
    print("format: \"-user username -pass password\"")
elif args['M'] == 'POST':
    conn = sqlite3.connect(path + '/login.db')
    curs = conn.cursor()
    email = args['user']
    passw = args['pass']
    #print(" \"SELECT * FROM login where email = '%s' and password = '%s'\" " % (data, passw))
    curs.execute("SELECT * FROM login where email = '%s' and password = '%s'" % (email, passw))
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
        if data[1] == Us.email and data[2] == Us.password:
            #Umail = list({data})[0].split('@')[0]
            print("data does exist")
            print("personal secret")
            #   else:
            #       flash('Login Unsuccessfull.')
        else:
            print("User " + str(email) + " does not exist")

    else:
        print("User " + str(email) + " does not exist")


