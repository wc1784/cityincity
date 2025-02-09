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
password_1 = elements.getvalue('password')

username = [username_1]
password = [password_1]

select_mem = "SELECT mem_name,password FROM member;"

#no quotes around numeric data
db_username = []
db_password = []
conn = mydb.connect(host='localhost', user='team2', password='team2', database='team2')
cursor = conn.cursor()
cursor.execute(select_mem)
rows = cursor.fetchall()
for row in rows:
    db_username.append(row[0])
    db_password.append(row[1])


def inter(a,b):
    return list(set(a)&set(b))


print("""<body><div class="wrapper">
        <nav>
        <div class="logo">Reader Sam's</div>
        <ul>
            <li><a class="active" href="home.html">Home</a></li>
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
if inter(username,db_username):
    mem_id = db_username.index(username_1)
    if password_1 != db_password[mem_id]:
        print("<h4>Password Error<h4>")
        print('<a href="home.html"><p>Try agian</p></a></div></div></div></div>')
    else:
        print("<p>Login Success</p>")
        print("<p>Welcome to Sam's bookclub</p></div></div></div></div>")
else:
    print("<h4>Sorry, this user name does not exist.</h4>")
    print('<a href="register.html"><p>Do not have a account? Go to register</p></a></div></div></div></div>')

htmlpart2="""<div class="today-book">
        <h1>Today's Book ……</h1>
        <div class="today-book-grid">
            <div class="today-book-pic">
                <img src="book-socialdistance.jpg">
                <h2 style="text-align: center">Arts About Social distance</h2>
            </div>
            <div class="today-book-text">

                <h3>BOOK NAME 1</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Huius, Lyco, oratione locuples, rebus ipsis ielunior. At ille pellit, qui permulcet sensum voluptate. Ego vero isti, inquam, permitto. Quod iam a me expectare noli. Duo Reges: constructio interrete.</p>
                <h3>BOOK NAME 2</h3>
                <p>Quare hoc videndum est, possitne nobis hoc ratio philosophorum dare. Sed quot homines, tot sententiae; Praeclarae mortes sunt imperatoriae; Quid enim ab antiquis ex eo genere, quod ad disserendum valet, praetermissum est? </p>
                <h3>BOOK NAME 3</h3>
                <p>Quod cum accidisset ut alter alterum necopinato videremus, surrexit statim. Aliena dixit in physicis nec ea ipsa, quae tibi probarentur; Quorum altera prosunt, nocent altera.</p>
                <a href="#"><p>Learn more>></p></a>
            </div>
            </div>
        </div>
<!--hot books recommendation-->
    <div class="hot-books">
        <div class="hot-books-container">
        <h1>Hot Books ……</h1>
        <div class="hot-book-grid">
            <div class="b1">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b2">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b3">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b4">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b5">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b6">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b7">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b8">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b9">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
            <div class="b10">
                <img src="book-cover.jpg" align="middle" height="200px">
                <a href="#"><h4>BOOK NAME</h4></a>
                <p>Arthur Name</p>
            </div>
</div>
        </div>
        </div>
<!--Review for homepage-->
<div class="reviews">
    <h1>Reviews ……</h1>
    <div class="reviews-grid">
        <div class="review-book">
            <img src="book-cover2.jpg" align="middle" height="200px">
        </div>
        <div class="review-detail">
            <h4>REVIEW NAME</h4>
            <p style="font-style: italic"><span>User name</span>  BOOK NAME</p>
            <p>Quod cum accidisset ut alter alterum necopinato videremus, surrexit statim. Aliena dixit in physicis nec ea ipsa, quae tibi probarentur; Quorum altera prosunt, nocent altera. Qui potest igitur habitare in beata vita summi mali metus? Non quam nostram quidem, inquit Pomponius iocans; In motu et in statu corporis nihil inest, quod animadvertendum esse ipsa natura iudicet?</p>
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
</body>"""
print(htmlpart2.encode('ascii', 'ignore').decode('ascii'))

cursor.close()
conn.close()