# Picgram
A personal gallery application that lets you display your photos for other users to see.

## Screenshots 
###### Home page
 
<img src="https://github.com/AliKheirAbdi/pictogram/blob/master/picgram.png"> 

## User Story  
  
* Create an account and sign in 
* Upload a pictures to the application. 
* Search for different users using their usernames. 
* Edit and update their profile
* Like and comment on pictures they like
* See their profile with a profile photo and bio.  
* Follow other users and see their pictures on my timeline.  
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/AliKheirAbdi/pictogram.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picgram pip install -r requirements.txt 
```
##### Install and activate Virtual Env
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  On your database setup User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations
 ``` 
 Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
Open the application on your browser `127.0.0.1:8000`.  

## BDD
| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Register      | Fill out the reg form | user is created |
| Login     | Enter username and pwd   | Application logs user in |
| Edit Profile | User fills out biodata and photo | Profile is created|
| Delete Profile| Modal popup with the delete button | The account is deleted
| Share post|pop up to drive upload images | User can edit,caption photo|
| Like photo|click on the like button and like is registerd| button click|
| Comment on photo|click comment and enter comment| User can edit and delete comment
  
## Technology used  
  
* [Python3.7](https://www.python.org/)  
* [Django 2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com) 
* [Javascript]
* [Jquery]
  
## Known Bugs  
* There are currently no known bugs.  
  
## Contact Information   
If you are interested in this project or making contributions, please email me at [akheirali(@)gmail.com]  
  
## License 
MIT
* Copyright (c) 2019 **Ali Kheir**
