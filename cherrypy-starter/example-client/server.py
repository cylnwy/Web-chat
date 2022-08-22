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
from nacl.public import PrivateKey
import source

startHTML = "<html><head><title>CS302 example</title><link rel='stylesheet' href='/static/example.css' /></head><body>"

class MainApp(object):

   

	#CherryPy Configuration
    _cp_config = {'tools.encode.on': True, 
                  'tools.encode.encoding': 'utf-8',
                  'tools.sessions.on' : 'True',
                 }       

	# If they try somewhere we don't know, catch it here and send them to the right place.
    @cherrypy.expose
    def default(self, *args, **kwargs):
        """The default page, given when we don't recognise where the request is for."""
        Page = startHTML + "I don't know where you're trying to go, so have a 404 Error."
        cherrypy.response.status = 404
        return Page

    # PAGES (which return HTML that can be viewed in browser)
    # -------inital page------
    @cherrypy.expose
    def index(self):
        Page = startHTML + "<center>Welcome!</center><br/>"
        Page += "<center>Click here to <a href='login'>login</a>.</center>"
        return Page
        
    @cherrypy.expose
    def login(self, bad_attempt = 0):
        Page = startHTML
        if bad_attempt != 0:
            Page = source.bad_attempt_page()
            # when submitting form, send the data to /signin via post method
            # packing the form by enctype="multipart/form-data".
        else:    
                Page = source.loginpage()                
        return Page
    
        
    # LOGGING IN AND OUT
    @cherrypy.expose
    def signin(self, username=None, password=None, data_password=None,location=None,data=None):
        """Check their name and password and send them either to the main page, or back to the main login screen."""

        # Authenticate username & password
        if location == None:
            raise cherrypy.HTTPRedirect('/login?bad_attempt=1')
        try:
            Lognin.loginProcess(username, password,location,data,data_password)
            return source.get_mainpage()
        except:    
            raise cherrypy.HTTPRedirect('/login?bad_attempt=1')

    @cherrypy.expose
    def signout(self):
        """Logs the current user out, expires their session"""
        username = cherrypy.session.get('username')
        if username is None:
            pass
        else:
            cherrypy.lib.sessions.expire()
            Lognin.endThread()
            Lognin.reprot_offlice()
            #restart_program()
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def broadcast(self):
        Page = source.public_message()
        return Page

    @cherrypy.expose
    def privatemessage(self,address=None):
        Page = source.private_screen(address)
        return Page
    
    @cherrypy.expose
    def send_private(self,Message,ip):
        message_op.send_message_private(Message,ip)
        raise cherrypy.HTTPRedirect('/privatemessage?address=%s'%ip)


    @cherrypy.expose
    def messIn(self,Message):
        message_op.send_message(Message)
        raise cherrypy.HTTPRedirect('/broadcast')



###
### Functions only after here
###
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

