import sys

def convert_args(a):
    args = {}
    for i in range(0, len(a), 2) :
        name = a[i][1:] if a[i][0] == "-" else a[i]
        args[name] = a[i+1]
    return args

args = convert_args(sys.argv[1:])


if args['M'] == 'GET':
    print("Enter your file you want to read in the /home dir")
    print("format: \"-p path\"")
elif args['M'] == 'POST':
    path = args['p']
    if not path:
        print ("No input")
    else:
        fullPath = "/home" + path
        f = open(fullPath, "r")
        print(f.read())
