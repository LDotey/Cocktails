State & City Management CLI

State Planner CLI

A simple command-line interface (CLI) application for managing states and cities. Users can view, add, delete, and update states, as well as manage the cities within each state. This application is designed to help keep track of states and their cities, including key attributes like population and region.

Table of Contents
- Features
- Getting Started
- Usage
- Functions
    - State Functions
    - City Functions
- Database

Features

State Management:
- View all states (name, population, region)
- Add a new state
- Delete a state
- Update details of an existing state
- View cities associated with a state

City Management:
- View all cities of a state
- Add a new city to a state
- Update details of a city
- Delete a city

Getting Started:

Follow these instructions to get a copy of the project up and running on your local machine.

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/state-planner.git
    ```

2. Navigate to the project directory:
    ```sh
    cd state-planner
    ```

3. Install dependencies:
    ```sh
    npm install
    ```

4. Run the project:
    ```sh
    npm start
    ```

You should now see the project running locally on your machine.

Usage:

State:
    - A user is first presented with a main menu for State options 
        - View all states:
            - Allows a user to see all of the current States in the database
        - Add a State:
            - Allows a user to add a State to the database
                - User can update the name, population, and region
                - Once finished, user recieves a message validating the response given by the user
        Delete a State:
            - Allows a user to delete a state by selecting a state from the list of states
        Update a State:
            - Allows a user to update the population 
        Select State to View Cities:
            - Allows a user to view the cities for the selected state
                - User selects this option and they are presented with the list of cities 
                - User selects the city by entering the number of the city
                - User is then presented with city options
City:
    - After use selects city, they are presented with a city menu for City options
        - Add a State:
            - Allows a user to add a State to the database
                - User can update the name and population
                - Once finished, user recieves a message validating the response given by the user
        Delete a State:
            - Allows a user to delete a city by selecting the city from the list of states
        Update a State:
            - Allows a user to update the population

Functions

State Functions:

Detailed descriptions of functions related to state management.
- `viewStates()`: Fetches and displays all states from the database.
- `addState(name, population, region)`: Adds a new state with the specified name, population, and region.
- `deleteState(stateId)`: Deletes the state with the given ID.
- `updateState(stateId, updatedDetails)`: Updates the details of the state with the given ID.
- `viewCitiesOfState(stateId)`: Displays all cities associated with the specified state.

City Functions:

- `viewCities(stateId)`: Fetches and displays all cities for the given state.
- `addCity(stateId, name, population)`: Adds a new city to the specified state.
- `updateCity(cityId, updatedDetails)`: Updates the details of the city with the given ID.
- `deleteCity(cityId)`: Deletes the city with the given ID.

Database:

The application uses a SQLite database named `state.db` to store information about states and cities. Below is a detailed breakdown of the database structure:

Tables

`states`
- id: INTEGER PRIMARY KEY 
- name: TEXT 
- population: INTEGER
- region: TEXT

`cities`
- id: INTEGER PRIMARY KEY 
- name: TEXT 
- population: INTEGER
- state_id: INTEGER, FOREIGN KEY (state_id) REFERENCES states(id)

Relationships

- Each state can have multiple cities.
- Each city belongs to one state.

Example Data

#`states` Table

| id  | name       | population | region   |
|-----|------------|------------|----------|
| 1   | California | 39538223   | West     |
| 2   | Texas      | 29145505   | South    |

`cities` Table
| id  | name       | population | state_id |
|-----|------------|------------|----------|
| 1   | Los Angeles| 3979576    | 1        |
| 2   | Houston    | 2320268    | 2        |

This structure allows for efficient querying and management of states and their associated cities.



