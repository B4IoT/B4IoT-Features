import sys

def convert_args(a):
    args = {}
    for i in range(0, len(a), 2) :
        name = a[i][1:] if a[i][0] == "-" else a[i]
        args[name] = a[i+1]
    return args

args = convert_args(sys.argv[1:])


if args['M'] == 'GET':
    print("Enter your calculation you want to compute")
    print("format: \"-c Calculation\"")
elif args['M'] == 'POST':
    compute = args['c']
    if not compute:
        print ("No input")
    else:
        print ("Result =", eval(compute))
