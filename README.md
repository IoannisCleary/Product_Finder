Product_Finder
==============
Getting started
----
Within a virtual environment:<br/>
	1. Run "pip -install -r requirements.txt" and let it install what you need for the project to run<br/>
	2. Go into the project folder ("cd productfinder") <br/>
	3. Run "python manage.py syncdb" to create a database<br/>
	4. Run "python population_script.py" to populate the database<br/>
	5. Run "python manage.py runserver" to start up the server<br/>
	6. Open web-browser, it should start up on the website "http://127.0.0.1:8000/product_finder/"<br/>
