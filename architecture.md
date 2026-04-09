Architecture 

## Overview
For this project, we built a simple Flask app that connects a database and an external API.
The main idea was to take data from both and combine it into one response. We kept everything quite simple since this was our first time doing something like this.

## How does it work?

When the app runs:

- It gets a joke category from the database
- It sends a request to an external joke API
- The API returns a joke
- The app sends the result back to the user

So basically, the database decides the type of joke, and the API gives us the actual joke.

## Main parts of the system

## Flask app

This is the main part of the project.

It:
- handles the routes (like /api/joke)
- connects to the database
- calls the external API
- returns the result

## Database

We used PostgreSQL (Supabase).

It just stores joke categories. We kept it simple because we didn’t need anything complicated.

## External API

We used a joke API to get the actual jokes.
The app sends a request and gets back a response in JSON format.
If the API doesn’t work, we return an error message instead.

## Configuration

We used environment variables to store things like the database URL.

This is better than putting them directly in the code.

We also included a .env.example file to show what is needed.

## Deployment

We used Docker to run the app.

This makes it easier to run the project on different machines.

We also used GitHub Actions to automatically check and build the project when we push code.

## Version control

We used GitHub to work together.

We:

created branches for features
used pull requests
reviewed each other’s code

This helped keep everything organised.

## What we kept simple

We didn’t try to overcomplicate the project.

We focused on:

making sure everything works
understanding how the pieces connect
meeting the assignment requirements

## Limitations

Some things are basic:

error handling could be better
not many tests
no advanced UI

## What we would improve

If we had more time, we would:
- add more tests
- improve error handling
- improve the UI
- add more features

## Conclusion

This project helped us understand how to connect a database and an API in a simple way.

Even though it’s basic, everything works together and meets the requirements.