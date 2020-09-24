# The Pantry
This is our repo for The Pantry, an app that allows farms with an excess of crops to connect with local food banks in need. 


## Our Mission
Did you know that roughly 125 - 160 BILLION pounds of food goes to waste ever single year? Did you also know that roughly 41 million Americans are going hungry in that same time frame? Why, when there is perfectly good food being tossed, are others starving? What if we could change that? Enter, The Pantry. The Pantry creates a platform for farmers to post what food will go to waste from current crops, over production or back-out buyers and allows Food banks to reach out and pick up the food that people so desperately need. This platform is built for Farmers and Food banks to interact directly, cutting out any middle man delays. With The Pantry, we hope to connect Farmers with those in need and create a dent in the amount of sufferers who don’t have the same access to fresh, healthy food. Anyone can make a choice to save the world. We hope to have done our part to take a step in that direction. 


## User Stories

- As a Farm User, I want to be able to create an account.
- As a Farm User, I want to be able to post the food I have available for donation.
- As a Farm User, I want to be able to delete a post if the food has already been claimed.
- As a Food Bank User, I *don't* want to have to create an account to view available food.
- As a Food Bank User, I want to be able to search for food by category.
- As a Food Bank User, I want to be able to communicate directly with the source, rather than through a middle man.

## Tech Used

- Django/ Python
- DjangoAuth
- PostgreSQL
- Celery
- DotEnv
- gitignore

# PiP3 Installs
- pip3 install boto boto3 botocore django-celery-beat celery python-dotenv
- pip3 install 'celery[sqs]'
- pip3 install celery==5.0.0
This is to set proper celery version, will not work other wise



## The Planning

When we were given the topi of "Saving the world", we were surprised to find we had A LOT of ideas on how to go about this. The hardest part? Where do we start? How do we decide which issue to address? And how can we fix the issue we decide on? After narrowing down our list, we realized that poverty and hunger and a raging issue in this country (and world wide). By creating a platform that hits the root of this issue, while solving the issue of wasted crops, we hope to save two birds with one app, if you will. 

- The Wireframe : <insert wireframe here>
- The User: Who will be using our app? Who will be accessing it as a Guest? How can we make sure that, with or without an account, our User's and Guest's alike are getting the same benefits? This gave us the idea that the only User's that required *accounts* would be the ones with the produce, aka the Farmers. Our Food Bank User is technically a Guest on the site. No need to create an account because Food Banks won't be creating posts, they will be searching through posts, looking for the Location and produce that fits their needs.
- The Design: We wanted our site to feel welcoming and show off the kind of product Guest's will be looking to pick up. We also wanted it to be extremely user friendly, eliminating having a lot of extra tabs for user's to keep up with. By keeping the amount of pages stripped down, it simplifies the process and focuses the attention on what's important: finding foo for those in need!


### Division of responsibilities

- Rather than completely dividing up work and working alone, we decided to pair program our way through the whole project. We each took turns as the driver( writing the code), while the other two members of the team acted as navigators( googling, debugging and giving insight into what should be written). With 3 different members, all having a different point of view and skill set, we believe we were able to show off the best of our abilities and really work together as a team from start to finish.


## The Dev Team

- The Magnificent Margaret [github](https://github.com/margaret-jihua)
- The Superb Sameh [github](https://github.com/kinawy)
- The Lyrical Lizz [github](https://github.com/LizzWest)
- The Task Master [github](https://github.com/anthonygregis)
### Huge shoutout to Anthony and Pete, Anthony slogged through 3 different scheduling functions with me, and ultimately found the right syntax for Celery. Pete was able to help us figure out a custom search function, hope to fully implement it in the future



## Stretch goals

- We want to implement the actual functionality of the search by category.(currently queries the db, but we aren't pulling the actual data for times sake)
- We would like to add in the ability for retailers ( restaurants and stores) to also be able to post potentially wasted food for food banks to pick up.
