![bird_watcher_logo](https://user-images.githubusercontent.com/64138643/93746838-adcdfb80-fbed-11ea-9360-2bd3607f4e2d.PNG)
### [Heroku App](https://bird-watcher-project.herokuapp.com/)
### [GitHub](https://github.com/CarterStefan/bird_watcher)
 
![Am_I_Responsive](https://user-images.githubusercontent.com/64138643/97895263-7776b680-1d2b-11eb-81b3-ab9b2b888ba9.PNG)

 
Bird watcher is my third milestone project as part of my Full Stack Web Development Course with [Code Institute](https://codeinstitute.net/). This project focuses on "Data Centric Development" and will put into practice what I have learned over the last couple of modules.
 
## Table of Contents
1. [**Project overview**](#project-overview)
2. [**UX**](#ux)
  - [**User Stories**](#user-stories)
  - [**Design**](#design)
    - [**Libraries**](#third-party-libraries)
    - [**Color Scheme**](#color-scheme)
    - [**Typography**](#typography)
  - [**Wireframes**](#wireframes)
3. [**Features**](#features)
  - [**Existing Features**](#existing-features)
  - [**Features Left to Implement**](#features-left-to-implemement)
4. [**Technologies Used**](#technologies-used)
5. [**Databases Used**](#databases-used)
6. [**Deployment**](#Deployment)
7. [**Testing**](#Testing)
8. [**Acknowledgments**](#Acknowledgments)
---
 
## Project overview
Bird Watcher was built using [Python](https://www.python.org/) - programming language, [Flask](https://flask.palletsprojects.com/en/1.1.x/) - a Python framework & [MongoDB Atlas](https://www.mongodb.com/) - a document-based database for the storage and retriving of data.
 
 
## UX
 
Bird Watcher is an online web application and birdwatching challenege. It is focused on UK users which have an interest in bird watching, both experienced and beginners. Using Bird Watcher, users will be able to:

- Register an account
- See a list of all birds on the database
- See more information about a particular bird (registered user only)
- Report an error on the site for admin to change (registered user only)
- Search for a bird by species (registered user only)
- Add a bird to the users list of seen birds (registered user only)
- See a list of all birds the user has seen (registered user only)
- See how many birds the user has seen (registered user only)
 
The website will be easy to use, and have a familiar feel on all pages throughout the site.
 
### User Stories

##### Bird Watcher UK - Experienced
- I enjoy going out to see all kinds of birds.
- As a user, I would like a place to be able to record the birds that I see when out. I have a notebook, but I want a one stop place which is easy to use. I should be able to find a bird and mark it as seen. I should then also be able to see a list of all the birds I have spotted in one page and be able to see when and where I saw the bird. I am very knowledgable about birds and would like to correct any issues I spot on a birds information using an error form on the website.
 
##### Bird Watcher UK - Beginner
- I enjoy going to see the birds at my local nature reserve.
- As a user, I would like a place to be able to record the birds that I seen in the hope of seeing all bird species in the UK one day.
- I would like to see a list of common birds and mark them off once I have seen them. As a beginner, I do not know a lot of information about each bird and do not know where to find them. I should be able to click on a bird to see more information about that particular species. This should apply to both birds that I have seen and not yet seen to achieve the goal of finding where to spot them.
 
##### Website Admin
- As admin of the site I want to be in control of any errors on the site. I will add functionality to the site so that a user can report an error of information about a bird. I will then be able to look at an errors page and correct any legitimate issues myself. I also want the functionality to add new birds to the database to extend the challenge to spot all the birds if I wish.

### Design

The site is simple in design to make it easy on the eye and user friendly. The website is fully responsive between smaller and larger screen sizes.

#### Third party Libraries
 - [Materialize](https://materializecss.com/) - A modern responsive front-end framework based on Material Design. Used for the layout of the site, responsiveness to screen suzes and various features around the site (forms, buttons, search selctions etc)
 - [jQuery](https://jquery.com/) - jQuery is a fast, small, and feature-rich JavaScript library. Used for some interactive elements with the materiliase features.

#### Color Scheme 
- [Adobe Color](https://color.adobe.com/) - Used for selecting a color theme to suit my website.
![Color Theme](https://user-images.githubusercontent.com/64138643/97888179-c10ed380-1d22-11eb-91a0-8e6f26a8d866.PNG)

#### Typography
[Google Fonts](https://fonts.google.com/) - Used for the selection of my fonts.
- [Plaster](https://fonts.google.com/specimen/Plaster) - Logo of website
- [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed) - Used for majority of text around the website
- [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab) - Used for name of birds on bird cards

### Wireframes
You can view the wireframes that I based my site on in the UX folder.
- [View Wireframe](https://github.com/CarterStefan/bird_watcher/blob/master/static/UX/WireframePDF.pdf)

## Features 
### Existing Features
- Login - The login page is the first page a user will come to when visiting the site. It has two fields for the user input a username and a password field. Then there is a button for the user to submit the form to login, or if they are not a registered user to the site, they can use the link underneath to go to the register page. Underneath the form there is some information about the site for new users.

- Register - The register page is in the same layout as the login page. The only differences being that a user will create an account instead of logging in to their exisitng account. Also, the link underneath the login button directs to the login page instead of the register page. The information below is the same, and informs people about the site and its features. 

- My Sightings - The first page a user will be taken to once logging in / registering will be the my sightings page. This page shows a list of all the birds which that particular user has reported as being spotted. A message will display at the top to keep users updated how many of the birds they have spotted and how many there are to go. If the user has seen no birds a message will display encouraging the user to get out and get spotting. If a user has reported sightings, they will appear as 'cards' on this page with information where the user spotted the bird and on what date. The user can then click on the bird to see more information about it, or remove the sighitng if it was made by mistake.

- All Birds - This page will show the user the full list of birds which are on the database. This is the 159 most popular birds in the UK (at the time of creating the site) which are displayed in alphabetical order. On this page a user can browse through all the birds along with an image of them and have the option to click into the bird to find more information about the bird. As there is a lot of birds on here, the user has the option to filter by birds type (species) to reduce the number of birds that is displayed. You can clear the search to bring back the full list.

- Report Sighting - The report sighting page is where a user inputs the details of the sighting once he has seen a bird. There are three parts to the form. The user must first specify the name of the bird he has seen. This is done through a selection field which lists all the birds on the database preventing a user incorrectly spelling a bird. The second part is for the user to specify the date they saw the bird. This is done through a date selector, again to avoid incorrect user input. The final part of the form is the location field. This has a list of all the counties in the UK so the user can sleect the location they spotted the bird from the dropdown. This will be stored in the database as a sighting where the information will be displayed on the users 'my sightings' page. If the user has already marked this bird as seen, a flash message will display informing the user.

- View Bird - Here is where a user can view more detailed information about a specific bird. The top of the page will display an illustration of the bird, with information underneath of the birds name, scientific name, size, description, feeding habit and where the bird is located. Underneath the user has multiple options available to them to navigate around the site. If they have read some information on the bird they have the option to edit the bird directly themselves, or they can log an error report to admin.

- Log Error - The user can submit an error report if they have seen misinformation on a bird, or if they are unhappy with something on the birds page. There are two parts to the form. The first is the name of the bird they are unhappy with, or they can submit a general error not relating to a bird. The second part is a free text box which the user can put a description of the problem they are facing. 

- Home - This page also shows a count at the top showing the user how far through the challenge they are. It features a hero image at the top and three options underneath to navigate around the site. They can direct to the report sighting page, my sightings page or view all uk birds page.

- Delete Account - In the footer the user has the option to delete their account if they are unhappy with site and no longer wish to use it.

- Add New Bird (Admin Only) - If the user is logged in as admin, they can add a new bird. This form is a duplicate of the form seen on the Edit Bird page. This is so the admin can extend the challenge if they wish by adding more birds to be spotted. By adding a new bird here, the changes will be reflected in the birds seen count on my homepage and my sightings page, also the new birds will be showing straight away on the view all birds page.

- Edit Bird (Admin only) - If the user is logged in as admin, they can edit a birds information. The admin will click through to this page only from the view bird page. In doing so, the birds information is prepopulated on the form. The admin can then find the field they want to change and edit the text. There is a submit button at the bottom of the form which will amend the information on that bird on the database.

- Errors page (Admin Only) - If the user is logged in as admin, the errors page will show a list of all the errors which have been reported by users. These will be displayed in the form of cards similar to the view birds / my sightings page, to be consistent with the rest of the site. The admin will be able to see the username of the user which submitted the error, the bird the error relates to and the error message. Once the admin has actioned the error and made the required changes, there is the option to mark the error as resolved, which will remove the erorr from the list.

### Features Left to Implement
- Automatic location detection - I would like to add in a feature where the report sighting form could automatically detect where the user is and prepopulate the location field in the form based on this.

## Technologies Used
1. [HTML 5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- HTML is the standard markup language for Web pages.

2. [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.

3. [JQUERY](https://jquery.com/)
- jQuery is a fast, small, and feature-rich JavaScript library

4. [MATERIALIZE](https://materializecss.com/)
- A modern responsive front-end framework based on Material Design

5. [PYTHON](https://www.python.org/)
- Python is a programming language that lets you work quickly and integrate systems more effectively.

6. [FLASK](https://flask.palletsprojects.com/en/1.1.x/)
- Flask is a lightweight WSGI web application framework

7. [FLASK PYMONGO](https://flask-pymongo.readthedocs.io/en/latest/)
- MongoDB support for Flask applications

8. [WERKZEUG SECURITY](https://werkzeug.palletsprojects.com/en/1.0.x/)
- Werkzeug is a comprehensive WSGI web application library

9. [BSON](https://www.mongodb.com/json-and-bson)
- BSON is the binary encoding of JSON-like documents that MongoDB uses when storing documents in collections

10. [JINJA](https://jinja.palletsprojects.com/en/2.11.x/)
- Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates

11. [MONGODB](https://www.mongodb.com/)
MongoDB is a general purpose, document-based, distributed database built for modern application developers and for the cloud era

12. [PYMONGO](https://pymongo.readthedocs.io/en/stable/index.html)
- PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python

13. [GITPOD](https://www.gitpod.io/)
- Gitpod streamlines developer workflows by providing prebuilt, collaborative development environments in your browser - powered by VS Code

14. [GITHUB](https://github.com/)
- Hosting for software development and version control using Git

15. [HEROKU](https://www.heroku.com/home)
- Heroku is a cloud platform as a service supporting several programming languages

## Databases Used

### MongoDB
MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. I created the following collections for my project:

- bird_family : This was used to created a list of bird species and an icon to represent each species.

- bird_sightings : This was used to keep a record of all members sightings which can be retrived by using the corresponding username to display the sightiings on the users my sightings page.

- bird_species : This contains a list of 159 bird and some corresponding information for each one to display on the UK birds page.

- counties : This contains a list of all counties in the UK. This is used when a user is reporting a sighting and can choose where they spotted the bird.

- errors : When a user logs an error against a bird, or a general error they are then displayed on the errors page when logged in as admin after being read from this collection.

- users : When a user registered on the site, there username and password are stored on this collection. 

## Deployment

I used GitPod for the devlopment of my project and Heroku has been used for the hosting of the app. All com,its were pushed to Heroku from within GitPod.

To get my application to a standard which was ready for deployment I followed along with the Code Institues tutorials for setting up a project. This included:

- Removing any hardcoded environment variables from the app.py file so that any users were unable to see the database name, secret key and URI. These were then put in an env.py file and the values placed in the Heroku Config Vars.

- A requirements.txt file was created which contains a list of the specified packages needed to run the project and their versions.

- A Procfile was set up with the contents "web: python app.py". This indicates to Heroku that it must runt this as a web application and to run the file app.py.

- In my Heroku project I set up numerous Config Vars to contain the secret information that I wanted kept from the app. This included IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY, KEY.

- Once I was happy with my project, I set the flask debugging to 'False'.

- I then pushed the final code to Heroku using GitPod. 

## Testing

One of the requirements for the submission of the project is extensive testing to ensure the site works correctly with no bugs. I used a mix of online validators and manual testing to ensure my code would pass.

### HTML
- [W3CValidator](https://validator.w3.org/) I ran all my HTTML files through the validator, the only errors I received were relating to the Jinja syntax.

### CSS
- [W3CValidator CSS](http://jigsaw.w3.org/css-validator/) I recieved no errors with my CSS file.

### Javascript
- [JShint](https://jshint.com/) - No errors.

### Python
- [Pep8](http://pep8online.com/) - My code is Pep8 complient. I had confirmation of this through the message 'All Right' when running my code through the check.

### Manual Testing
To ensure my website was in good working order I tested all links on the pages across a range of devices using the chrome developer tools and Chrome, Edge and Firefox to ensure it works okay on different browsers. I have documented this [here](static/manual_testing/testing.md)

## Acknowledgments

### Media
- The images of birds on the site are taken from the [RSPB](https://www.rspb.org.uk/birds-and-wildlife/wildlife-guides/bird-a-z/) website. I then added the sketch effect to them and saved them locally.

- The silhouette images used for the bird families were taken from The Cornell Lab website [All About Birds](https://www.allaboutbirds.org/)

### Content
The information displayed on the birds indivudual pages was taken from a combination of:
- [RSPB](https://www.rspb.org.uk/birds-and-wildlife/wildlife-guides/bird-a-z/)
- [BirdSpot](https://www.birdspot.co.uk/)
- [Collins](https://collins.co.uk/collections/collins-gem) - Book on UK bird species

I would like to thank my mentor Gbenga for his help and guidance throughout this project and the Code Institute for teaching me skills required to do so.

The inspiration for this project was from my own passion of a good walk in the countryside.


