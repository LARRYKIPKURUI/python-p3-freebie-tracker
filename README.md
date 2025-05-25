# Freebie Tracker

## Project Overview

This project is a Freebie Tracker app designed to help developers keep track of swag (free items) they collect from hackathons and events. The main models are:

- **Company**: Companies that give out freebies.
- **Dev**: Developers who receive freebies.
- **Freebie**: Items given to developers by companies.

The relationships are:

- A `Company` has many `Freebie`s.
- A `Dev` has many `Freebie`s.
- A `Freebie` belongs to one `Company` and one `Dev`.
- A `Company` and `Dev` have a many-to-many relationship through freebies.


### Database Schema

View the full database schema here:  
[Schema Link](https://dbdiagram.io/d/Code-Challenge-Schema-682d6600b9f7446da371de0f)

---

## Setup Instructions

1. **Install dependencies and activate environment**  
   Run the following commands inside your project directory:

   ```bash
   pipenv install
   pipenv shell

2. **Run Migrations**
    Create and apply migrations to set up the database schema, including the freebies table

3. **Seed the database**
    Use the provided seed.py script to populate the database with sample data:
    ```bash
    python seed.py
    ```
