# [Advent of Code](https://adventofcode.com/)
These are my solutions to the coding puzzles of advent of code.
All puzzle are done in Python because I like the flexibility and ease of use of this language

## Setup
### Run the following commands
Create a virtualenv
> python -m venv venv

Activate the virtualenv
> source venv/bin/activate

Install the requirements
> pip install -r requirements.txt
 
### Acquire a valid session id
1. Go to [Advent of Code](https://adventofcode.com/) and open the devtools.
2. Navigate to Application -> Cookies
3. Copy the value of the session cookie and paste it in _config.py.tpl_
4. Remove the _.tpl_ extension, so you're left with _config.py_

## The script aoc.py
### What does it do
This script will open a browser window or new tab to the puzzle specified by the arguments.\
Next it creates 2 python files with some code to read the input file or test file.\
Finally an input.txt will be generated with your puzzle input for the day, and an empty test.txt for testing purposes.\


### How to use
```bash
usage: aoc.py [-h] year day                  
                                             
AOC management command.                      
                                             
positional arguments:                        
  year        Year of the event, e.g. 2015   
  day         Day of the puzzle, e.g. 5      
                                             
options:                                     
  -h, --help  show this help message and exit
```

Example usage
> python aoc.py 2015 1