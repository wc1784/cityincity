#!/usr/bin/python
import cgi
import cgitb
import pymysql as mydb
import os					     #import os module
from http import cookies			     #from http module import cookies object
cgitb.enable( )
print("Content-Type: text/html \n")

elements		= cgi.FieldStorage()
comment = elements.getvalue('comment')
rating = elements.getvalue('rating')
bookid = elements.getvalue('bookid')
conn = mydb.connect(host='localhost', user='team2', password='team2', database='team2')
cursor = conn.cursor()

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    # c=Cookie.SimpleCookie() 坑
    c = cookies.SimpleCookie()
    c.load(cookie_string)
    try:
        userCookieValue = c['username'].value
        useridCookieValue = c['userid'].value
        if bookid is not None:
            sql = (F"""INSERT INTO review(review_time, rating, comment, book_id, member_id)
                        VALUES (now(), '{rating}', '{comment}', '{bookid}', '{useridCookieValue}');""")
            cursor.execute(sql)
            conn.commit()
            print('<head><meta charset="UTF-8" http-equiv="refresh" content="3; url=userhome.py"><link rel="stylesheet" type="text/css" '
              'href="home.css"/><link rel="stylesheet" type="text/css" href="register.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">'
              "<style>h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}</style><title>Redirecting...</title></head>")
            print("<body><p>Your review has been successfully submitted.</p></body>")
        else:
            print("No book ID, pls check")
    except:
        print(
            '<head><meta charset="UTF-8" http-equiv="refresh" content="3; url=userhome.py"><link rel="stylesheet" type="text/css" '
            'href="home.css"/><link rel="stylesheet" type="text/css" href="register.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">'
            "<style>h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}</style><title>Redirecting...</title></head>")
        print("<body><p>You have not login. Please Login in before submit your review.</p></body>")
else:
    print(
        '<head><meta charset="UTF-8" http-equiv="refresh" content="3; url=userhome.py"><link rel="stylesheet" type="text/css" '
        'href="home.css"/><link rel="stylesheet" type="text/css" href="register.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">'
        "<style>h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}</style><title>Redirecting...</title></head>")
    print("<body><p>You have not login. Please Login in before submit your review.</p></body>")
cursor.close()
conn.close()