import dataOperation

def loginpage():
    Page = """ 
    <!DOCTYPE html>
    <html>
    <title>WebChat</title>

    <head>
        <title>Login</title>
        <style type='text/css'>
            .body {
                background-image:url('./static/background.jpg');
                background-repeat: no-repeat;
                background-size: cover;
                background-attachment: fixed;

            }
            .table {
                top: 50%;
                left: 50%;
                background-color:rgba(0,0,0,0.6);
                position: absolute;
                transform: translate(-50%, -50%);
                color: cornsilk;
            }
            .cb{

            }
            .rd{

            }
        </style>
    </head>

    <body class="body">
        
            <form action='/signin' method=post enctype="multipart/form-data">
                <table class="table">
                    <tr>
                        <td colspan=2><font color = 'white'>Login</font></td>
                    </tr>
                    <tr>
                        <td><font color = 'white'>username:</font></td>
                    </tr>
                    <tr>
                        <td><input type='text' name='username' size=16 /></td>
                    </tr>
                    <tr>
                        <td><font color = 'white'>password:</font></td>
                    </tr>
                        <td><input type='password' name='password' size=16 /></td>
                    </tr>
                    <tr>
                        <td><font color = 'white'>data:</font></td>
                    </tr>
                    <tr>
                        <td><input type='password' name=data_password size=16 /></td>
                    </tr>
                    
                    <tr>
                        <td>
                        <div><label><input type="radio" class = 'rd' name="location" value="0">Uni_Lab</label>
                            <label><input type="radio" class = 'rd' name="location" value="1">Uni_Wireless</label>
                            <label><input type="radio" class = 'rd' name="location" value="2">Rest_word</label>
                        </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <label><input type="checkbox" class = "cb" name="data" value="0">enable private_data</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                            <td><input type=submit value=submit></td>
                    </tr>
                </table>
            </form>
    </body>

    </html>
    """
    return Page

def bad_attempt_page():
    Page = """ 
           <!DOCTYPE html>
    <html>
    <title>WebChat</title>

    <head>
        <title>Login</title>
        <style type='text/css'>
            .body {
                background-image:url('./static/background.jpg');
                background-repeat: no-repeat;
                background-size: cover;
                background-attachment: fixed;

            }
            .table {
                top: 50%;
                left: 50%;
                background-color:rgba(0,0,0,0.6);
                position: absolute;
                transform: translate(-50%, -50%);
                color: cornsilk;
            }
            .cb{

            }
            .rd{

            }
        </style>
    </head>

    <body class="body">
        
            <form action='/signin' method=post enctype="multipart/form-data">
                <table class="table">
                    <tr>
                        <td colspan=2><font color = 'white'>Login</font>
                        <font color='red'>Invalid username/password!</font></td>
                        
                    </tr>
                    <tr>
                        <td><font color = 'white'>username:</font></td>
                    </tr>
                    <tr>
                        <td><input type='text' name='username' size=16 /></td>
                    </tr>
                    <tr>
                        <td><font color = 'white'>password:</font></td>
                    </tr>
                        <td><input type='password' name='password' size=16 /></td>
                    </tr>
                    <tr>
                        <td><font color = 'white'>data:</font></td>
                    </tr>
                    <tr>
                        <td><input type='password' name=data_password size=16 /></td>
                    </tr>
                    
                    <tr>
                        <td>
                        <div><label><input type="radio" class = 'rd' name="location" value="0">Uni_Lab</label>
                            <label><input type="radio" class = 'rd' name="location" value="1">Uni_Wireless</label>
                            <label><input type="radio" class = 'rd' name="location" value="2">Rest_word</label>
                        </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div>
                                <label><input type="checkbox" class = 'cb' name="data" value="0">enable private_data</label>
                            </div>
                        </td>
                    </tr>
                    <tr>
                            <td><input type=submit value=submit></td>
                    </tr>
                </table>
            </form>
    </body>

    </html>
    """
    return Page
#------------------------------------------------------
#------------------------------------------------------
#------------------------------------------------------

def get_mainpage_css1():
    Page = """ 
        <!DOCTYPE html>
<html class='html'>
<title>WebChat</title>

<head>
    <title>Login</title>
    <style type='text/css'>
        .html {
            height: 90%;
            margin: 0;
        }

        .body {
            background-image: url('./static/background.jpg');
            background-repeat: no-repeat;
            background-size: cover;
            background-attachment: fixed;
            height: 100%;
            margin: 0;
        }
        .word{
            color: rgb(255, 255, 255);

        }

        .head {
            background-color: rgba(0, 0, 0, 50%);
            margin-bottom: 0;
            margin-top: 0;
            height: 7%;
        }

        .right_lable {
            position: absolute;
            top: 0px;
            right: 10px;
            color: cornsilk;
            text-align: right;
        }

        .menu {
            float: left;
            border-right: 2px solid rgb(92, 92, 92);
            width: 100px;
            height: 97%;
            overflow: auto;
            color: cornsilk;
            display: table-cell;
            vertical-align: middle;
            text-align: left;
        }

        .footer {
            background-color: rgb(0, 0, 0);
            clear: both;
            text-align: center;
            position: absolute;
            color: cornsilk;
            left: 0;
            right: 0;
            bottom: 0;
        }

        .content {
            float: left;
            position: absolute;
            right: 0;
            left: 102px;
            height: 90%;
            color: cornsilk;
            background-color: rgba(0, 0, 0, 40%);

        }

        a:link {
            color: cornsilk;
        }

        a:visited {
            color: cornsilk;
        }

    </style>
</head>
<body class='body'>
    <div class='head'>
        <h1 class="word">
            <center>
                WebChat<font size= 1>  private</font>
            </center>
        </h1>
    </div>
    <div class='right_lable'>
        <a href='/signout'>Sign out</a><br />
        <a href='/broadcast'>broadcast</a><br />
    </div>
            """
    return Page

def get_mainpage():
    Page1 = """ 
            <table class='menu'>

        """

    page_end = """

    </table>
    <div class="content">
    
    </div>

    <div class='footer'>
        <center>hwan685</center>

    </div>

</body>

</html>
     """
    userlist = gen_userlist()

    Page = Page1 + userlist +page_end
    Page = Page + get_mainpage_css1()
    return Page



def gen_userlist():
    userlist = dataOperation.SELECT_uerlist()
    Page = """ """
    online = """ """
    offline = """ """
    for row in userlist:
        if row[2] !='online':
            current = """ 
                <tr>
                    <td>
                        <a href='/privatemessage?address=%s'>%s</a>
                        <font color=red><font size= 1>%s</font></font>
                    </td>
                </tr>
                """%(row[0],row[1],row[2])
            online = online +current
        else:
            current = """ 
                <tr>
                    <td>
                        <a href='/privatemessage?address=%s'>%s</a>
                        <font color=white><font size= 1>%s</font></font>
                    </td>
                </tr>
                """%(row[0],row[1],row[2])
            offline = offline +current
    Page = offline+online
    return(Page)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

def public_message():
    Page_head = """ 
                    <!DOCTYPE html>
    <html class='html'>
    <title>WebChat</title>

    <head>
        <title>Login</title>
        <style type='text/css'>
            .html {
                height: 90%;
                margin: 0;
            }

            .body {
                background-image: url('./static/background.jpg');
                background-repeat: no-repeat;
                background-size: cover;
                background-attachment: fixed;
                height: 100%;
                margin: 0;
            }

            .word {
                color: rgb(255, 255, 255);

            }

            .head {
                background-color: rgba(0, 0, 0, 50%);
                margin-bottom: 0;
                margin-top: 0;
                height: 7%;
            }

            .right_lable {
                position: absolute;
                top: 0px;
                right: 10px;
                color: cornsilk;
                text-align: right;
            }

            .menu {
                float: left;
                border-right: 2px solid rgb(92, 92, 92);
                width: 100px;
                height: 97%;
                overflow: auto;
                color: cornsilk;
                display: table-cell;
                vertical-align: middle;
                text-align: left;
            }

            .footer {
                background-color: rgb(0, 0, 0);
                clear: both;
                text-align: center;
                position: absolute;
                color: cornsilk;
                left: 0;
                right: 0;
                bottom: 0;
            }

            .content {
                float: left;
                position: absolute;
                right: 0;
                left: 102px;
                height: 90%;
                color: cornsilk;
                overflow: auto;
                background-color: rgba(0, 0, 0, 40%);

            }


            .atalk {
                margin: 30px;
                text-align: center;
                font-size:20px;
                
            }

            .atalk span {
                display: inline-block;
                border-radius: 10px;
                color: #fff;
                padding: 5px 10px; 
                font-size:40px;
                word-wrap: break-word;
                width: 100%;

            }

            a:link {
                color: cornsilk;
            }

            a:visited {
                color: cornsilk;
            }
        </style>
    </head>

    <body class='body'>
        <div class='head'>
            <h1 class="word">
                <form action='/messIn' method=post enctype="multipart/form-data">
                    <center>
                        WebChat<font size=1> public</font>
                        <span>
                            <input type=text name= Message size=30 />
                            <input type=submit value= send>
                        </span>
                    </center>
                </form>
            </h1>
        </div>
        <div class='right_lable'>
            <a href='/signout'>Sign out</a><br />
        </div>
        <table class='menu'>
        """
    userlist = gen_userlist()
    Page_end1 = """ 
                </table>
                <div class="content">
        """
    pubmess = get_pubmessage()
    page_end2 = """ 

        </div>

        <div class='footer'>
            <center>hwan685</center>

        </div>

    </body>

    </html>
        """
    Page = Page_head+userlist+Page_end1+pubmess+page_end2
    return Page
def get_pubmessage():
    b = """ """
    data_read = dataOperation.SELECT_pubmessage()
    for items in data_read:
        a = """
            <div class="atalk">%s <br/>
            <span>%s</span>
            <font size=1> %s</font>
            <hr/>
        </div>
        """%(items[0],items[1],items[2])
        b = b+a
    return b
#--------------------------------------------------------------------------------------

def private_screen(ip):
    Page_head = """ 
                <!DOCTYPE html>
    <html class='html'>
    <title>WebChat</title>

    <head>
        <title>Login</title>
        <style type='text/css'>
            .html {
                height: 90%;
                margin: 0;
            }

            .body {
                background-image: url('./static/background.jpg');
                background-repeat: no-repeat;
                background-size: cover;
                background-attachment: fixed;
                height: 100%;
                margin: 0;
            }
            .word{
                color: rgb(255, 255, 255);

            }

            .head {
                background-color: rgba(0, 0, 0, 50%);
                margin-bottom: 0;
                margin-top: 0;
                height: 7%;
            }

            .right_lable {
                position: absolute;
                top: 0px;
                right: 10px;
                color: cornsilk;
                text-align: right;
            }

            .menu {
                float: left;
                border-right: 2px solid rgb(92, 92, 92);
                width: 100px;
                height: 97%;
                overflow: auto;
                color: cornsilk;
                display: table-cell;
                vertical-align: middle;
                text-align: left;
            }

            .footer {
                background-color: rgb(0, 0, 0);
                clear: both;
                text-align: center;
                position: fixed;
                color: cornsilk;
                left: 0;
                right: 0;
                bottom: 0;
            }

            .content {
                float: left;
                position: absolute;
                right: 0;
                left: 102px;
                height: 90%;
                color: cornsilk;
                background-color: rgba(0, 0, 0, 40%);

            }

            a:link {
                color: cornsilk;
            }

            a:visited {
                color: cornsilk;
            }

            .talk_con {
                width: 600px;
                height: 500px;
                border: 1px solid #666;
                margin: 50px auto 0;
                background: rgba(0, 0, 0, 40%);
            }

            .talk_show {
                width: 580px;
                height: 420px;
                border: 1px solid #666;
                background: rgba(0, 0, 0, 40%);
                margin: 10px auto 0;
                overflow: auto;
            }

            .talk_input {
                width: 580px;
                margin: 10px auto 0;
            }

            .whotalk {
                width: 80px;
                height: 30px;
                float: left;
                outline: none;
            }

            .talk_word {
                width: 420px;
                height: 26px;
                padding: 0px;
                float: left;
                margin-left: 10px;
                outline: none;
                text-indent: 10px;
            }

            .talk_sub {
                width: 56px;
                height: 30px;
                float: left;
                margin-left: 10px;
            }

            .atalk {
                margin: 10px;
            }

            .atalk span {
                display: inline-block;
                background: #03476e;
                border-radius: 10px;
                color: #fff;
                padding: 5px 10px;
            }

            .btalk {
                margin: 10px;
                text-align: right;
            }

            .btalk span {
                display: inline-block;
                background: #a05800;
                border-radius: 10px;
                color: #fff;
                padding: 5px 10px;
            }
        </style>
    </head>

    <body class='body'>
        <div class='head'>
            <h1 class="word">
                <center>
                    WebChat<font size= 1>  private</font>
                </center>
            </h1>
        </div>
        <div class='right_lable'>
            <a href='/signout'>Sign out</a><br />
            <a href='/broadcast'>broadcast</a><br />
        </div>
        <table class='menu'>
                """
    userlist = gen_userlist()
    upi = dataOperation.SELECT_nameByip(ip)
    Page_a_1 = """ 
             </table>
        <div class="content">
        <div class="talk_con">
         <center><span>%s</span></center>
         <div class="talk_show">
                """%upi
    chat = gen_chat(upi)
    Page_end = """</div>
                    <form action='/send_private' method=post enctype="multipart/form-data">
                    <div class="talk_input">
                        <input type="text" name = Message class="talk_word">
                        <input type='hidden' name = ip value =%s>
                        <input type=submit value= send class=talk_sub>
                    </div>
                    </form>
                </div>
            </div>

            <div class='footer'>
                <center>hwan685</center>

            </div>

        </body>

        </html> """%ip
    Page = Page_head +userlist +Page_a_1+chat+Page_end
    return Page


def gen_chat(upi):
    #Page = """
     #   <div class="atalk">
     #               <font size = '1'>%s</font><br/>
     #               <span>%s</span>
     #           </div>
     #   <div class="btalk">
     #               <font size = '1'>%</font><br/>
     #               <span>im fine</span>
     #   </div>              
     #            """
    message = dataOperation.SELECT_all_message(upi)
    Page = """ """
    for items in message:
        if items[0] == 'R':
            a = """
                    <div class="atalk">
                        <font size = '1'>%s</font><br/>
                        <span>%s</span>
                    </div>
                """%(items[2],items[1])
            Page = Page+a;
        else:
            a = """
                    <div class="btalk">
                        <font size = '1'>%s</font><br/>
                        <span>%s</span>
                    </div>
                """%(items[2],items[1])
            Page = Page + a
    return Page