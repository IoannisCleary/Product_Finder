Product_Finder
==============
Getting started
----
set up virtual environment:<br/>
	1. virtualenv env <br/>
	2. source env/bin/activate <br/>
	3. cd into folder with the requirements.txt file
setting up web app
	4. 1. Run "pip install -r requirements.txt" and let it install what you need for the project to run<br/>
		1. if this doesn't work run pip -install :
			1. Django==1.5.4 or django==1.5.4
			2. django-bootstrap==0.2.4
			3. django-bootstrap-form==3.1
			4. django-forms-bootstrap==3.0.1
	5. Go into the project folder ("cd productfinder") <br/>
	6. Run "python manage.py syncdb" to create a database<br/>
	7. Run "python population_script.py" to populate the database<br/>
	8. Run "python manage.py runserver" to start up the server<br/>
	9. Open web-browser, it should start up on the website "http://127.0.0.1:8000/product_finder/"<br/>
