# weB FOR SIGNUP AND LOGIN
This web app has been developed using the popular Django framework and Bootstrap for the frontend. My motivation to build this project is so that I can learn about Django and tighten up my skills. This mini-app can be easily integrated into a bigger system project that needs to have a registration and login system.

### Basic Features of The App
    
* Register – Users can register and create a new profile
* Login - Registered users can login using username and password
* Social Apps Login – Users can login using their GitHub or Google account
* User Profile - Once logged in, users can create and update additional information such as avatar and bio in the profile page
* Update Profile – Users can update their information such as username, email, password, avatar and bio
* Remember me – Cookie Option, users don’t have to provide credentials every time they hit the site
* Forgot Password – Users can easily retrieve their password if they forget it 
* Admin Panel – admin can CRUD users

![ScreenShot](https://user-images.githubusercontent.com/66206865/131695930-648342b0-010b-44b2-a419-15ad54d47869.png)


### Quick Start
$ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/praveenjayabalan/SCMSI.git
    $ cd Webapp
    
Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate

    $ python3 manage.py makemigrations && python3 manage.py migrate
Create Super user
    
    $ python3 manage.py createsuperuser

### Launching the app
    $ python3 manage.py runserver
   
3. Open a browser and go to http://localhost:8000/

