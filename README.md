# Flask Blog Tutorial

This repository was cloned from a blog series by [Tech with Tim (TwT)](https://www.youtube.com/watch?v=GQcM8wdduLI&list=PLzMcBGfZo4-nK0Pyubp7yIG0RdXp6zklu) where he walks through how to implement a functional blog app using Python and Flask (see tutorial 5 for the final product, or watch the entire series for a great walkthrough).  Tim avoids using data models that require SQL syntax, and instead uses the SQLAlchemy ORM.  This allows developers to work with a data model even if they're unfamiliar with SQL...great for beginning programmers!  While this repository will keep SQLAlchemy, future commits will have more comlicated relationships and so this is more tailored to intermediate to advanced develoeprs.  

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
 
