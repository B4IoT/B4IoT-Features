#!/usr/bin/env python3

"""
This file should be search for Json files in the backend and make one big file of them, automating the development of the big config file
"""

import os
import json

def make():
    # Read small JSON files
    directory = './Features'
    config = ""
    jsonfiles = []
    print("Starting....")
    for type in os.listdir(directory):
        if os.path.isdir(directory + "/" + type):
            print(type)
            for feature in os.listdir(directory + "/" + type):
                if os.path.isdir(directory + "/" + type + "/" + feature):
                    print("     |" + feature)
                    for item in os.listdir(directory + "/" + type + "/" + feature):
                        if item.endswith(".json"):
                            print("         |"+item)
                            jsonfile = directory + "/" + type + "/" + feature + "/" + item
                            jsonfiles.append(jsonfile)

                        elif os.path.isdir(directory + "/" + type + "/" + feature + "/" + item) and item != "dist":
                            print("         |" + item)
                            for sub in os.listdir(directory + "/" + type + "/" + feature+ "/" + item):
                                if sub.endswith(".json"):
                                    print("             |" + sub)
                                    subJsonfile = directory + "/" + type + "/" + feature + "/" + item + "/" + sub
                                    jsonfiles.append(subJsonfile)
                            

    # Write full JSON file
    #print(jsonfiles)
    #return 1

    configFile = open("features.json", "w")
    i = 0
    j = 0
    test = ""
    typeBegin = ""
    beginInfo = """
    {
    \"location\": \"https://github.com/DairodR/Benchmark-Repo-Features.git\",
    \"branch\": \"redesign\",
    \"featuresPath\": \"Features\",
    \"features\": [
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine x86\",
            \"description\":\"Latest Alpine Linux x86\",
            \"os\":\"Alpine\",
            \"architecture\":\"x86\",
            \"baseImage\":\"alpine\",
            \"version\":\"latest\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine x86 v3.14\",
            \"description\":\"Alpine Linux x86 v3.14\",
            \"os\":\"Alpine\",
            \"architecture\":\"x86\",
            \"baseImage\":\"alpine\",
            \"version\":\"3.14\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine armv7\",
            \"description\":\"latest Alpine Linux for ARM32 v7\",
            \"os\":\"Alpine\",
            \"architecture\":\"armv7\",
            \"baseImage\":\"arm32v7/alpine\",
            \"version\":\"latest\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine armv6\",
            \"description\":\"latest Alpine Linux for ARM32 v6\",
            \"os\":\"Alpine\",
            \"architecture\":\"armv6\",
            \"baseImage\":\"arm32v6/alpine\",
            \"version\":\"latest\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine armv8\",
            \"description\":\"latest Alpine Linux for ARM64 v8\",
            \"architecture\":\"armv8\",
            \"os\":\"Alpine\",
            \"baseImage\":\"arm64v8/alpine\",
            \"version\":\"latest\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine i386\",
            \"architecture\":\"i386\",
            \"description\":\"latest Alpine Linux for i386\",
            \"os\":\"Alpine\",
            \"baseImage\":\"i386/alpine\",
            \"version\":\"latest\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine ppc64le\",
            \"architecture\":\"ppc64le\",
            \"description\":\"latest Alpine Linux for ppc64le\",
            \"os\":\"Alpine\",
            \"baseImage\":\"ppc64le/alpine\",
            \"version\":\"latest\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine riscv64\",
            \"architecture\":\"riscv64\",
            \"description\":\"Alpine Linux for riscv64 edge\",
            \"os\":\"Alpine\",
            \"baseImage\":\"riscv64/alpine\",
            \"version\":\"edge\"
        },
        {
            \"feature\": \"platform\",
            \"name\": \"Alpine s390x\",
            \"architecture\":\"s390x\",
            \"description\":\"latest Alpine Linux for s390x\",
            \"os\":\"Alpine\",
            \"baseImage\":\"s390x/alpine\",
            \"version\":\"latest\"
        },
    """

    typeBegin = "{beginInfo}\n".format(beginInfo=beginInfo)
    

    test += typeBegin
    for jsonfile in jsonfiles:
        file = open(jsonfile, "r")
        jsonF = file.read()
        if j == 0:
            test += jsonF
        else:
            test += ",\n" + jsonF
        j = j + 1
        file.close()


    typeEnd = "] \n}"
    test += typeEnd
    i = i + 1
    configFile.writelines(json.dumps(json.loads(test), indent=4))

    configFile.close()

if __name__ == '__main__':
    make()