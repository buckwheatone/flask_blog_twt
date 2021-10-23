# Flask Blog Tutorial

This repository was cloned from a blog series by [Tech with Tim (TwT)](https://www.youtube.com/watch?v=GQcM8wdduLI&list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu) where he walks through how to implement a functional blog app using Python and Flask (see tutorial 5 for the final product, or watch the entire series for a great walkthrough).  Tim avoids using data models that require SQL syntax, and instead uses the SQLAlchemy ORM.  This allows developers to work with a data model even if they're unfamiliar with SQL...great for beginning programmers!  While this repository will keep SQLAlchemy, future commits will have more comlicated relationships and so this is more tailored to intermediate to advanced developers.  

# Enhancements

Tech with Tim's vlog is great.  Anyone looking to grow their programming knowledge should stop by his channel and find something you like, because there's a lot to like.  My goal is to take these beginnger projects and add features and UX improvements that you might see out in the world.  In other words, this we're starting with MVP1 and I'd like to take it to MVP2.

My choices to enhance the tutorial include: 
- including a landing page with a call to action for registration
- leveraging more features of Bootstrap to improve the UX including better responsive design
- adding more security by leveraging WTForms for validation, including CSRF tokens
- adding functionality to allow easy deployment to your choice of server

# Small Things
- Add "logged in as" to home screen 
- Make username case insensitive 
- Ensure that success/error messages don't persist 
- Change like, delete from fontawesome to Material Icons

# Full List 
### UX, No New Data
- [x]  Fix issue in 'delete post' in views to account for post.author, not post.id
- [x]  add material icons for like/delete to post
- [x]  add material icons for delete to comments
- [x]  UX — spacing and icons for like/delete on posts and comments
- [x]  UX — add modal to confirm deletion of post (use JS to allow multiple deletes on one page)
- [x]  UX — font change from standard to something nicer (added Roboto)
- [x]  UX — time formatting
- [x]  UX — show / hide 1 comment and more than one comment
- [x]  Add create post link in navbar
- [x]  ability to paginate and show posts in reverse chron order
- [x]  UX — hover descriptions for what you'll see (user name on post or comment, like, delete)
    - [ ]  Fix like/unlike hover message so it doesn't require reload to show
- [ ]  UX — navbar look and feel (brand logo, sign-in and sign-up buttons on right, profile dashboard)
- [ ]  Turn alerts into toasts
- [ ]  preview a post before submitting
- [ ]  ability to edit a post after it's posted
- [ ]  shorten long posts with a "show more..."

### UX, New Data or Logic
- [x]  UX — add pic to profile
- [x]  UX — add favicon
- [x]  UX — add a landing page
    1. Go to free illustrations com, pick out a nice image for the landing page, copy the free version and store it into your static directory
    2. Create a new template called landing.html and extend your base template 
    3. Add fun messaging 
- [x]  Add user account page for email change, password change, delete account, profile pic update
- [ ]  Add title to post-creation page and posts themselves, line should say "[Title] by [Author]"

### Backend

- [x]  Backend — username case insensitive
- [x]  Backend — add functionality to change email and password
- [x]  Backend — email form validation and CSRF
- [ ]  Backend — add 'forgot password functionality' —> new page w/email request and recaptcha —> sorry that e-mail is not registered, try again or *sign-up.*
- [ ]  Add unit tests

### Maybe
- Backend — time zone compatibility???
- Backend — clear session if server resets or after some time
- Backend — sign-in with social (Google, Twitter, Facebook, Apple)
- Backend — search posts


Background images on landing courtesy of [SVG Backgrounds](https:www.svgbackgrounds.com)