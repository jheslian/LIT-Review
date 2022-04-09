# An application that request or publish reviews of books or articles.

## Objectives:

- A user could ask for a review of a particular book or article.
- A user could search for an interesting articles or books to read, based on the reviews of others.


## Getting started:
**Note**: Make sure you have python, virtual environment and git on your machine : 
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
5. Run the program : 
	for unix or macos: `python3 manage.py. runserver`
	for windows: `py manage.py. runserver`
	***Note*** : The default port will open at 8000, if you are already using it you could either close it and try again or use another any other port  like `python3 manage.py. runserver 9000` for mac as exemple