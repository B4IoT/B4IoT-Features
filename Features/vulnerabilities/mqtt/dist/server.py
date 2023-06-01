from asyncio import open_connection
import paho.mqtt.client as mqtt
import subprocess
import time
import os 

path = os.path.realpath(__file__)
path = os.path.dirname(path)
os.chdir(path)
vuln_path = path + "../vulns/"

extensionsMap = {".py": ["python3"], ".jar": ["java", "-jar"], ".bin": ["./"]}

executables = []
executables_fp = []
for subdir,dirs,files in os.walk(vuln_path):
        sub_path = str(subdir).split('/')[len(str(subdir).split('/'))-1]
        for file in files:
            if file.split('.')[1] != 'db':
                full_path = os.path.join(subdir, file)
                executables.append(file)
                executables_fp.append(full_path)


def on_connect(client, userdata, flags, rc):
    for exe in executables_fp:
        exe_split = exe.split('/')
        name = exe_split[len(exe_split)-2] + "/" + exe_split[len(exe_split)-1]

        client.publish(name, "To know the format send \"-M GET\" to the topic \n To post data send \"-M POST\" and the arguments required")


def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8"))
    print("received message: " + message.payload.decode("utf-8") + " on topic " + message.topic)

    splitted_msg = payload.split(' ')

    
    if len(splitted_msg) > 1:
        if splitted_msg[0] == "-M" and splitted_msg[1] == "POST":
            print("Post request")
            cmd = ""

            for exe in executables_fp:
                if message.topic in exe:
                    ext = os.path.splitext(exe)[1]
                    cmd = extensionsMap[ext].copy()

                    cmd.append(exe)
                    cmd.append('-M')
                    cmd.append('POST')
                    
            payload_tmp = payload.split('POST ')[1][1:]

            splitted_payload = payload_tmp.split(' -')
            for param in splitted_payload:
                flagged_param = '-' + param

                whitespace = False
                i = 0
                while whitespace == False:
                    if flagged_param[i] == ' ':
                        whitespace = True
                        flag = flagged_param[:i]
                        value = flagged_param[i:]
                    i = i + 1
                    
                cmd.append(flag)
                cmd.append(value)

            print(str(cmd))
            result = subprocess.check_output(cmd)
            client.publish(message.topic, result)

        elif splitted_msg[0] == "-M" and splitted_msg[1] == "GET":
            print("Get request")
            # Send get request to file linked to topic

            for exe in executables_fp:
                if message.topic in exe:
                    ext = os.path.splitext(exe)[1]
                    cmd = extensionsMap[ext].copy()

                    cmd.append(exe)
                    for arg in splitted_msg:
                        cmd.append(arg)
                    print(str(cmd))
                    result = subprocess.check_output(cmd)
                    
                    client.publish(message.topic, result)

        else:
            print("Not responding to this format.")


mqttBroker ="127.0.0.1"

for exe in executables_fp:
    exe_split = exe.split('/')
    name = exe_split[len(exe_split)-2] + "/" + exe_split[len(exe_split)-1]
    client = mqtt.Client(exe)
    client.connect(mqttBroker) 

    client.loop_start()

    client.subscribe(name)
    client.on_connect=on_connect
    client.on_message=on_message


while True:
    time.sleep(60)
    for exe in executables_fp:
        exe_split = exe.split('/')
        name = exe_split[len(exe_split)-2] + "/" + exe_split[len(exe_split)-1]

        client.publish(name, "To know the format send \"-M GET\" to the topic \n To post data send \"-M POST\" and the arguments required")