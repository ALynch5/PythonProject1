Architecture 

## Overview
For this project, we built a simple Flask app that connects a database and an external API.
The main idea was to take data from both and combine it into one response. We kept everything quite simple since this was our first time working with tools like Flask, APIs, and Docker.

## How does it work?

When the app runs:

- It gets a joke category from the database
- It sends a request to an external joke API
- The API returns a joke
- The app sends the result back to the user

So basically, the database decides the type of joke, and the API gives us the actual joke.

## Architecture Flow

Our system follows a simple flow:

The system follows a simple flow:

1. A user sends a request to the Flask app  
2. The Flask app queries the PostgreSQL database for a category  
3. The app sends a request to the external Joke API  
4. The API returns a joke  
5. Flask combines the data and sends a response back  

This shows how the application connects both internal (the database) and external (API) services.

## Main parts of the system

## Flask app
This is the main part of our project.

It:
- handles the routes (like /api/joke)
- connects to the database
- calls the external API
- returns the result

## Database

We used PostgreSQL (Supabase).

It stores joke categories. We kept it simple because we didn’t need anything complicated.

## External API

We used a joke API to get the actual jokes.
The app sends a request and gets back a response in JSON format.
If the API doesn’t work, we return an error message instead.

## Integration Points
The application connects two main services:

- PostgreSQL (Supabase) -> stores joke categories  
- External Joke API -> provides the jokes  

The Flask app then sits in the middle and connects both of these together.


## Configuration

We used environment variables to store things like the database URL.

This is better than putting them directly in the code.

We also included a .env.example file to show what is needed.

## Deployment

We used Docker to run the app.

This makes it easier to run the project on different machines.

We also used GitHub Actions to automatically check and build the project when we push code.

## CI/CD Pipeline

Our CI pipeline runs automatically on every push and pull request.

It:
- installs dependencies  
- runs linting (flake8)  
- runs tests (pytest)  
- builds the Docker image  

This helps make sure the code works correctly before being merged.

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