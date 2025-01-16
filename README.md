# Daisy - CBT Mood Tracker

**Daisy** is a personal program designed to help me track my mood, this helps me when going for councilling/therapy. It serves as a tool to support Cognitive Behavioral Therapy (CBT) by offering insights into emotional patterns and progress over time.

## Future Updates

I want to add a login so i can have some security. On the topic of security I do want the passwords to be stored safely. 

## Daisy v1

### Features

- Track your mood on a given day and time.
- Rate your tolerance level for each mood at the moment.
- Write a description reflecting how you handled the emotional situation.
- View a history of all entries.

### Lessons Learned

- Using an array to have some form of memory for the journal.
- Accessing the array and retrieving data.
- Error handling.

This programme is also the first in which I tried everything myself before seeking help. This has helped me understand the fundamentals of programming that little bit better. I have also noticed that I can read code a bit better than before now.



## Daisy v2

### Features

- Store enteries in a MySQL database (locally).
- View all the enteries.
- Delete enteries.
- View a history of all entries.
- Date and Time stamping

### Lessons Learned

- Creating a MySQL database (Both in python and MySQL Workbench)
- Crerating tables for a database (Both in python and MySQL Workbench)
- CRUD: Create, Read, Update, Delete
- Writing SQL queries
- Connecting to a database via python
- Passing queries from python

This version has taught me quite a lot. I first started looking into SQLite3 with python and it was a good introduction to databases in programming and how to connect and interact with databases. I wanted to know a bit more using a more popular database. Quick google, and MySQL won for no particular reason other than it was the first I seen.

So I downloaded MySQL Workbench, installed mysql.connector in python and got to it. As a visual learner I first go to YouTube for a quick introductory as I have seen and played with SQL before. I then got to work using python to create the database, then workbench to write queries and build the tables needed with the correct columns. 

From there I hopped over to my copy of v1 and begin to alter it to include the local database.
