#!/usr/bin/python
import cgi
import cgitb
import pymysql as mydb
cgitb.enable( )

print("Content-Type: text/html \n")

elements		= cgi.FieldStorage( )

htmlpart1 = """	<!DOCTYPE html>
				<html lang="en">
				<head>
					<meta charset="UTF-8">
					<link rel="stylesheet" type="text/css" href="home.css"/>
					<link rel="preconnect" href="https://fonts.gstatic.com">
					<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300&display=swap" rel="stylesheet">
					<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;800&display=swap" rel="stylesheet">
					<link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo&display=swap" rel="stylesheet">
					<style>
						h1,h1,h3 {font-family: 'East Sea Dokdo', sans-serif;}
						button{
    background-color:  rgba(0,0,0,0);
    border: none;
    color: black;
    padding: 0;
    text-align: left;
    text-decoration: none;
    font-size: 16px;
    box-shadow: none;
}
button:hover{
    color: blue;
    background-color: rgba(0,0,0,0);
    box-shadow: none;
}
					</style>
					<title>Sam's BookClub - Hot Books</title>
				</head>
				<body>
				<!--navigation part-->
					<div class="wrapper">
						<nav>
						<div class="logo">Reader Sam's</div>
						<ul>
							<li><a href="userhome.py">Home</a></li>
							<li><a href="todaysbook.html">Today's Book</a></li>
							<li><a class="active" href="hotbooks.py">Hot Books</a></li>
							<li><a href="reviews.html">Reviews</a></li>
							<li><a href="search.html">Search</a></li>
						</ul>
						</nav>
					</div>
				<!--banner part-->
					<div class="banner">
						<div class="inner">
							 <div class="banner-text">
									<p>Share your thoughts of books.</p>
							 </div>
						</div>
					</div>
				<div class="hot-books">
					<div class="hot-books-container">
					<h1>Hot Books ......</h1>
						<div class="hot-book-grid">
				"""
print(htmlpart1)

conn = mydb.connect(host='localhost', user='team2', password='team2', database='team2')
cursor = conn.cursor()


sql = F""" select book.book_id, title, concat(author_fname,' ',author_lname) author, isbn, round(avg(rating),1) rating, count(review_id) review 
			from book
			join review on review.book_id=book.book_id
			join author on author.author_id=book.author_id
			where DATEDIFF(sysdate(),review_time)<=30 
			group by book.book_id, title, concat(author_fname,' ',author_lname)
			order by 5 desc, 4 desc
			limit 10"""
try:
	# print(sql)
	cursor.execute(sql)
	result = cursor.fetchall()
	for index, row in enumerate(result):
		book_id = row[0]
		title = row[1]
		author = row[2]
		isbn = row[3]
		print(f"""<div class='b {index+1}'> <img src='cover/%s.jpg' align='middle' height='200px'><form action="book_detail.py"><button type="submit" value="{isbn}" name="isbn"><h4>%s</h4></button></form><p>%s</p> </div>""" % (book_id, title, author))

except mydb.Error as e:
	print('Database Connection Error')
	print("</body></html>")
	exit()


cursor.close( )
conn.close( )

htmlpart2 = """		</div>
				</div>
			</div>
				<footer class="footer">
					<div class="row">
					  <div class="col-6">
						<p><i class="fa fa-phone" aria-hidden="true"></i> +1 (666)888 6888</p>
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
				</body>
				</html>
				"""
print(htmlpart2)