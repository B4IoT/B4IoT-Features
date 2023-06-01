#!/usr/bin/python3
import datetime
import logging
import threading 
import asyncio
import time
import aiocoap.resource as resource
import aiocoap
import os
import subprocess

path = os.path.realpath(__file__)
path = os.path.dirname(path)
os.chdir(path)

extensionsMap = {".py": ["python3"], ".jar": ["java", "-jar"], ".bin": ["./"]}


class LevelOne(resource.Resource):
    # Basic command injection with feedback, you can do anything you like
    def __init__(self, path):
        super().__init__()
        self.path = path
    #    self.content = (b"Post the correct data to turn on the light!: \n")

    async def render_get(self, request):
        # Send a request with a get query to the file that it communicates with
        ext = os.path.splitext(self.path)[1]
        cmd = extensionsMap[ext].copy()
        cmd.append(self.path)

        #if request is not None:
        #    print(str(request))
            #cmd.append(request)

        cmd.append("-M")
        cmd.append("GET")
        #cmd.append(" > tmp.txt")

        print("formed command: "+ str(cmd))
        try:
            output = subprocess.check_output(cmd)
            print(output)
            #fp = open('tmp.txt', "r")
            #output = fp.read()
            #fp.close()
            #os.remove('tmp.txt')
            #print(output)
            return aiocoap.Message(payload=output)
        except subprocess.CalledProcessError:
            return aiocoap.Message(payload="ERROR".encode('utf-8'))
        
        
    async def render_put(self, request):
        # Send a request with a get query to the file that it communicates with
        ext = os.path.splitext(self.path)[1]
        cmd = extensionsMap[ext].copy()
        cmd.append(self.path)
        
        print(str(request.opt.uri_query))
        print(str(request.opt))
        cmd.append("-M")
        cmd.append("POST")

        print('PUT payload: %s' % request.payload)
        payload_string = request.payload.decode("utf-8")
        print('payload as string: ', payload_string)
        # TODO: Split on second -
        #cmd.append("-P")
        
        payload_tmp = payload_string[1:]
        splitted_payload = payload_tmp.split(' -')
        print(splitted_payload)
        for param in splitted_payload:
            flagged_param = '-' + param
            print(flagged_param)

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


        print("formed command: "+ str(cmd))
        try:
            output = subprocess.check_output(cmd)
            print(output)
            return aiocoap.Message(payload=output)
        except subprocess.CalledProcessError:
            return aiocoap.Message(payload="ERROR".encode('utf-8'))
        

        #result = [None]
        #x = threading.Thread(target=LevelOne.switch_light, args=(self,request,result))
        #x.start()
        # Not using join since this is blocking
        #time.sleep(0.5)

        #return result[0]

class TimeResource(resource.ObservableResource):
    """Example resource that can be observed. The `notify` method keeps
    scheduling itself, and calles `update_state` to trigger sending
    notifications."""

    def __init__(self):
        super().__init__()

        self.handle = None

    def notify(self):
        self.updated_state()
        self.reschedule()

    def reschedule(self):
        self.handle = asyncio.get_event_loop().call_later(5, self.notify)

    def update_observation_count(self, count):
        if count and self.handle is None:
            print("Starting the clock")
            self.reschedule()
        if count == 0 and self.handle:
            print("Stopping the clock")
            self.handle.cancel()
            self.handle = None

    async def render_get(self, request):
        payload = datetime.datetime.now(). \
            strftime("%Y-%m-%d %H:%M").encode('ascii')
        return aiocoap.Message(payload=payload)


class WhoAmI(resource.Resource):
    async def render_get(self, request):
        text = ["Used protocol: %s." % request.remote.scheme]

        text.append("Request came from %s." % request.remote.hostinfo)
        text.append("The server address used %s." % request.remote.hostinfo_local)

        claims = list(request.remote.authenticated_claims)
        if claims:
            text.append("Authenticated claims of the client: %s." % ", ".join(repr(c) for c in claims))
        else:
            text.append("No claims authenticated.")

        return aiocoap.Message(content_format=0,
                               payload="\n".join(text).encode('utf8'))


# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)


def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['.well-known', 'core'],
                      resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['whoami'], WhoAmI())

    vuln_path = path + "/../vulns/"
    print(vuln_path)
    for subdir,dirs,files in os.walk(vuln_path):
        sub_path = str(subdir).split('/')[len(str(subdir).split('/'))-1]
        for file in files:
            if file.split('.')[1] != 'db':
                full_path = os.path.join(subdir, file)
                root.add_resource([sub_path ,file], LevelOne(full_path))

    asyncio.Task(aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()

