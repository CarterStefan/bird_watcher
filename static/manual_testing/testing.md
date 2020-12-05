## Manual Testing

### NavBar:

My NavBar has three states. I tested all three states to make sure they displayed correctly and all the links worked as they should:

When a user first visits the page in a logged out state, they see:

- Home 
- UK Birds
- Login
- Register

When logged out, all routes are working correctly:

Click BIRDWATCHER logo - You are taken to the login page (route to /login)
Click home - You are taken to the login page (route to /login)
Click UK BIRDS - You are taken to the UK Birds page (route to /uk_birds)
Click Login - You are taken to the login page (route to /login)
Click Register - You are taken to the login page (route to /register)

When a user logs in, they see:

- Home 
- UK Birds
- Sightings
	- My Sightings
	- Report Sighting
- Logout

Click BIRDWATCHER logo - You are taken to the home page (route to /home)
Click Home - You are taken to the home page (route to /home)
Click UK BIRDS - You are taken to the UK Birds page (route to /uk_birds)
Click My Sightings - You are taken to the login page (route to /my_sightings)
Click Report Sightings - You are taken to the report sighting page (route to /report_sighting)
Click Logout - You are taken to the login page (route to /login)

When a user logs in with the username Admin, they see:

- Errors
- Add New Bird
- Home
- UK Birds
- Sightings
	- My Sightings
	- Report Sighting
- Logout

Click BIRDWATCHER logo - You are taken to the home page (route to /home)
Click Errors - You are taken to the errors page (route to /admin_errors)
Click Add New Bird - You are taken to the add new bird page (route to /add_new_bird)
Click Home - You are taken to the home page (route to /home)
Click UK BIRDS - You are taken to the UK Birds page (route to /uk_birds)
Click My Sightings - You are taken to the login page (route to /my_sightings)
Click Report Sightings - You are taken to the report sighting page (route to /report_sighting)
Click Logout - You are taken to the login page (route to /login)

### Footer

Similar to the NavBar, the footer has 2 states, depending on how the user is visiting the page. I tested both states to make sure they displayed correctly and all the links worked as they should:

When a user first visits the page in a logged out state, they see:

- UK Birds
- Login
- Register

Click UK BIRDS - You are taken to the UK Birds page (route to /uk_birds)
Click Login - You are taken to the login page (route to /login)
Click Register - You are taken to the login page (route to /register)

When a user logs in with any username, they see:

- UK Birds
- My Sightings
- Report Sighting
- Logout
- Report Error
- Delete Account

Click UK BIRDS - You are taken to the UK Birds page (route to /uk_birds)
Click My Sightings - You are taken to the login page (route to /my_sightings)
Click Report Sightings - You are taken to the report sighting page (route to /report_sighting)
Click Logout - You are taken to the login page (route to /login)
Click Report Error - You are taken to the report error page (route to /report_error)
Click Delete Account - You are taken to the delete account page (route to /delete_account)

### Login Page

- Login form is displayed

- Type a username which is less then 5 characters and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' message turn red

- Type a username which contains symbols and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' message turn red

- Type a username which is between 5 - 15 charcaters and contains no symbols and click off the field - Field turns green and message reads 'This Works'

- Type a password which is less then 5 characters and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red

- Type a Password which contains symbols and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red

- Type a username which contains symbols and click login - Message appears to say 'Please match the requested format'

- Type a password which contains symbols and click login - Message appears to say 'Please match the requested format'

- Type a Password which is between 5 - 15 charcaters and contains no symbols and click off the field - Field turns green and message reads 'This Works'

- Click Login with one or both fields missing - Message appears to say 'Please fill in this field'

- Login with an invalid username - Flash message appears 'Incorrect Username or Password'

- Login with an invalid password - Flash message appears 'Incorrect Username or Password'

- Login with a correct username and password - You are taken to the My Sightings page in a logged in state

- Click the 'Register Here' link under form - You are taken to the register page

- Click the 'Register Here' link in the 'What is birdwatcher' box - You are taken to the register page

- Click the 'UK Birds' link in the UK Birds box - You are taken to the UK Birds page


### Register Page

- Register form is displayed

- Type a username which is less then 5 characters and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' message turn red

- Type a username which contains symbols and click off the field - Field and 'Username must be between 5-15 characters using only letters and numbers' message turn red

- Type a username which is between 5 - 15 charcaters and contains no symbols and click off the field - Field turns green and message reads 'This Works'

- Type a password which is less then 5 characters and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red

- Type a Password which contains symbols and click off the field - Field and 'Password must be between 5-15 characters using only letters and numbers' message turn red

- Type a username which contains symbols and click register - Message appears to say 'Please match the requested format'

- Type a password which contains symbols and click register - Message appears to say 'Please match the requested format'

- Type a Password which is between 5 - 15 charcaters and contains no symbols and click off the field - Field turns green and message reads 'This Works'

- Click register with one or both fields missing - Message appears to say 'Please fill in this field'

- Register with a username which has already been registered - Flash message appears 'Username taken, please choose another or login'

- Register with a correct username and password - You are taken to the My Sightings page in a logged in state.

- Click the 'Login Here' link under form - You are taken to the login page

- Click the 'Login Here' link in the 'What is birdwatcher' box - You are taken to the register page

- Click the 'UK Birds' link in the UK Birds box - You are taken to the UK Birds page

### Homepage

- Number in the hero image displays the correct number of birds which have been spotted

- Click the 'Add to sightings' button - You are taken to the Report Sighting Page

- Click the 'My Sightings' button - You are taken to the My Sightings page

- Click the 'View All Birds' button - You are taken to the UK Birds page

### UK Birds Page

- All birds are displayed in alphabetical order

- Clicking the filter by bird type dropdown displays the bird species in alphabetical order

- Choose 'Birds of Prey' and click submit - Only birds with a bird species of 'Bird Of Prey' are displayed

- Choose 'Diver' and click submit - Only birds with a bird species of 'Divers' are displayed

- Click clear - Filter is removed and all birds are shown in alphabetical order

- Click back to top from the bottom of the list - Takes you to the top of the page

- Click 'View (bird name) - Takes you to the bird page for that particular bird

- Click the 'Add to sightings' button - You are taken to the Report Sighting Page

- Click the 'My Sightings' button - You are taken to the My Sightings page

### View Bird

- If the bird you are viewing has been spotted by the user - Flash message 'You have seen this bird'

- Bird Image is displayed at the top of the page

- Option to edit bird is displayed if logged in as admin

- Click the edit bird button - You are taken to the edit bird page with all information pre filled for the correct bird

- Bird Name shows correct bird name as entered in the database

- Scientific Name shows correct scientific name as entered in the database

- Length shows correct length as entered in the database

- Wingspan shows correct wingspan as entered in the database

- Weight shows correct weight as entered in the database

- Description shows correct description as entered in the database

- Feeding shows correct feeding as entered in the database

- Where shows correct where as entered in the database

- Click the 'Log Error Report' - You are taken to the Report Error page

- Click the 'View All Birds' button - You are taken to the UK Birds page

- Click the 'Add To Sightings' button - You are taken to the Report Sighting page

### Edit Bird - Admin only

- When the page loads the entire form is pre-populated with the correct information for the bird you clicked through from

- Try to submit form with Name of Bird field missing - Message appears 'Please fill in this field'

- Try to submit form with Scientific Name field missing - Message appears 'Please fill in this field'

- Try to submit form with Length field missing - Message appears 'Please fill in this field'

- Try to submit form with Wingspan field missing - Message appears 'Please fill in this field'

- Try to submit form with Weight field missing - Message appears 'Please fill in this field'

- Try to submit form with Bird Family option missing - Message appears 'Please select an item in this list'

- Try to submit form with Description field missing - Message appears 'Please fill in this field'

- Try to submit form with Image field missing - Message appears 'Please fill in this field'

- Try to submit form with Feeding habit of bird field missing - Message appears 'Please fill in this field'

- Try to submit form with Where to see this bird field missing - Message appears 'Please fill in this field'

- Try to submit form with Name of Bird field containing numbers or symbols - Message appears 'Please match the requested format' with a explanation of the format required

- Try to submit form with Name of Bird field containing numbers or symbols - Message appears 'Please match the requested format' with a explanation of the format required

- Try to submit the form with the length field containing letters, symbols (Except -) and spaces - Message appears saying 'please match the requested format' with a explanation of the format required

- Try to submit the form with the wingspan field containing letters, symbols (Except -) and spaces - Message appears saying 'please match the requested format' with a explanation of the format required

- Submit form with all fields with valid information with 'Add to sightings' toggle off - page is reloaded with new information and flash message to confirm successful edit of bird

- Click 'Cancel Edit' button - You are taken to the View Bird page of the bird you are / have edited


### My Sightings

- Correct username is displayed in the top message

- Correct number of birds spotted is displayed in the top message

- If the number of birds spotted is equal to 0 - Message shows saying 'Get out there and get spotting'

- Birds spoted are displayed in alphabetical order

- The birds image is displayed in the card

- The birds name is displayed in the card

- The date seen is displayed in the card

- The location is displayed in the card

- Clicking 'View (bird name) - Takes you to the bird page for that particular bird

- Clicking 'Remove Sighting' - Removes the bird sighting from your list

- Click the 'Add to sightings' button - You are taken to the Report Sighting Page

- Click the 'view all birds' button - You are taken to the UK Birds page and flash message appears to confirm

### Report Sighting

- Report Sighting form is displayed

- Trying to submit the form with the Name of Bird field missing - Message appears 'Please select an item in this list'

- Trying to submit the form with the Date Spotted field missing - Message appears 'Please fill in this field'

- Trying to submit the form with the County field missing - Message appears 'Please select an item in this list'

- Clicking the Name of Bird option - Dropdown appears with the list of all birds in alphabetical order

- Clicking the Date Spotted option - Calendar popout appears and you are able to select your date

- Clicking the County option - Dropdown appears with the list of Counties in alphabetical order

- Clicking the 'Add to my sightings' with all fields filled out, the bird is added to the sightings database with the correct information

- Clicking the 'Add to my sightings' with all fields filled out, you are taken to the 'My Sightings' page where the new sighting is displayed and the number of birds seen increased by one.

### Add New bird - Admin Only

- Try to submit form with Name of Bird field missing - Message appears 'Please fill in this field'

- Try to submit form with Scientific Name field missing - Message appears 'Please fill in this field'

- Try to submit form with Length field missing - Message appears 'Please fill in this field'

- Try to submit form with Wingspan field missing - Message appears 'Please fill in this field'

- Try to submit form with Weight field missing - Message appears 'Please fill in this field'

- Try to submit form with Bird Family option missing - Message appears 'Please select an item in this list'

- Try to submit form with Description field missing - Message appears 'Please fill in this field'

- Try to submit form with Image field missing - Message appears 'Please fill in this field'

- Try to submit form with Feeding habit of bird field missing - Message appears 'Please fill in this field'

- Try to submit form with Where to see this bird field missing - Message appears 'Please fill in this field'

- Try to submit form with Name of Bird field containing numbers or symbols - Message appears 'Please match the requested format' with a explanation of the format required

- Try to submit form with Name of Bird field containing numbers or symbols - Message appears 'Please match the requested format' with a explanation of the format required

- Try to submit the form with the length field containing letters, symbols (Except -) and spaces - Message appears saying 'please match the requested format' with a explanation of the format required

- Try to submit the form with the wingspan field containing letters, symbols (Except -) and spaces - Message appears saying 'please match the requested format' with a explanation of the format required

- Submit form with all fields with valid information with 'Add to sightings' toggle off - Goes to UK Birds page with new bird showing

- Submit form with all fields with valid information with 'Add to sightings' toggle on - Goes to Report Sighting page

### Errors Page

- Page displays a list of all errors which have been reported and stored on the 'Errors' database

- Card displays 'Error With:' and the correct bird the error has been logged against or general error

- Card displays 'Reported By:' and the correct username of the user that logged the errror

- Card displays 'Description:' and the correct error message that the user submitted when logging the error

- Click 'Error Resolved' - The Error is removed from the database and is no longer displayed on the page. Flash message 'Error Resolved' to confirm the deletion

### Report Error

- Page displays Error Form with two fields - Name of Bird and Description

- Try to submit the form with Name of Bird field missing - Message appears 'Please select an item in this list'

- Try to submit the form with the Description field missing - Message appears 'Please fill in this field'

- Submit form with all fields with valid information - You are taken to the UK Birds page, Flash message to confirm the error has been reported, Error is logged to the database and shows in errors page

### Delete Account

- Page displays with options to delete account or to stay on the site

- Click 'Keep Watching' - You are taken to the My Sightings page

- Click 'Fledge Nest' - You are taken to the Register page and account information is deleted from the database

- Try to log in with the details of the account that has been deleted - Incorrect username or password message is displayed

### Page Not Found

- Go to page with invalid route - Page displays to let the user know page is invalid with option to go home

- Click 'Take Me Home' - You are taken to the homepage if logged in

- Click 'Take Me Home - You are taken to the login page if logged out

## Devices

I have tested my page on the following devises.

- Huwawei P30 Pro - Physical Device

- iPhone X - Google Chrome Dev tools

- iPhone 6/7/8 - Google Chrome Dev tools

- iPhone 6/7/8 plus - Google Chrome Dev tools

- iPphone 5/se - Google Chrome Dev tools

- iPpad - Google Chrome Dev tools

- iPad Pro - Google Chrome Dev tools