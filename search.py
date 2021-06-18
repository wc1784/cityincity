#!/usr/bin/python
import cgi
import cgitb
import pymysql as mydb
cgitb.enable( )

print("Content-Type: text/html \n")

elements		= cgi.FieldStorage( )
search			= elements.getvalue('search')
searchtype		= elements.getvalue('searchtype')

htmlpart1 = """<!DOCTYPE html>
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
					</style>
					<title>Sam's BookClub - Search</title>
				</head>
				<body>
				<!--navigation part-->
					<div class="wrapper">
						<nav>
						<div class="logo">Reader Sam's</div>
						<ul>
							<li><a href="home.html">Home</a></li>
							<li><a href="todaysbook.html">Today's Book</a></li>
							<li><a href="hotbooks.html">Hot Books</a></li>
							<li><a href="reviews.html">Reviews</a></li>
							<li><a class="active" href="search.html">Search</a></li>
						</ul>
						</nav>
					</div>
				<div class="banner-search">
					<div class="inner-search">
						<div class="search-result">
							<table cellpadding="10"  align="center" width=100%>
				"""
print(htmlpart1)

conn = mydb.connect(host='localhost', user='team2', password='team2', database='team2')
cursor = conn.cursor()
# if user search with title
if searchtype == 'title':
	sql = F""" SELECT title, isbn, concat(author_fname, ' ',author_lname) author, category, publish_year, pub_name publisher FROM book
               join author on book.author_id=author.author_id
               join publisher on book.pub_id=publisher.pub_id 
               where title LIKE "%{search}%" """
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		print("<th>Title</th><th>ISBN</th><th>Author</th><th>Category</th><th>Publish Year</th><th>Publisher</th>")
		for row in result:
			title = row[0]
			isbn = row[1]
			author = row[2]
			category = row[3]
			publish_year = row[4]
			publisher = row[5]
			print(F'<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><form action="book_detail.py"><button type="submit" name="isbn" value="{isbn}"">Details</button></form></td></tr>' % (title, isbn, author, category, publish_year, publisher))
	except mydb.Error as e:
		print('Database Connection Error')
		exit()

# if user search with isbn
elif searchtype == 'isbn':
	sql = F""" SELECT isbn, title, concat(author_fname, ' ',author_lname) author, category, publish_year, pub_name publisher FROM book
						join author on book.author_id=author.author_id
						join publisher on book.pub_id=publisher.pub_id
						where isbn LIKE "%{search}%" """
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		print("<th>ISBN</th><th>Title</th><th>Author</th><th>Category</th><th>Publish_year</th><th>Publisher</th>")
		for row in result:
			isbn = row[0]
			title = row[1]
			author = row[2]
			category = row[3]
			publish_year = row[4]
			publisher = row[5]
			print(F'<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><form action="book_detail.py"><button type="submit" name="isbn" value="{isbn}">Details</button></form></td></tr>' % (isbn, title, author, category, publish_year, publisher))
	except mydb.Error as e:
		print('Database Connection Error')
		exit()

# if user search with author
else:
	sql = F""" SELECT concat(author_fname, ' ',author_lname) author, title, isbn, category, publish_year, pub_name publisher FROM book
						join author on book.author_id=author.author_id
						join publisher on book.pub_id=publisher.pub_id
						where concat(author_fname, ' ',author_lname) LIKE "%{search}%" """
	try:
		cursor.execute(sql)
		result = cursor.fetchall()
		print("<th>Author</th><th>Title</th><th>ISBN</th><th>Category</th><th>Publish_year</th><th>Publisher</th><th>Book detail</th>")
		for row in result:
			author = row[0]
			title = row[1]
			isbn = row[2]
			category = row[3]
			publish_year = row[4]
			publisher = row[5]
			print(F'<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><form action="book_detail.py"><button type="submit" name="isbn" value="{isbn}">Details</button></form></td></tr>' % (author, title, isbn, category, publish_year, publisher))
	except mydb.Error as e:
		print('Database Connection Error')
		print("</body></html>")
		exit()


cursor.close( )
conn.close( )

htmlpart2 = """				</table>
						</div>
					</div>
				</div>
				<script>
				function book_detail(){
						window.open('book_detail.py')
				}
				</script>
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
