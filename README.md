# STAR HOTELS AND ACCOMODATIONS

![Mockup](static/images/amiresponsive.png)

This comprehensive site was designed for the third of four Milestone Projects that the developer must complete during the Full Stack Web Development Program at The Code Institute. The main requirements were to build a full-stack site that allows your users to manage a common dataset about a particular domain.
## UX

The purpose is to design an attractive website, so the costumers can find destinations for theirs next trips.

## User Stories

- As user I want a clear understanding of the website funcionalities.
- As a user I want to be able to view this site on my computer, mobile and tablet.
- As a user I want to be able to create and add a new hotel.
- As a user I want to be able to edit an existing hotel.
- As a user I want to be able to delete an existing hotel.


## Design
### Colour Scheme

- The main colours used are green, blue and yellow, to give the site a clean, modern and professional look.

### Typography

- The Oswald font is used throughout the website with Sans Serif.


### Wireframes

#### hotels.html
1. [Desktop hotels.html](static/wireframe/hotels_desk.pdf)

2. [Mobile hotels.html](static/wireframe/hotels_phone.pdf)

3. [Tablet hotels.html](static/wireframe/hotels_table.pdf)

#### login.html
1. [Desktop login.html](static/wireframe/login_desk.pdf)

2. [Mobile login.html](static/wireframe/login_phone.pdf)

3. [Tablet login.html](static/wireframe/login_tablet.pdf)

#### register.html
1. [Desktop register.html](static/wireframe/login_desk.pdf)

2. [Mobile register.html](static/wireframe/login_phone.pdf)

3. [Tablet register.html](static/wireframe/login_tablet.pdf)

#### add_hotel.html
1. [Desktop add_hotel.html](static/wireframe/addhotel_desk.pdf)

2. [Mobile add_hotel.html](static/wireframe/addhotels_phone.pdf)

3. [Tablet add_hotel.html](static/wireframe/addhotels_tablet.pdf)

#### edit.html
1. [Desktop edit.html](static/wireframe/edit_desk.pdf)

2. [Mobile edit.html](static/wireframe/hotelmngt_phone.pdf)

3. [Tablet edit.html](static/wireframe/edit_tablet.pdf)




## Existing Features.

#### Below is a brief overview of the website and its main features.

- Login

![Login](static/images/login.png)

- Login

![Register](static/images/register.png)

- Add hotel

![Add Hotel](static/images/addhotel.png)

- Edit Card

![editcard.png](static/images/editcard.png)

- Logged Navbar

![Logged Navbar](static/images/loggednavbar.png)


## Frameworks, Languages & Programs Used

### [Gitpod](https://www.gitpod.io/)
- This developer used Gitpod for their IDE while building the website.

### [BootstrapCDN](https://www.bootstrapcdn.com/)
- The project uses Bootstrap v 5.1.0 to simplify the structure of the website.
- The project also uses BootstrapCDN to provide icons from FontAwesome.
### [Google Fonts](https://fonts.google.com/)
- The project uses Google fonts to style the website fonts.

### [Balsamiq](https://balsamiq.com/) 
- The project uses Balsamiq to create the wireframe mockups.

### MongoDB
- MongoDb is used as project database.

### HTML 5 
- Markup language designed to be displayed in a web browser.

### CSS 3
- Style sheet language used for describing the presentation of a document in HTML.

### Javascript
- JavaScript is a scripting language used to create and control dynamic website content.

## Testing

### Development Testing

-  I used the Google Chrome Developer tools during the development of the website to inspect the site at different device sizes and in responsive mode.

### Manual Testing

1. As user I want a clear understanding of the website funcionalities.
- The website is clear and easy to understand.

2. As a user I want to be able to view this site on my computer, mobile and tablet.
- The website works in any device.

3. As a user I want to be able to create and add a new hotel.
- After the log in the user are able to add their favourite hotels.

4. As a user I want to be able to edit an existing hotel.
- After the log in the user are able to edite or delete existing hotels.

- Social Media Links
1. When each link is clicked, it opens a new tab.
2. When each link is clicked, it takes the user to the correct page.

### Code Validation

The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors in the project.

- W3C HTML Validator

![Markup Index](static/images/htmlvalidator.png)


- W3C CSS Validator 

![Markup CSS](static/images/cssvalidator.png)

The CSS validator shows an error that comes from Materialize.


- Lighthouse

![Lighthouse](static/images/lighthouse.png)

I used the Lighthouse on Google Developer Tools to check the Perfomance, Accessibility, Best Practices and SEO of the website.

- Pep8 Validator

![Pep8](static/images/pep8.png)

Pep8 is a Python validator.

### Issues
- I had many issues deploying the project on Heroku, wich the tutors helped to fix.
- Due to the proximity of the deadline I had to leave behind some improvements on CSS code.  

## Deployment

### Deploying on Heroku

To get the project deployed the following steps were taken:

1. To prepare for deployement on Heroku, these steps were first taken:
    - Create the requirements file, via Gitpod CLI: `pip3 freeze --local > requirements.text`
    - Create the Procfile (capital P and no extension), via Gitpod CLI: `echo web: python app.py > Procfile` 

2. Using git, the new files are commited. (git commit)
3. Now a new app is created on Heroku:
    - Login (or first register an account) on Heroku
    - Within heroku a new app is created with name npc-library (at this moment there is a button in the top right corner called 'new')
4. After the app was created I went to settings (within the app dashboard) and copied the Heroku Git URL (https://git.heroku.com/star-milestonep3.git)
5. Back in Gitpod I logged into Heroku using on the CLI `heroku login` and entered credentials.
6. To add Heroku as a remote I entered in the CLI: `git remote add heroku https://git.heroku.com/star-milestonep3.git` (the URL copied in step 4.)
7. Now I pushed all content to Heroku using the CLI: `git push heroku main`
8. I started the Heroku process with `heroku ps:scale web=1` also from the gitpod CLI.
9. To get the connection string of the database, I logged into [MongoDB Atlas](https://account.mongodb.com/account/login). There I selected the cluster of the project and connected. Through the option 'connect your application' I got to the database connection string.
10. Within the heroku app dashboard I clicked the button 'reveal config vars' and entered the following values:
    1. IP: 0.0.0.0
    2. PORT: 5000
    3. MONGO_URI: Here is pasted the connection string gotten at 9 and edited the values 'password' and 'dbname' to match my own data.
    4. SECRET_KEY: Added this as defined in my env.py file
11. Lastly I went to the 'more' button and chose 'restart all dynos'
12. Now through the 'open app' button I started the app


The live link can be found here - http://star-milestonep3.herokuapp.com/hotels

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps.

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.
7. Press Enter. Your local clone will be created.

## Credits

### Code

- Bootstrap v 5.1.0: Bootstrap was used throughtout the project mainly the buttons, cards and carousel.
- FontAwesome: The icons in the footer were taken from Font Awesome.

### Media

- All images were sourced from [Unsplash](https://unsplash.com/) or [Pexels](https://www.pexels.com/).

### Acknowledgements

- Code Institute tutors Sean, Christine and Scott and fellow students for their support.




