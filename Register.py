#!/usr/bin/python
import cgi
import cgitb
import pymysql as mydb
cgitb.enable()

print("Content-Type: text/html \n")			#HTTP response header required for CGI
print('<head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" '
      'href="home.css"/><link rel="stylesheet" type="text/css" href="register.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">'
      "<style>h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}</style><title>Register to join the Sam's</title></head>")
elements = cgi.FieldStorage()
username_1 = elements.getvalue('username')
password = elements.getvalue('password')
email = elements.getvalue('email')
birthday = elements.getvalue('birthday')
gender = elements.getvalue('gender')
phone = elements.getvalue('phone')
username = [username_1]
select_mem = "SELECT mem_name FROM member;"
insert_mem = F""" INSERT INTO  member(mem_name, password,email,birthday,gender,phone )
                  VALUES( '{username_1}', '{password}', '{email}', '{birthday}', '{gender}', '{phone}' );"""
#no quotes around numeric data
db_username = []
conn = mydb.connect(host='localhost', user='team2', password='team2', database='team2')
cursor = conn.cursor()
cursor.execute(select_mem)
rows = cursor.fetchall()
for row in rows:
    db_username.append(row[0])


def inter(a,b):
    return list(set(a)&set(b))
print("""<body><div class="wrapper">
        <nav>
        <div class="logo">Reader Sam's</div>
        <ul>
            <li><a class="active" href="home.html">Home</a></li>
            <li><a href="todaysbook.html">Today's Book</a></li>
            <li><a href="hotbooks.py">Hot Books</a></li>
            <li><a href="reviews.html">Reviews</a></li>
            <li><a href="search.html">Search</a></li>
        </ul>
        </nav>
    </div>
    <div class="banner">
        <div class="inner">
            <div class="banner-container">
                <div class="banner-text">
                    <p>Share your thoughts of books.</p>
                </div>
                <div class="banner-login" style="color:#2E1437">""")

if inter(username,db_username):
    print('<body><h1>Username already exist!</h1></body>')
    print('<a href="register.html"><p>Back to the register page</p></a></div></div></div></div>')
else:
    try:
        cursor.execute(insert_mem)
        conn.commit()
        print('<body><h1>Register Successful!</h1></body>')
        print('<a href="home.html"><p>Back to the home page</p></a></div></div></div></div>')
    except mydb.Error as e:
        print('Insert Error: format maybe not match')
        exit()

cursor.close()
conn.close()