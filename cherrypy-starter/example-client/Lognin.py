import urllib.request
import json
import nacl
import nacl.encoding
import nacl.signing
import base64
import nacl.utils
import cherrypy
import dataOperation
from threading import Timer
import time
import threading
import myThreading
import update_data
from nacl.public import PrivateKey
import _thread
flage = True
location_g = 1
data_flag = False

def ping_server(username,password):
    ### Get API key that used to inplace of HTTP BASIC authentication.
    ### The usage of API key is optional as all endopint will accept HTTP BASIC
    url = 'http://cs302.kiwi.land/api/ping'
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
        JSON_object = json.loads(data.decode(encoding))
        #
        update_data.getServerPubk()
        return JSON_object
    except urllib.error.HTTPError as error:
        return error.read()

def getAPIKey(username,password):
    ### Get API key that used to inplace of HTTP BASIC authentication.
    ### The usage of API key is optional as all endopint will accept HTTP BASIC
    url = 'http://cs302.kiwi.land/api/load_new_apikey'
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
        JSON_object = json.loads(data.decode(encoding))
    except urllib.error.HTTPError as error:
        return error.read()
    return(JSON_object)

def PostPubKey(signature,pubkey,username,password):
    url = 'http://cs302.kiwi.land/api/add_pubkey'
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'X-signature':signature,
        'Content-Type' : 'application/json; charset=utf-8',
        
    }
    payload ={
        'pubkey':pubkey,
        'username':username,
        'signature':signature
    }

    data_str = json.dumps(payload)
    data_byt = data_str.encode(encoding = 'utf-8')

    try:
        req = urllib.request.Request(url, data=data_byt, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
        #reprot
        reportServer(username, password,pubkey,location_g)
    except urllib.error.HTTPError as error:
        print(error.read(),"----------------ERROR MESSAGE------------------")

    JSON_object = json.loads(data.decode(encoding))
    dataOperation.INSERT_serverRecording(JSON_object["loginserver_record"])
    print(JSON_object,"--------------public key push feedback-----------")

def loginProcess(username, password,location,data,data_password):
    global location_g
    global data_flag
    location_g = location
    if data != None:
        data_flag = True
        update_data.get_privatedata(data_password)
    apikey = getAPIKey(str(username),str(password)) 
    ping = ping_server(str(username),str(password)) 
    log_res = apikey['response']
    API_Key = apikey['api_key']
    ping_re = ping['response']
    cherrypy.session['username'] = username
    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    private_key_hex = signing_key.encode(encoder=nacl.encoding.HexEncoder).decode('utf-8')
    public_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder).decode('utf-8')

    signature = signing_key.sign(bytes(public_key_hex+username,encoding="utf-8"),encoder=nacl.encoding.HexEncoder)
    signature_str = signature.signature.decode("utf-8")
    dataOperation.INSERT_PERSONAL_DATA(private_key_hex,public_key_hex,signature_str,username,password)

    PostPubKey(signature_str,public_key_hex,username,password)
    try:
        t.start()
    except:
        a = ()
        _thread.start_new_thread(delayrun,a)


def reportServer(username, password,pubkey,location):
    flage = 1
    url = 'http://cs302.kiwi.land/api/report '
    ip = dataOperation.get_ip()
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }

    payload={
        "connection_address": "%s"%ip, 
        "connection_location": '%s'%location,  
        "incoming_pubkey": pubkey
    }

    data_str = json.dumps(payload)
    data_byt = data_str.encode(encoding = 'utf-8')

    try:
        req = urllib.request.Request(url, data=data_byt, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
    except urllib.error.HTTPError as error:
        print(error.read(),"----------------ERROR MESSAGE------------------")

    JSON_object = json.loads(data.decode(encoding))
    update_data.getUserList()
    print(JSON_object,"--------------Reoport-----------")
    print("---------main loop still runing--------")


def reprot_offlice():
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    pubkey = dataOperation.get_PBK()
    url = 'http://cs302.kiwi.land/api/report '
    ip = dataOperation.get_ip()
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }

    payload={
        "connection_address": "%s"%ip, 
        "connection_location": 2,  
        "incoming_pubkey": pubkey,
        "status":'offline'
    }

    data_str = json.dumps(payload)
    data_byt = data_str.encode(encoding = 'utf-8')

    try:
        req = urllib.request.Request(url, data=data_byt, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
    except urllib.error.HTTPError as error:
        print(error.read(),"----------------ERROR MESSAGE------------------")

    JSON_object = json.loads(data.decode(encoding))
    update_data.getUserList()
    if data_flag:
        update_data.add_privatedata()
#--------------------------------------------------------------
def delayrun(name = 1):
    global flage
    while (flage):
        counter = 0
        time.sleep(1)
        counter = counter +1
        if(counter == 200):
            upi = dataOperation.get_UPI()
            pw = dataOperation.get_PW()
            pubkey = dataOperation.get_PBK()
            reportServer(upi,pw,pubkey,location_g)
            update_data.getUserList()
        else:
           pass

t=threading.Thread(target = delayrun)



    
def endThread():
    global flage 
    flage = False
    #myThreading.StoppableTHread.stop(t)