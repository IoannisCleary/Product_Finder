Product_Finder
==============
Getting started
----
Set up virtual environment:<br/>
	&nbsp;&nbsp;Open bash terminal: <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	1. virtualenv env <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	2. source env/bin/activate <br/> 
	&nbsp;&nbsp;&nbsp;&nbsp;	3. cd into folder with the requirements.txt file <br/>
Setting up web app <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	4. Run "pip install -r requirements.txt" and let it install what you need for the project to run<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;	1. if this doesn't work run "pip install (item from list below)" : <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		1. Django==1.5.4 or django==1.5.4 <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		2. django-bootstrap==0.2.4 <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		3. django-bootstrap-form==3.1 <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		4. django-forms-bootstrap==3.0.1 <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	5. Go into the project folder ("cd productfinder") <br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	6. Run "python manage.py syncdb" to create a database<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	7. Run "python population_script.py" to populate the database<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	8. Run "python manage.py runserver" to start up the server<br/>
	&nbsp;&nbsp;&nbsp;&nbsp;	9. Open web-browser, it should start up on the website "http://127.0.0.1:8000/product_finder/"<br/>
