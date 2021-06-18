#!/usr/bin/python
import cgi
import cgitb
import pymysql as mydb
cgitb.enable( )

print("Content-Type: text/html \n")
print("""<head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="home.css"/>
        <link rel="stylesheet" type="text/css" href="book-detail.css"/>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">
        <style>
            h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}
        </style>
        <title>Book Detail</title>
    </head>
    <body>
        <div class="wrapper">
            <nav>
            <div class="logo">Reader Sam's</div>
            <ul>
                <li><a href="home.html">Home</a></li>
                <li><a href="todaysbook.html">Today's Book</a></li>
                <li><a href="hotbooks.html">Hot Books</a></li>
                <li><a href="reviews.html">Reviews</a></li>
                <li><a href="search.html">Search</a></li>
            </ul>
            </nav>
        </div>
        <div class="banner">
            <div class="inner">
            </div>
        </div>""")
elements		= cgi.FieldStorage()
book_id = elements.getvalue('isbn')
conn = mydb.connect(host='localhost', user='team2', password='team2', database='team2')
cursor = conn.cursor()
sql = F""" SELECT title, isbn, concat(author_fname, ' ',author_lname) author, category, publish_year, pub_name publisher FROM book
               join author on book.author_id=author.author_id
               join publisher on book.pub_id=publisher.pub_id
               where isbn ={book_id} """

sql_detail =F"""SELECT title, comment, rating, mem_name from book
        join review on book.book_id = review.book_id 
        join member on review.member_id = member.member_id
        where book.isbn ={book_id}"""

#get book basic info
try:
    cursor.execute(sql)
    result_tu = cursor.fetchall()
    result = result_tu[0]
    title = result[0]
    isbn = result[1]
    author = result[2]
    category = result[3]
    publish_year = result[4]
    publisher = result[5]
    print(F"""<div class="book-detail">
        <h1>{title}</h1>
        <div class="book-detail-container">
        <div class="book-img"><img src="book-cover.jpg"></div>
        <div class="book-info">
            <p>Arthor: {author}</p>
            <p>ISBN: {isbn}</p>
            <p>Publisher: {publisher}</p>
            <p>Publish year: {publish_year}</p>
            <p>Category: {category}</p>
        </div>
        </div>
        <div class="book-review">
            <h1>Reviews......</h1>""")
    print("Connection success!")
except mydb.Error as e:
    print('Database Connection Error')
    exit()


#get book review info
try:
    cursor.execute(sql_detail)
    review = cursor.fetchall()
    for row in review:
        comment = row[1]
        rating = row[2]
        members_name = row[3]
        print(F"""<ul>
            <li><b>{members_name}</b> Rating:{rating}</li>
            <li>{comment}</li>
        </ul>""")
    print("""</div>
</div>
<div class="write-review">
<p>Write your own review</p>
</div>
<footer class="footer">
    <div class="row">
      <div class="col-6">
        <p><i class="fa fa-phone" aria-hidden="true"></i> +44 (0)123 456 789</p>
			<p><i class="fa fa-envelope" aria-hidden="true"></i> info@landingpage.com</p>
      </div>
      <div class="col-6" style="text-align: right;">
        <h3>Heading</h3>
        <p>Quod cum accidisset ut alter alterum necopinato videremus, surrexit statim. Aliena dixit in physicis nec ea ipsa, quae tibi probarentur; Quorum altera prosunt, nocent altera. Qui potest igitur habitare in beata vita summi mali metus? Non quam nostram quidem, inquit Pomponius iocans; In motu et in statu corporis nihil inest, quod animadvertendum esse ipsa natura iudicet?iam, incidunt?</p>
        </ul>
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-12">&copy; 2020 Reader Sam's - <a href="#">Facebook</a> - <a href="#">Twitter</a></div>
    </div>
</footer>
</body>""")
except mydb.Error as e:
    print('Database Connection Error')
    exit()
