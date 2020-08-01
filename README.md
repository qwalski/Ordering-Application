# Ordering-Application
Django Application to order items

## Steps to run the application

1-> clone the repo <br/>
2-> move inside the repo  <br/>
2-> install virtual env if not intalled (command -> sudo apt install virtualenv)  <br/>
3-> create virtualenv (command -> virtualenv env), here env is the name of enviroment <br/>
4-> activate virtual env (command-> source env/bin/activate)  <br/>
5-> install all the dependencies present in requirements.txt file   <br/>
(command -> pip3 install -r requirements.txt)  <br/>
6-> Migrate the database (command ->python3 manage.py migrate)  <br/>
7-> Populate/Reset the database (command->python3 manage.py seed)  <br/>
8-> Run the server (command->python3 manage.py runserver)  <br/>


## Key Points

2 Users are created with their username and password as follows <br/>
<br/>
i) username -> admin1<br/>
   password -> password<br/>
   <br/>
ii) username -> admin2<br/>
    password -> password<br/>

## Screenshots of Django Application
### Login Page
<img src = "https://github.com/qwalski/Ordering-Application/blob/master/Readme_Images/login%20page.png" />

### Inventory Page
<img src = "https://github.com/qwalski/Ordering-Application/blob/master/Readme_Images/Inventory%20page.png" />

### Order Details Page
<img src = "https://github.com/qwalski/Ordering-Application/blob/master/Readme_Images/Order%20details%20page.png" />
