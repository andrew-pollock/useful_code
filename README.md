## Hello World

Explanation of what's going on:  
pyproject.toml holds all the project metadata and instructions on how it should be built.  
tox.ini has a list of different environments (currently just Python 3.10) and 
the commands it will run in those environemnts. Currently it's just set to run
Pytest in each env, but I could define a "flake" env where it runs the flake8 
command to lint my files.  

.github will hold a workflows folder, with a tests.yml file. 

.pre-commit-config.yaml runs Black to format all code anytime you commit to Git.
I think the setup for this is done locally, not controlled by git/the project?  
It was setup using instructions from here: https://pre-commit.com/

1) pip install pre-commit
2) Add it to requirements.txt
3) Create the .pre-commit-config.yaml file
4) Ran pre-commit install to install any hooks referenced in step 3