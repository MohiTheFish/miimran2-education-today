# Education Today Citations
As part of the application for the 25% RA position, I completed the first task, to find the most cited papers by a given author.

## SQL Database
I first began by taking a look at the schema on the Microsoft documentation, and picked out the relevant fields, as well as additional fields that I was personally interested in. I was planning to keep these fields around for ability to render additional information.

See the db_scripts folder to see the tables and format I used to read in data. Note: I chose not to have explicit foreign keys as it seemed SOME of the rows did not satisfy the Foreign key constraints, and so the database creation consistently failed.

One thing I did have trouble with is the Papers database. Whenever I tried to read it in, the format consistently failed on certain rows. I began the process of using a Python notebook with the pandas library to format the data better, but my laptop was taking far too long processing the dataset. For this reason, when you view the data on the front end, I end it at PaperId, since the Papers table is not properly entered. 

## Flask Server
To understand how to implement the flask server, I used this tutorial: https://dev.to/dev_elie/connecting-a-react-frontend-to-a-flask-backend-h1o. 
This tutorial had a lot of information about taking advantage of Flask-SqlAlchemy to create Python Modals for all tables in the database. I didn't use these to their full advantage, however, as the SQL query I wanted to do was a little complicated, involving a join and group by, and I felt that using SQL directly would increase legibility since it's usage is more widespread. 

The endpoint I created is at '/author/:name/citations/', where :name corresponds to either the actual name of the author OR the author Id. This returns a json in the following shape:
```json
{
    name: string (author_name),
    id: number (author_id),
    mostReferenced: [
        {
            count: number,
            paperId: number,
        }
    ]
}
```
## React Frontend
I began with the basic CRA template, and started creating a MainPage. The MainPage has a simple text entry field, provided from Material UI. In here, the user types in either the name of the author, or they type in the author Id corresponding to the author in the text field. After making a request to the backend, and doing some error checking, the results will be rendered. As mentioned before, since I didn't get the Papers table working on my machine, I chose not to drill further to retrieve information about each paper, such as the title.