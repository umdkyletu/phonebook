## Documentation

Our project is a web application focused on creating a database to **add**, **store**, and **delete** contacts paired with a user interface that makes it easy to find a specific contact. It is designed as a digital phonebook, where the data, such as contact information, will be stored on the computer. It is meant to be accessible to everyone to keep track of their contact information, such as **first nam**e, **last name**, **phone number**, and **contact picture**. 

To run the program, you must first install all the required files using the “pip install” command on your terminal. Modules needed to be installed:



* flask
* flask-login
* Flask-sqlalchemy
* Flask-WTF
* wtforms 

Once the modules are installed, run the Python file “main.py” inside your terminal to create a local host on your computer that has a database you can access. Once you click on the server link, you will be redirected to the web application.

Once on the application, you will see a navigation bar at the top of the page which gives you the option to log in if you have an account or sign up if you do not have one.



* When you create an account, you will need an **email address**, **first name**, and **password** to create an account within the database. You will know your attempt is successful if you are redirected to the homepage. If your attempt fails, there will be an alert at the top notifying you of the problems with your input.
* To log in, simply enter your **email address **and **password**. A successful login will take you to the home page, but you will stay on the page and be alerted if your credentials are invalid.
* To sign out, click the “**Logout**” button at the top left corner of the navigation bar which will redirect you to the login page.

Once signed in, you can create new contacts by inputting their **first name**, **last name**, **phone number**, and a **link** to a photo of them. You will know you have successfully created a contact once a card pops up at the top carrying all the desired information. This information is also saved within the database stored within your computer.

Each contact card contains the option to **delete** or **update** the contact information.



* To **delete**, simply press the “**x**” icon at the top right corner to remove it from your page and the stored information from the database.
* To **update** your contact’s information, press the “**update**” button at the bottom of the card, which will redirect you to the update page. Upon viewing the update page, you will be given a form with the same inputs of **first name**, **last name**, **phone number**, and a **link** to a photo for the contact. If all the inputs follow the parameter requirements, press the **update** button and you will be taken back to the home page to see the newly updated information. This is reflected in the stored data as well.

At the top of the page in the navigation bar, there is a search bar that allows you to search for specific contacts. The search bar takes the exact name or the most similar to what was searched for and returns the **first name**, **last name**, and **phone number** of that contact. If there are the same names for the contact, it will return the information for both contacts.


### <span style="text-decoration:underline;">Bibliography</span>

Codemy.com. (Nov 5, 2021)._Search Blog Posts From Navbar - Flask Fridays #31._[Video]. Youtube. [https://www.youtube.com/watch?v=kmtZTo-_gJY&ab_channel=Codemy.com](https://www.youtube.com/watch?v=kmtZTo-_gJY&ab_channel=Codemy.com)


    This video taught us how to create a search bar and how to search for a contact by querying the database.

Codemy.com. (May 21, 2020)._How To Update The Database - Python and Flask #9._[Video]. Youtube.[https://www.youtube.com/watch?v=4EJwK56pE1Y&t=1s](https://www.youtube.com/watch?v=4EJwK56pE1Y&t=1s)


    This video taught us how to update the database using Flask.

Tech With Tim. (Feb 1, 2021). _Python Website Full Tutorial - Flask, Authentication, Databases & More_. [Video]. Youtube.[https://www.youtube.com/watch?v=dam0GPOAvVI](https://www.youtube.com/watch?v=dam0GPOAvVI)




    We used this video to learn how to create the primary application that we wanted to create. It was also our first time using Flask, so we learned how to install the required modules, connect to a database using Flask, and code with Jinga. This taught us to authenticate users, make posts, and delete them.  

_Testing flask applications_. Testing Flask Applications - Flask Documentation (3.0.x). (n.d.). https://flask.palletsprojects.com/en/3.0.x/testing/ 

This is the Flask testing documentation. We used this to learn how to test a flask app using pytest like we did in class. It involved creating a client and testing the endpoints using the expected HTML response or redirect. 
