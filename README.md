# Useful Code

A repo containing some useful helper functions.

## Repo Structure

| File                    | Purpose                                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| pyproject.toml          | Replaces setup.py. Holds all the project metadata and instructions on how the package should be built.                |
| tox.ini                 | A list of environments and commands to be run in them. Currently just specifies to run Pytest on Python 3.10          |
| .github                 | Contains the tests.yml file which defines the Github actions. Currently these runs tests, triggered by pushes or PRs. |
| .pre-commit-config.yaml | Runs Black to format all code anytime you commit to Git.                                                              |


Pre-commit was setup using these instructions: https://pre-commit.com/  

1) `pip install pre-commit`
2) Add it to requirements.txt
3) Create the .pre-commit-config.yaml file
4) Run `pre-commit install` to install any hooks referenced in step 3

To be used on another machine you will first need to run ```pre-commit install```
(after installing the pre-commit package).

The project uses [Google's styleguide for docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).