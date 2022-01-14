Django Rest framework with PostgreSQL database
      - User registration
      
      - User login
      
      - Each user could create multiple products and get them
      
      - All users could retrieve products data




instructions to run your code
*****************************

1-clone the repository to your local machine:
		https://github.com/HESHAM-WebDev/Bit68-Taskapp.git
		
		
2-Confirm your Python is at least version 3.7.0
		python -V
		
		
3-Create a Python virtual environment and install dependencies:
		python -m venv venv
		
		
		source venv/bin/activate
		
		
		pip install --upgrade pip
		
		
		pip install -r requirements.txt
		
		
4-make migrations
		python3 manage.py makemigrations
		
		python3 manage.py migrate
		
		
5-create superuser (username, email, password, confirm-password)
		
		python3 manage.py createsuperuser
		
***********************************************************************************
1-postgres database docker container used as main database

2- flake8 use as a linter

3- pytest used instead of django autotest

4-api collection created
	
		
		


