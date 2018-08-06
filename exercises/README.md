# Y2 2018 Summer: Databases Lab

Welcome to the databases lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

In this lab, we will create our own database. The only files that you will
need to modify are `knowledge_model.py` and `knowledge_databases.py`.

### Part 1: Creating a Database Model

1. After realizing just
how easy it is to organize information, you decide to create a website to 
organize all the information in the world. To start off, you'd like to understand
what kind of topics people are interested in. Survey at least three people
around you and ask them what they want to learn about!

2. To start with, you decide to look on Wikipedia to find information on the relevant
topics. So, for each topic that has been chosen, find a Wikipedia article that
your friends can use to learn more about the topic. 

3. Read through the articles and give them a rating from 1-10, based off of how
much you liked them and what you've learned.

4. Now, after doing this, you have enough information to create a database of
the knowledge you've learned so far. The database should have:
- A primary key (what would this be for the set of articles?). Choose an attribute appropriately.
- The topic of the article (what did your friends want to learn about?)
- The title of the relevant article that you've chosen. This can be the same as the topic of the article, but it does not have to be!
- Your rating of the article, from 1-10.
Edit `knowledge_model.py` and create a table, named `knowledge`, to create a table which stores this information.

5. Add a `__repr__` function to your table. That is, when you want to print an instance
of the Knowledge class, which has primary key 1, a topic of weather, a title of rainbow,
and a rating of 9, the following should be printed:
```
If you want to learn about weather, you should look at the Wikipedia article called rainbow.
We gave this article a rating of 9 out of 10!
```

6. Bonus: If the article is rated lower than 7 out of 10, add the following message, after
the message above, when printing the object.
```
Unfortunately, this article does not have a better rating. Maybe, this is an article that should be
replaced soon!.
```

6. Bonus: Add printing of the primary key to the `__repr__` function in `knowledge_model.py` so that
we can see what the primary keys of the articles in the DB are!

### Part 2: Adding to your Database

In this part and all the next ones, you will only need to edit `knowledge_databases.py`. 

1. Now, we'd like to add the articles that you've already read and rated to your database. To do
this, write a function `add_article` in `knowledge_databases.py`, to add a new article to
your database. What inputs does this function need?

2. Make sure to run your function at least once, so that your database will contain at least one article.

### Part 3: Querying your database.

1. Write a function `query_all_articles()` to print all the articles in your database. For each article,
this should print the statement described in Part 1.5 (or 1.6, if you did the bonus!). When you run this
function, you should see all the articles that you have previously added to the DB!

2. Now, you'd like to look up an article by its topic. Write a function `query_article_by_topic()` to
retrieve all the articles in a specific topic. 

3. Bonus: Sometimes, you want to find all articles, which have low ratings. Add a function
`query_article_by_rating()`, which takes an input parameter, `threshold`, and returns all articles
which have a rating that is lower than `threshold`.

4. Bonus: Sometimes, you want to find a specific article. Since the only unique property that 
each article is guaranteed to have is a primary key, add a function `query_article_by_primary_key()`,
which returns the article with the correct primary key.

### Part 4: Deleting from your Database

1. Write a function `delete_article_by_topic()`, which removes all articles in a certain topic
from the database. Test this function out to remove all articles from a topic that's in your DB.

2. Write a function `delete_all_articles()`, which removes all the articles from your database!

### Part 5: Editing in your Database

1. Write a function `edit_rating()`, which takes in input parameters `updated_rating` and `article_title`. This function should update all articles with the given title to have a rating of `updated_rating`.

2. Bonus: Now, you'd like to improve the quality of your database. So, you decide to write a function
which removes all articles from your database if their rating is too low. Write a function `delete_article_by_rating()`, which takes an input threshold, and removes all articles that have a rating
below `threshold`. Are there other functions that you've implemented that could be useful here?

### Part 6: Bonus!

Add additional functionality to your database. This can include, but is not limited to:
- Adding a new query function, which returns the top-5 highest rated articles in the DB.
- A new function to update the rating of a DB, which takes the average of the original rating
and the new rating. What data type should this column have? You might need to edit `knowledge_model.py`
and add some additional imports to get this working correctly.
- Editing your database model, to add a new column, which keeps track of the number of times
an article has been queried. Then, edit `knowledge_model.py` to
give this column a default value of 0, when adding a new article to the DB.
When should this column be updated? 
*Note: If you're doing this, you might get some SQLAlchemy issues. You can resolve this by
deleting the file knowledge.db, which stores the schema of the old database, which has now
been changed. This file should be in the exercises folder, which you are working in.*
