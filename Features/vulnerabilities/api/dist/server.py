"""
Generic REST Server implementation
"""
from os import environ
import os
import re
import subprocess
from flask import Flask, abort, request

app = Flask(__name__)

PREFIX = environ.get("REST_PREFIX", "B4IoT")
extensionsMap = {".py": ["python3"], ".jar": ["java", "-jar"], ".bin": ["./"]}


def check_path(path):
    for resource in app_paths.keys():
        print(resource)
        match = re.match(app_paths[resource]["re"], path)
        print(match)
        if match:
            return resource
    abort(404)

def parse_path_parameters(resource, path):
    """parse parameters provided in path uri"""
    res = list()
    match = re.match(app_paths[resource]["re"], path)
    if match:            
        grps = match.groupdict()
        for grp in grps:
            res.append("-" + grp)
            res.append(grps[grp])
    return res



def get_data(resource):
    """Convert Request to parameters"""
    # general parameters
    args = ["-M", request.method]
    # path parameters
    print(args)
    args.extend(parse_path_parameters(resource, request.path))
    # form data
    print(args)
    args.extend([x for l in [["-{}".format(x), request.form[x]]
                for x in request.form.keys()] for x in l])
    # take body
    print(args)
    if request.data != b'':
        args.extend(["-P", str(request.data, "utf-8")])
    # query arguments
    print(request.args)
    for arg in request.args.keys():
        args.extend([arg, request.args[arg]])
    
    print(args)
    return args



@app.route('/', defaults={'path': ''},methods=['GET','POST'])
@app.route('/<path:path>',methods=['GET','POST'])
def call(path):
    """Provide general call to vulnerabilities"""
    print(path)
    if path == PREFIX+"/":
        return str(list_paths())
    # check if path supported and parse uri parameters
    resource = check_path("/"+path)
    print(resource)
    ext = os.path.splitext(resource)[1]
    cmd = extensionsMap[ext].copy()
    print(cmd)
    cmd.append(resource)
    print(cmd)
    cmd.extend(get_data(resource))
    print(cmd)
    try:
        return subprocess.check_output(cmd)
    except subprocess.CalledProcessError:
        abort(404)


app_paths = {}


def list_paths():
    """list the paths provided by the features"""
    return [app_paths[k]["resource_path"] for k in app_paths]


def add_dir(path):
    """Add vulnerabilities in the VULNS path"""
    for file in os.listdir(path):
        fullpath = os.path.join(path, file)
        if os.path.isfile(fullpath):
            if os.path.splitext(file)[1] in extensionsMap:
                # resource path:
                resource_path = os.path.splitext(fullpath)[0]
                # replace prefix:
                resource_path = resource_path.replace(PATH, "/" + PREFIX) + "/"
                # check existance of path file
                path_file = fullpath + ".pt"
                if os.path.exists(path_file):
                    with open(path_file, "r", encoding="utf-8") as reader:
                        resource_path = resource_path.replace(
                            os.path.splitext(file)[0] + "/", str(reader.read()))
                print("Adding rule {}".format(resource_path))
                app_paths[fullpath] = {
                    "resource_path": resource_path,
                    "re": "^" + re.sub("(<[^/]*?>)", r"(?P\1[^/]*)", resource_path) + "$"
                }
        else:
            add_dir(fullpath)


if __name__ == '__main__':
    PATH = "/opt/dvd/services/vulns"
    add_dir(PATH)
    app.run()
