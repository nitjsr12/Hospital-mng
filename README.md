# Hospital Management System
This project is for hospital management system. In this project, I have used lots of feature which is the followings:
* Doctor database management
* Patient database management
* Prescription management
* Appointment management
* Human Resource database management
* Receptionist database management
* Invoicing, etc.

## Setup project
1. Clone the repository.
2. Go to the project ```cd hospital_mng```
3. intall the requirement packages ```pip install -r requirements.txt``` 
4. Migrate the database ```python manage.py migrate```
5. Create the admin of the database ```python manage.py createsuperuser```
6. Login into admin then we have to create group inside ```Group section``` which names is following ```Doctor```, ```Patient```, ```Receptionist```, ```HR``` by the run of this url ```127.0.0.1:8000/admin```.
7. Run the server ```python manage.py runserver```
8. url ```127.0.0.1:8000```
## Django admin user password 
> admin user: raviadmin    
> password: Mca@12306
## HR  user password 
> HR login: Ravi06      
> password: sumit123
## Receptionist  user password 
> Receptionist login: Ravi123           
> password: surya123


#### Note: You must have setup Django enviroment into your system.

## Project environment
* Python - 3.8
* Django - 3.0.5
* Editor - VS Code
* Database - SQLite
