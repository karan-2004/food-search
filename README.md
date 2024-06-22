![assignment_prime_numbers_2](https://github.com/karan-2004/food-search/assets/94951738/b8d431cc-b570-4a7c-8e2e-a52e1927815a)
![assignment_prime_numbers_1](https://github.com/karan-2004/food-search/assets/94951738/71559c3a-d0e2-4c03-80a5-ee6456e880c4)

# Steps for setting-up this application in localhost
## Run the following commands in your terminal(lines starting with # are annotations not for execution)
> #Creating a directory for the application

`mkdir foodsearch`

`cd foodsearch`

> #Creating environment(make sure you have python and pip installed)

`pip install venv`

`python -m venv environment`

> #activating environment

> #for windows

`environment/Scripts/activate`

>#for linux

`source environment/bin/activate`

>#Cloning the repository

`git clone https://github.com/karan-2004/food-search searchify -b main`

>#changing the directory

`cd searchify`

>#Installing dependencies

`pip install -r requirements.txt`

>#For database connectivity

`python manage.py migrate`

# Now you are ready to run the application 
>#The final command

`python manage.py runserver`

## search `127.0.0.1:8000` in the browser
