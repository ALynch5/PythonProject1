# DeployHub Project - Joke API

## Team
- Alex Lynch - 124340181
- Colin Molloy - 
- Robert Barrett - 124385211

## What this project is
This is a small web app we built using Flask for our DevOps assignment.

The goal was to connect two things:

- a database (PostgreSQL)
- an external API
and combine them into one simple API.

We kept it simple because this is our first time doing something like this.

## What does the app do

Our app:
1. Gets a joke category from the database
2. Sends a request to an external Joke API
3. Returns a joke based on that category

So basically the database decides the type of joke, and the API gives us the actual joke.

## Endpoints
Endpoint	What it does
/	            Shows a joke in the browser
/api/joke	    Returns a joke as JSON
/health	        Checks if the app is running
/status	        Shows if database + API are working

## How we built it

We used:
- Flask for the backend
- PostgreSQL (Supabase) for storing data
- JokeAPI for external data
- Docker to run the app
- GitHub for version control

## What did we learn?
- How to connect an API to a database
- How to use environment variables properly
- How Docker works (at a basic level)
- How to work in a team using GitHub

## What we would improve in the future?
- Add more tests
- Improve error handling
- Make the UI nicer
- Add better logging

## Notes
This was our first time working with APIs, Docker, and CI/CD, so we focused on keeping everything simple and working correctly rather than making it complex.