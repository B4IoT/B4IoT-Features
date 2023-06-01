#https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Python.md
import cPickle
from base64 import b64encode, b64decode

class User:
    def __init__(self):
        self.username = "anonymous"
        self.password = "anonymous"
        self.rank     = "guest"

h = User()
new_token = raw_input("New Auth Token : ")
token = cPickle.loads(b64decode(new_token))
print ("Welcome " + format(token.username))

