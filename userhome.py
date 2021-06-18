#!/usr/bin/python
import cgi
import cgitb
import pymysql as mydb
import os					     #import os module
from http   import cookies			     #from http module import cookies object
from urllib import parse
cgitb.enable( )
print("Content-Type: text/html \n")
cookieStr = os.environ.get("HTTP_COOKIE")	#get the HTTP cookies
myCookies = cookies.SimpleCookie(cookieStr)	#create an object from existing cookies

userid = myCookies['userid'].value		#to obtain a single cookie value
username = myCookies['username'].value
if userid is not None:
    print('<head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" '
        'href="home.css"/><link rel="stylesheet" type="text/css" href="register.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">'
        "<style>h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}</style><title>Register to join the Sam's</title></head>")
    print("""<body><div class="wrapper">
            <nav>
            <div class="logo">Reader Sam's</div>
            <ul>
                <li><a class="active" href="userhome.py">Home</a></li>
                <li><a href="todaysbook.html">Today's Book</a></li>
                <li><a href="hotbooks.html">Hot Books</a></li>
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
    print(F"<p>Hi, {username}!</p>")
    print("<p>Welcome to Sam's bookclub</p></div></div></div></div>")
    html_part2 = ("""<div class="today-book">
            <h1>Today's Book......</h1>
            <div class="today-book-grid">
                <div class="today-book-pic">
                    <img src="book-socialdistance.jpg">
                    <h2 style="text-align: center">The Art of Social Distancing</h2>
                </div>
                <div class="today-book-text">
                    <h3>Zone One</h3>
                    <p>A pandemic has devastated the planet, sorting humanity into two types: the uninfected and the infected, the living and the living dead. Mark Spitz is a member of one of the three-person civilian sweeper units tasked with clearing lower Manhattan of the remaining feral zombies...</p> </br>
                    <h3>Walden</h3>
                    <p> In this new edition of the classic text, ample space is given for readers to record their thoughts right alongside Thoreau’s words. It is a tool to study one of the great works of American literature. </p> </br>

                    <a href="todaysbook.html"><p>Learn more>></p></a>
                </div>
                </div>
            </div>
            <footer class="footer">
        <div class="row">
          <div class="col-6">
            <p><i class="fa fa-phone" aria-hidden="true"></i> +1 (666）888 6888</p>
    			<p><i class="fa fa-envelope" aria-hidden="true"></i> info@readersams.com</p>
          </div>
          <div class="col-6" style="text-align: right;">
            <h3>Reader Sam's</h3>
            <p>Dedicated to the most inspiring community for book lovers </p>
            </ul>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-12">&copy; 2020 Reader Sam's - <a href="#">Facebook</a> - <a href="#">Twitter</a></div>
        </div>
    </footer>
    </body>""")
    print(html_part2.encode('ascii', 'ignore').decode('ascii'))
else:
    print('<head><meta charset="UTF-8" http-equiv="refresh" content="0; url=home.html"><link rel="stylesheet" type="text/css" '
          'href="home.css"/><link rel="stylesheet" type="text/css" href="register.css"><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">'
          "<style>h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}</style><title>Redirect</title></head>")
    print('<p>Redirecting...</p>')
