import cherrypy
import urllib.request
import json
import nacl
import nacl.encoding
import nacl.signing
import base64
import nacl.utils
import Lognin
import sys
import os
import threading
import time
import message_op
from nacl.public import PrivateKey,SealedBox
import dataOperation
import binascii

startHTML = "<html><head><title>CS302 example</title><link rel='stylesheet' href='/static/example.css' /></head><body>"

class Receive(object):

    @cherrypy.expose
    @cherrypy.tools.json_in()

    def rx_broadcast(self):
        blocked = False
        body = cherrypy.request.json
        log_Re = body["loginserver_record"]
        record_time = body["sender_created_at"]
        message = body["message"]
        send_time = body["sender_created_at"]
        sinature = body["signature"]
        sinature_by = bytes(sinature,encoding="utf-8")
        log_list = [str(x) for x in log_Re.split(',')]
        username = log_list[0]
        pubkey = log_list[1]
        verifykey = nacl.signing.VerifyKey(pubkey,encoder=nacl.encoding.HexEncoder)
        mes_byte = bytes(log_Re+message+send_time,encoding="utf-8")
        mes_hex = binascii.b2a_hex(mes_byte)
        blocked_words = dataOperation.get_block_word()
        for word in blocked_words:
            if(word[0] in message):
                blocked = True
                word = word[0]
                break
        try:
            verifykey.verify(mes_hex,sinature_by,nacl.encoding.HexEncoder)
            if(blocked):
                print("-----------message_blocked-------------")
                payload={
             'response':'error',
             'message':'blocked'
                }
                data_str = json.dumps(payload)
                data_byt = data_str.encode(encoding='utf-8')
                return data_byt
            else:
                print("hey! you receive a message")
                dataOperation.INSERT_pubmessage(username,message,send_time)
                payload={
                'response':'ok'
                }
                data_str = json.dumps(payload)
                data_byt = data_str.encode(encoding='utf-8')
                return data_byt
        except:
            payload={
                'response':'error'
            }
            data_str = json.dumps(payload)
            data_byt = data_str.encode(encoding='utf-8')
            return data_byt
        
    @cherrypy.expose
    @cherrypy.tools.json_in()

    def rx_privatemessage(self):
        blocked = False
        word = ""
        body = cherrypy.request.json

        myname = dataOperation.get_UPI()
        mypubkey = dataOperation.get_PBK()

        log_Re = body["loginserver_record"]
        target_pubkey = body["target_pubkey"]
        target_username = body["target_username"]
        encrypted_message = body["encrypted_message"]
        send_time = body["sender_created_at"]
        sinature = body["signature"]


        if(target_username != myname or target_pubkey != mypubkey):
            pass
        else:
            sinature_by = bytes(sinature,encoding="utf-8")
            log_list = [str(x) for x in log_Re.split(',')]
            pubkey = log_list[1]
            username = log_list[0]
            verifykey = nacl.signing.VerifyKey(pubkey,encoder=nacl.encoding.HexEncoder)
            mes_byte = bytes(log_Re+target_pubkey+target_username+encrypted_message+send_time,encoding="utf-8")
            mes_hex = binascii.b2a_hex(mes_byte)
            try:
                verifykey.verify(mes_hex,sinature_by,nacl.encoding.HexEncoder)
                enc_byte = bytes(encrypted_message,encoding='utf-8')
                myprk = dataOperation.get_PRK()
                signingkey = nacl.signing.SigningKey(myprk,encoder = nacl.encoding.HexEncoder)
                PrivateKey = signingkey.to_curve25519_private_key()
                unseale_box = nacl.public.SealedBox(PrivateKey)
                try:
                    plaintext = unseale_box.decrypt(enc_byte,encoder = nacl.encoding.HexEncoder)
                    message_plain = plaintext.decode('utf-8')
                    blocked_words = dataOperation.get_block_word()
                    for word in blocked_words:
                        if(word[0] in message_plain):
                            blocked = True
                            word = word[0]
                            break

                    if(blocked):
                        payload={
                            'response':'error',
                            'message':'contain blocked words:%s'%word
                        }
                        data_str = json.dumps(payload)
                        data_byt = data_str.encode(encoding='utf-8')
                        return data_byt
                        
                    else:
                        payload={
                            'response':'ok',
                        }
                        data_str = json.dumps(payload)
                        data_byt = data_str.encode(encoding='utf-8')
                        dataOperation.INSERT_Privatemessage('R',username,message_plain,send_time)
                        print('recieve_message',username)
                        return data_byt
                except:
                    payload={
                        'response':'error',
                        'message':'can not decrypt the message'
                    }
                    data_str = json.dumps(payload)
                    data_byt = data_str.encode(encoding='utf-8')
                    return data_byt

            except:
           
        
                payload={
                    'response':'error',
                    'message':'wrong people'
                }
                data_str = json.dumps(payload)
                data_byt = data_str.encode(encoding='utf-8')
                return data_byt
