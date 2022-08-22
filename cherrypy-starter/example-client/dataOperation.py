import sqlite3
import nacl
import nacl.encoding
import nacl.signing
import nacl.utils
from nacl.public import PrivateKey

#--------------------------------------------------------------------
#---------------private_detail---------------------------------------
#--------------------------------------------------------------------

def INSERT_PERSONAL_DATA(private,public,sign,upi,password):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("INSERT INTO private_detail (private_key,public_key,signature,upi,password) VALUES ('%s','%s','%s','%s','%s')"%(private,public,sign,upi,password))
    datadb.commit()
    c.close

def get_PRK():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT private_key FROM private_detail order by ID desc limit 1")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]

def get_PBK():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT public_key FROM private_detail order by ID desc limit 1")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]

def get_ID():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT ID FROM private_detail order by ID desc limit 1")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]


def get_UPI():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT upi FROM private_detail order by ID desc limit 1")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]


def get_PW():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT password FROM private_detail order by ID desc limit 1")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]


def get_Signature():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT signature FROM private_detail order by ID desc limit 1")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]

def get_ip():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT ip FROM ip_address")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]

def INSERT_ip(ip):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("DELETE FROM ip_address")
    c.execute("INSERT INTO ip_address (ip) VALUES ('%s')"%(ip))
    datadb.commit()
    c.close


#---------------------------------------------------------------
#-----------------------serverkey-------------------------------
#---------------------------------------------------------------

def INSERT_SERVER_DATA(public):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("DELETE FROM serverkey")
    c.execute("INSERT INTO serverkey (public_key) VALUES ('%s')"%(public))
    datadb.commit()
    c.close

#------------------------------------
#---------------userlist-------------
#------------------------------------

def INSERT_UserList(username,address,location,pubkey,updatedAt,status):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    try:
        c.execute("INSERT INTO userlist VALUES ('%s','%s','%s','%s','%s','%s')"%(username,address,location,pubkey,updatedAt,status))
        datadb.commit()
        c.close
    except:
        c.close
        datadb.close()
        raise 

def UPDATE_UserList(username,address,location,pubkey,updatedAt,status):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("DELETE FROM userlist WHERE username = '%s'"%(username))
    c.execute("INSERT INTO userlist VALUES ('%s','%s','%s','%s','%s','%s')"%(username,address,location,pubkey,updatedAt,status))
    datadb.commit()
    c.close

def set_offline():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("UPDATE userlist SET status = 'offline'")
    datadb.commit()
    c.close


def SELECT_pubkey(username):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT incomeing_pubkey FROM userlist WHERE username = '%s'"%(username))
    data_read = c.fetchone()
    datadb.close
    return(data_read[0])

def SELECT_address(username):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT connection_address FROM userlist WHERE username = '%s'"%(username))
    data_read = c.fetchone()
    datadb.close
    return(data_read[0])

def SELECT_status(username):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT status FROM userlist WHERE username = '%s'"%(username))
    data_read = c.fetchone()
    datadb.close
    return(data_read[0])

def SELECT_all_user():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT username FROM userlist")
    data_read = c.fetchall()
    datadb.close
    return(data_read)

#--------------------------------------------
#------------loginserver_recoding------------
#--------------------------------------------

def INSERT_serverRecording(recording):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("DELETE FROM serverRecording")
    c.execute("INSERT INTO serverRecording(loginserver_record) VALUES ('%s')"%(recording))
    datadb.commit()
    c.close

def get_serverRecording():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT loginserver_record FROM serverRecording")
    data_read = c.fetchone()
    datadb.close
    return data_read[0]


#---------------------------------------------
#--------------private_data-------------------
#---------------------------------------------
def get_Private_data(target):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT "+target+" FROM private_data")
    data_read = c.fetchall()
    datadb.close
    output = []
    for items in data_read:
        output.append(items[0])
    return(output)


def INSERT_private_data(private,b_username,b_pubkey,b_words,b_sign,f_sign,f_username):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("INSERT INTO private_data (prikeys,blocked_usernames,blocked_pubkey,blocked_words,blocked_signatures,favourite_signatures,friends_usernames) VALUES ('%s','%s','%s','%s','%s','%s','%s')"%(private,b_username,b_pubkey,b_words,b_sign,f_sign,f_username))
    datadb.commit()
    c.close

def DELETE_private_date():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("DELETE FROM private_data")
    datadb.commit()
    c.close
def get_block_word():
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT blocked_words FROM private_data")
    data_read = c.fetchall()
    datadb.close
    return data_read

#---------------------------------------------
#--------------------broadcast----------------
#---------------------------------------------
def INSERT_pubmessage(username,message,time):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("INSERT INTO broadcast (username,message,time) VALUES ('%s','%s','%s')"%(username,message,time))
    datadb.commit()
    c.close


def SELECT_pubmessage():
    datadb = sqlite3.connect('dataBase')
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT username,message,time FROM broadcast order by time desc")
    data_read = c.fetchall()
    datadb.close
    return data_read


#---------------------------------------------
#--------------------web page-----------------
#---------------------------------------------
def SELECT_uerlist():
    userlist = []
    list = SELECT_all_user()
    for items in list:
        username = items[0]
        datadb = sqlite3.connect('dataBase')
        c = datadb.cursor()
        c.execute("SELECT connection_address,username,status FROM userlist WHERE username = '%s'"%(username))
        data_read = c.fetchall()
        userlist = userlist+data_read
        datadb.close
    return(userlist)


    

#---------------------------------------------
#--------------------private---------------
#---------------------------------------------

def INSERT_Privatemessage(label,Who,Message,Time):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("INSERT INTO private_message (label,Who,Message,Time) VALUES ('%s','%s','%s','%s')"%(label,Who,Message,Time))
    datadb.commit()
    c.close

def SELECT_nameByip(ip):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT username FROM userlist WHERE connection_address = '%s'"%ip)
    data_read = c.fetchone()
    datadb.close
    return data_read[0]

def SELECT_all_message(username):
    datadb = sqlite3.connect('dataBase')
    c = datadb.cursor()
    c.execute("SELECT label,Message,Time FROM private_message WHERE who ='%s' order by Time asc"%username)
    data_read = c.fetchall()
    datadb.close
    return(data_read)


#------------------------------
def pri2signConvert(privateKey):
    return nacl.signing.SigningKey((bytes(privateKey,encoding="utf-8")),encoder=nacl.encoding.HexEncoder)