Product_Finder
==============
Within a virtual environment:
1. Run "pip -install -r requirements.txt" and let it install what you need for the project to run
2. Go into the project folder ( "cd productfinder" )
3. Run "python manage.py syncdb" to create a database
4. Run "python population_script.py" to populatee the database
5. Run "python manage.py runserver" to start up the server
6. Open web-browser, it should start up on the website "http://127.0.0.1:8000/product_finder/"