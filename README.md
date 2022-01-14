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

6-Create the docker container for postgres
		docker run -v <path to db file you want >:/var/lib/postgresql/data -d -e POSTGRES_USER=restframework -e
		POSTGRES_PASSWORD=restframework -e POSTGRES_DB=postgres --name restframework_db -p 5445:5432 postgres		

7-Check your database container is up & running by running the following command
		psql -h 0.0.0.0 -p 5445 -U restframework -d restframework --password		
		
		


