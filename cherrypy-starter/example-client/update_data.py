import urllib.request
import json
import nacl
import nacl.encoding
import nacl.signing
import base64
import nacl.utils
import cherrypy
import message_op
import dataOperation
import time
import nacl.secret
import nacl.pwhash


#used in getAPIkey login.py
def getServerPubk():

    url = 'http://cs302.kiwi.land/api/loginserver_pubkey'
    headers ={
        'Content-Type' : 'application/json; charset=utf-8',
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
        JSON_object = json.loads(data.decode(encoding))
        dataOperation.INSERT_SERVER_DATA(JSON_object['pubkey'])
        return JSON_object['pubkey']
    except urllib.error.HTTPError as error:
        return error.read()

#used in reprot and thred
def getUserList():
    url = 'http://cs302.kiwi.land/api/list_users'
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }
    try:
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
    except urllib.error.HTTPError as error:
        print(error.read(),"----------------ERROR MESSAGE------------------")
    JSON_object = json.loads(data.decode(encoding))
    data_read = JSON_object["users"]
    dataOperation.set_offline()
    for row in data_read:
        try:
            dataOperation.INSERT_UserList(row["username"],row["connection_address"],row["connection_location"],row["incoming_pubkey"],row["connection_updated_at"],row["status"])
        except:
            dataOperation.UPDATE_UserList(row["username"],row["connection_address"],row["connection_location"],row["incoming_pubkey"],row["connection_updated_at"],row["status"])


#not used yet       
def getloginserverRecord():
    url = 'http://cs302.kiwi.land/api/get_loginserver_record'
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
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
        dataOperation.INSERT_serverRecording(JSON_object["loginserver_record"])
    except urllib.error.HTTPError as error:
        print (error.read())  

def add_privatedata():
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    signature = dataOperation.get_Signature()
    log_Re = dataOperation.get_serverRecording()
    time1 = time.time()
    time_Send = repr(time1)

    pk = dataOperation.get_PRK()
    bk_puk = dataOperation.get_Private_data("blocked_pubkey")
    bk_username = dataOperation.get_Private_data("blocked_usernames")
    bk_wd = dataOperation.get_Private_data("blocked_words")
    bk_ms = dataOperation.get_Private_data("blocked_signatures")
    favour_ms = dataOperation.get_Private_data("favourite_signatures")
    friends = dataOperation.get_Private_data("friends_usernames")

    private = {
        'prikeys':pk,
        'blocked_pubkeys':bk_puk,
        'blocked_usernames':bk_username,
        'blocked_words':bk_wd,
        'blocked_message_signatures':bk_ms,
        'favourite_message_signatures':favour_ms,
        'friends_usernames':friends
    }


    private_enc = message_op.encrypt_data(private)

    prikey = dataOperation.get_PRK()
    signingKey = dataOperation.pri2signConvert(prikey)
    signature_send = signingKey.sign(bytes(private_enc+log_Re+time_Send,encoding = "utf-8"),encoder=nacl.encoding.HexEncoder)
    signature_send_str = signature_send.signature.decode("utf-8")

    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    url = 'http://cs302.kiwi.land/api/add_privatedata'
    headers = {
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'X-signature': signature,
        'Content-Type': 'application/json; charset=utf-8',

        }
    payload = {
        'privatedata':private_enc,
        'loginserver_record':log_Re,
        'client_saved_at':time_Send,
        'signature':signature_send_str
        }

    data_str = json.dumps(payload)
    data_byt = data_str.encode(encoding='utf-8')
    try:
        req = urllib.request.Request(url, data=data_byt, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read()  # read the received bytes
        # load encoding if possible (default to utf-8)
        encoding = response.info().get_content_charset('utf-8')
        response.close()
    except urllib.error.HTTPError as error:
        print(error.read(), "----------------ERROR MESSAGE------------------")

    JSON_object = json.loads(data.decode(encoding))
    print(JSON_object, "--------------feedback-----------")

def get_privatedata(key):
    url = 'http://cs302.kiwi.land/api/get_privatedata'
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }


    try:
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
    except urllib.error.HTTPError as error:
        print(error.read(),"----------------ERROR MESSAGE------------------")

    key_16 = ""
    for i in range(0,16):
        key_16 = key_16 + key
        if(len(key_16) >= 16):
            key_16 = key_16[0:16]
            break
    key_16_byte = bytes(key_16,encoding= "utf-8")
    key_byte = bytes(key,encoding= "utf-8")
    symKey = nacl.pwhash.argon2i.kdf(32,key_byte,key_16_byte,8,536870912)    
    box = nacl.secret.SecretBox(symKey)
    JSON_object = json.loads(data.decode(encoding))
    content = JSON_object["privatedata"]
    content_byte = bytes(content,encoding= "utf-8")
    content_row = base64.b64decode(content_byte)
    plaintext = (box.decrypt(content_row)).decode('utf-8')
    text_dict = eval(plaintext)
    a = text_dict["blocked_words"]
    for n in range(0,len(a)):
        dataOperation.INSERT_private_data(text_dict['prikeys'][n],text_dict['blocked_usernames'][n],text_dict['blocked_pubkeys'][n],text_dict['blocked_words'][n],text_dict['blocked_message_signatures'][n],text_dict['favourite_message_signatures'][n],text_dict['friends_usernames'][n])

def refresh_data():
    get_privatedata("cylnwy")
    add_privatedata()
    dataOperation.DELETE_private_date()