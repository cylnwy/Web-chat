# 2019-Python-WebCat

(The outcome of the Engineering Part III course)


This is a python-based web chat client that works with a pre-setted cherrypy server.

The user can log in to their account, then  have a broadcast, private chat, and find other users through the web-based UI. 

The development involved the use of python and cherrypy for the back-end and HTML and CSS for the front-end.

********
To run the WebChat, the device should set up with python environments and able to load cherrypy, pynacl, and Jinia2 properly.

'python3 main.py' could do the compiling via terminal under this path.

In the Login page, username, password and the Connection Location(Uni_Lab, Uni_Wireless or Rest_word) have to be filled and selected for login into the server.

Enable_private_data checkbox is used to enable get and post methods of private data. When the box is clicked, the 'data' has to be filled with the correct password. (the password already be set as 'cylnwy', the password is unchangeable) As the functions related to private data is not finished. The enable of private data only allowed the user to download and upload the information.

For both private message and broadcast, word 'test' 'one' to 'seven' are blocked.

Users have to click the 'sign out' link on the right top to log out the WebChat properly.(Refresh of the page is recommended if the user wishes to log in again.)

To broadcast a message, the link with the same name should be clicked.


***** Login and log out may take some time ********
