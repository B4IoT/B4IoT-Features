#https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Python.md
import cPickle
from base64 import b64encode, b64decode

def convert_args(a):
    args = {}
    for i in range(0, len(a), 2) :
        name = a[i][1:] if a[i][0] == "-" else a[i]
        args[name] = a[i+1]
    return args


class User:
    def __init__(self):
        self.username = "anonymous"
        self.password = "anonymous"
        self.rank     = "guest"

args = convert_args(sys.argv[1:])
if args['M'] == 'GET':
    print("Enter your token to authenticate")
    print("format: \"-t token\"")
elif args['M'] == 'POST':
    h = User()
    new_token = str(args['P'])
    token = cPickle.loads(b64decode(new_token))
    print ("Welcome " + format(token.username))

