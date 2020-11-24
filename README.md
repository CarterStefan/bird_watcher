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
---
 
## Project overview
Bird Watcher was built using [Python](https://www.python.org/) - programming language, [Flask](https://flask.palletsprojects.com/en/1.1.x/) - a Python framework & [MongoDB Atlas](https://www.mongodb.com/) - a document-based database for the storage and retriving of data.
 
 
## UX
 
Bird Watcher is an online web application and birdwatching challenege. It is focused on users which have an interest in bird watching, both experienced and beginners. Using Bird Watcher, users will be able to:

- Register an account
- See a list of all birds on the database
- See more information about a particular bird (registered user only)
- Report an error to the site for admin to change (registered user only
- Search for a bird by species (registered user only)
- Add a bird to the users list of seen birds (registered user only)
- See a list of all birds the user has seen (registered user only)
- See how many birds the user has seen (registered user only)
 
The website will be easy to use, and have a familiar feel on all pages throughout the site.
 
### User Stories

##### Bird Watcher - Experienced
- I enjoy going out to see all kinds of birds.
- As a user, I would like a place to be able to record the birds that I see when out. I have a notebook, but I want a one stop place which is easy to use. I should be able to find a bird and mark it as seen. I should then also be able to see a list of all the birds I have spotted in one page and be able to see when and where I saw the bird. I am very knowledgable about birds and would like to correct any issues I spot on a birds information.
 
##### Bird Watcher - Beginner
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
