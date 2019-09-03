# Readme MAE International Student Website 

## Steps to follow to run on your local machine 

1. Open up terminal
2. Navigate to where you want to 'git clone' our repository
3. Click on the green 'Clone or download' button on our repo
4. Copy the address
5. Run `git clone <the copied address>` in the terminal
6. Move into the cloned folder by `cd mae_demo`
7. Run `./health_app_setup.command` to download our setups by typing `./health_app_setup.command` onto the terminal

All set! The server should have launched at this time. Open up your favorite browser and navigate to http://127.0.0.1:8000 to look at our website.


## Functionalities in the website 

1. Authentication (google authentication) - signup and login / logout

   For easier website usage, we have signup button and login button. Based on our code logic, if the user have never created an id before, it would automatically make the user create a profile for both login and signup button. If the user already has a profile, the login and signup button will login the user. The reason for having these two buttons that do the same thing is for a more intuitive user experience. 
  
2. Event Page 

     * Event viewing and creating available on main page and through event button on top nav
     * Event viewing, creation, and RSVPing   
     * View a list of events stored in the database. 
     * Create event by clicking the 'create event' button. 
     * RSVP events - RSVP events are stored and saved per user.
   
       * Try logging out and logging into the same account. The RSVPed events should be preserved.  
       * Try logging out and logging into a different newly created account. There should be no RSVPed events. 
   
   
3. Profile Page  

   Profile creation, viewing, editing profile items one at a time 

     * Profile is created when the user creates an account for the first time. 
     * Profile page, user can view the current user profile 
     * There are edit buttons for each profile item, so user can easily edit one at a time. 

4. About Page 

5. PDF download on the main page 




### Google Authentication Resources and Website 

django allauth documentation 
https://django-allauth.readthedocs.io/en/latest/

### Resources 

django documentation 
https://www.djangoproject.com/

front end 
https://www.udemy.com/learn-front-end-development/learn/lecture/10496752?start=360#overview
