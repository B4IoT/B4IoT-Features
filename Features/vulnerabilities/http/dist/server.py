from flask import Flask, app
from flask import render_template, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from forms import LoginForm, updateForm
import ssl
import os
path = os.path.realpath(__file__)
path = os.path.dirname(path)
os.chdir(path)

app = Flask(__name__)

app.debug = True

login_manager = LoginManager(app)

login_manager.login_view = "login"

credential_path = "/etc/credentials"


class User(UserMixin):
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

    def change_email(self, email):
        self.email = email


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('login.db')
    curs = conn.cursor()
    curs.execute("SELECT * from login where id = (?)", [user_id])
    lu = curs.fetchone()
    if lu is None:
        return None
    else:
        return User(int(lu[0]), lu[1], lu[2])


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect('login.db')
        curs = conn.cursor()
        data = form.email.data
        passw = form.password.data
        #print(" \"SELECT * FROM login where email = '%s' and password = '%s'\" " % (data, passw))
        curs.execute("SELECT * FROM login where email = '%s' and password = '%s'" % (data, passw))
        data = curs.fetchone()
        #print(data)
        if data is not None:
            #user = list(curs.fetchone())
            Us = load_user(data[0])
            # if form.email.data == Us.email and form.password.data == Us.password:
            login_user(Us, remember=form.remember.data)
            Umail = list({form.email.data})[0].split('@')[0]
            return redirect(url_for('profile'))
         #   else:
         #       flash('Login Unsuccessfull.')
        else:
            flash("User " + form.email.data + " does not exist")
    return render_template('login.html', title='Login', form=form)

@app.route("/", methods=['GET'])
def redirection():
    return redirect(url_for("login"))


@app.route("/profile", methods=['GET','POST'])
@login_required
def profile():
    #print("login successful")
    con = sqlite3.connect("priv.db")
    con.row_factory = sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from priv")
    rows = cur.fetchall()
    formUpdate = updateForm()
    if formUpdate.validate_on_submit():
        print("current id user " +str(current_user.id))
        conn = sqlite3.connect('login.db')
        curs = conn.cursor()
        email = formUpdate.email.data
        #print(" \"SELECT * FROM login where email = '%s' and password = '%s'\" " % (data, passw))

        print("updating user "+current_user.email +" to " + email)
        curs.execute("UPDATE login SET email = '%s' WHERE id = '%s'" % (email,current_user.id))
        conn.commit()
        print("Done")

        curs.execute("SELECT * FROM login where id = '%s' " % (current_user.id))
        data = curs.fetchone()
        Us = load_user(data[0])
        print("user is now " + str(Us.id) + " " + str(Us.email) + " " + str(Us.password))
    return render_template('profile.html', title='profile', rows=rows, form=formUpdate)

    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/admin_remarks", methods=['POST', 'GET'])
def admin_remarks():

    db_file = "comments.txt"
    file = os.path.dirname(path) + "/" + db_file
    print(file)
    if not os.path.isfile(file):
        f = open("comments.txt","w")

    if request.method == 'POST':
        comment = request.form["comment"]
        
        with open(db_file, "a") as f:
            f.write(comment+"\n")
        
    comments = ""
    with open(db_file, "r+") as f:
        for line in f.readlines():
            comments+=f"<div>{line}</div>"

    page = f"""
        <html>
        <head></head>
        <body>
            <h>Under development!</h>
            <form action="#" method="POST">
                <input type="text" id="comment" name="comment"><br><br>
                <input type="submit" value="Submit">
            </form>
            {comments}
        </body>
        </html> 
    """
    return page


def main():
   
    app.config.update(dict(
        SECRET_KEY="powerful secretkey",
   #     WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #setup SSL configuration
    context.load_verify_locations(cafile="{path}/root.cer".format(path = credential_path),capath=None,cadata=None)
    context.load_cert_chain('{path}/server.cer'.format(path = credential_path), '{path}/server.key'.format(path = credential_path))
    app.run(ssl_context=context,host="0.0.0.0",  port=443, threaded=True)
   # app.run(port=80,threaded=True)

if __name__ == "__main__":
    main()