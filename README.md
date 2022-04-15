
# An application that request or publish reviews of books or articles.

## Objectives:

- A user could ask for a review of a particular book or article.
- A user could search for an interesting articles or books to read, based on the reviews of others.

## Functionnalities:
1. Sign up - create an account
2. Log in - User log in
3. Flux - The main page of the application where:
	- They can see the tickets and reviews of all users they follow
	- They should also see their own tickets and reviews, as well as any reviews in response to their own tickets 
	- They can post their ticket requesting a review for a book or literature article
	- The users who follow them can then submit their reviews in response to the ticket.
	- Users should also be able to post reviews for books and articles that do not have a ticket yet.
4. Posts page where:
	- User can see their own tickets and reviews separately
	- User can edit, and delete their own tickets and reviews
5. Follow page where:
	 - Users will be able to follow other users and should also have the option to unfollow them
	 - Users will be able to see who follows them
6. Log out 


## Getting started:
**Note**: Make sure you have python(atleast version 3.8) , virtual environment and git on your machine:
	- `python -V` : command to check the version python if its installed
	- verify that you have the venv module : `python -m venv --help` if not please check https://www.python.org/downloads/. You could also use any other virtual environment to run the program(**if you opted to use other virtual environment the next commands are not suitable to run the program**)
	- `git --version` : to check your git version if its installed or you could download it at https://git-scm.com/downloads
 1. Clone the repository on the terminal or command prompt : `git clone https://github.com/jheslian/LIT-Review.git`
 2. Create a virtual environment with "venv"  
	 - `cd LIT-Review` :  to access the folder 
	 - python -m venv ***environment name*** : to create the virtual environment - exemple: `python -m venv env`
3. Activate the virtual environment:
	for unix or macos:
	- source ***environment name***/bin/activate - ex : `source env/bin/activate` if "env" is used as environment name 
	for windows:
	- ***environment name***\Scripts\activate.bat - ex: `env\Scripts\activate.bat`
4. Install the packages with pip: `pip install -r requirements.txt`	
5  Migrate the tables to database:
    for unix or macos: `python3 manage.py migrate`
	for windows: `py manage.py migrate`
6. Run the program :
	for unix or macos: `python3 manage.py runserver`
	for windows: `py manage.py runserver`
	***Note*** : The default port will open at 8000, if you are already using it use another port  like 9000 `python3 manage.py runserver 9000` for mac as exemple
