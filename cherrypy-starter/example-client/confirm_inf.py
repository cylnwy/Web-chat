import urllib.request
import json
import nacl
import nacl.encoding
import nacl.signing
import base64
import nacl.utils
import cherrypy
import dataOperation

def checkPubkey():
    url = 'http://cs302.kiwi.land/api//check_pubkey'
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    pubkey = dataOperation.get_PBK()
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    headers ={
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'Content-Type' : 'application/json; charset=utf-8',
    }
    payload={
        "pubkey":pubkey
    }

    data_str = json.dumps(payload)
    data_byt = data_str.encode(encoding='utf-8')
    try:
        req = urllib.request.Request(url, data=data_byt, headers=headers)
        response = urllib.request.urlopen(req)
        data = response.read() # read the received bytes
        encoding = response.info().get_content_charset('utf-8') #load encoding if possible (default to utf-8)
        response.close()
    except urllib.error.HTTPError as error:
        print(error.read(),"----------------ERROR MESSAGE------------------")


    JSON_object = json.loads(data.decode(encoding))
    print(JSON_object,"____________feedback___________")