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
from nacl.public import PrivateKey,SealedBox
import nacl.secret
import nacl.pwhash


def send_message(message):
    content = dataOperation.SELECT_all_user()
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    signature = dataOperation.get_Signature()
    login_Re = dataOperation.get_serverRecording()
    pk = dataOperation.get_PRK()
    signingKey = dataOperation.pri2signConvert(pk)
    time1 = time.time()
    time_Send = repr(time1)
    signature_send = signingKey.sign(bytes(login_Re+message+time_Send,encoding = "utf-8"),encoder=nacl.encoding.HexEncoder)


    signature_send_str = signature_send.signature.decode("utf-8")

    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    for user in content:
        username_tar = user[0]
        address_tar = dataOperation.SELECT_address(username_tar)
        url = 'http://%s/api/rx_broadcast'%address_tar
        headers = {
            'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
            'X-signature': signature,
            'Content-Type': 'application/json; charset=utf-8',

            }
        payload = {
            'loginserver_record':login_Re,
            'message': message,
            'sender_created_at':time_Send,
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
                JSON_object = json.loads(data.decode(encoding))
                print(username_tar,JSON_object)

        except:
            pass


def send_message_private(message,ip):

    username_tar = dataOperation.SELECT_nameByip(ip)
    username = dataOperation.get_UPI()
    password = dataOperation.get_PW()
    m_enc = encrypt_sealedbox(message,username_tar)
    log_Re = dataOperation.get_serverRecording()
    time1 = time.time()
    time_Send = repr(time1)
    pubkey_tar = dataOperation.SELECT_pubkey(username_tar)
    pubkey = dataOperation.get_PRK()
    signingKey = dataOperation.pri2signConvert(pubkey)
    signature_send = signingKey.sign(bytes(log_Re+pubkey_tar+username_tar+m_enc+time_Send,encoding = "utf-8"),encoder=nacl.encoding.HexEncoder)
    signature_send_str = signature_send.signature.decode("utf-8")
    signature = dataOperation.get_Signature()
    credentials = ('%s:%s' % (username, password))
    b64_credentials = base64.b64encode(credentials.encode('ascii'))
    url = 'http://%s/api/rx_privatemessage'%ip
    headers = {
        'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
        'X-signature': signature,
        'Content-Type': 'application/json; charset=utf-8',

        }
    payload = {
        'loginserver_record':log_Re,
        'target_pubkey':pubkey_tar,
        'target_username':username_tar,
        'encrypted_message':m_enc,
        'sender_created_at':time_Send,
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
        dataOperation.INSERT_Privatemessage('S',username_tar,message,time_Send)
        response.close()
        JSON_object = json.loads(data.decode(encoding))
        print(username_tar,JSON_object)
    except:
        pass
def encrypt_sealedbox(mess,username):
        message = bytes(mess,encoding="utf-8")
        
        pubkey_target=dataOperation.SELECT_pubkey("%s"%username)
        verifykey = nacl.signing.VerifyKey(pubkey_target,encoder = nacl.encoding.HexEncoder)
        publickey = verifykey.to_curve25519_public_key()
        sealed_box = nacl.public.SealedBox(publickey)
        encrypted = sealed_box.encrypt(message,encoder=nacl.encoding.HexEncoder)
        message = encrypted.decode('utf-8')
        return(message)

def encrypt_data(message):
    priate_str = str(message)
    priate_byt = bytes(priate_str,encoding = 'utf-8')
    key = "cylnwy"
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
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)


    encrypted = box.encrypt(priate_byt,nonce)

    encrypted_b64 = base64.b64encode(encrypted)
    encrypted_str = encrypted_b64.decode('utf-8')
    return encrypted_str

