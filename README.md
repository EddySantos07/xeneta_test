First install poetry if you do not have it

```bash
pip install poetry
```

then tell poetry to install dependencies 

```bash
poetry install
```

then you can try out - http://127.0.0.1:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main

but the only problem here is the table is not working, tried to fix this but ended up spending too much time leading to the rest going in blind! 

# What I would do different

I would certainly make everything run smooth first i had to drop the table from docker
then init the table again from the dockerfile
'
a simple way would be just to docker run ratestask

then I would make sure the connection and psycopg2 would work well with postgres as 
something was happening where psycopg2 was not getting any tables from tasksrates container

I would then fix the queries as I could not test propery and would make sure that is in line

I also understood how the ports and regions worked together as you get the ports from the regions if only handed regions.

possible combinations were 4 with 2 being interchangeable a bit!



-----------------------------
# Assignment: HTTP-based API

Develop an [HTTP-based API](#task-1-http-based-api) capable of handling the GET request described below. Our stack is based on Flask, but you are free to choose any Python framework you like. All data returned is expected to be in JSON format. Please demonstrate your knowledge of SQL (as opposed to using ORM querying tools).


Implement an API endpoint that takes the following parameters:

* date_from
* date_to
* origin
* destination

and returns a list with the average prices for each day on a route between port codes *origin* and *destination*. Return an empty value (JSON null) for days on which there are less than 3 prices in total.

Both the *origin, destination* params accept either port codes or region slugs, making it possible to query for average prices per day between geographic groups of ports.

    curl "http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"

    [
        {
            "day": "2016-01-01",
            "average_price": 1112
        },
        {
            "day": "2016-01-02",
            "average_price": 1112
        },
        {
            "day": "2016-01-03",
            "average_price": null
        },
        ...
    ]

# Requirements

* Write the solution using Python and SQL, you can use an ORM but please
  demonstrate some raw SQL

* Keep your solution in a Version Control System of your
  choice. *Provide the solution as a public repository that can be
  easily cloned by our development team.*

* Provide any instructions needed to set up the system in `README.md`.

* Ensure the API handles errors and edge cases properly.

* Use dates in YYYY-MM-DD format for the API. There is no need for more
  complicated date processing.

# Extra details

* It usually takes 2 - 6 hours to complete this task for a developer with 2+ years of experience in building APIs with Python and SQL.

* Our key evaluation criteria:
    - Ease of setup and testing
    - Code clarity and simplicity
    - Comments where appropriate
    - Code organisation
    - Tests

* You are encouraged to modify or extend the database schema if you think a different model fits the task better.

* If you have any questions, please don't hesitate to contact us

* Please let us know how much time you spent on the task, and of any difficulties that you ran into.


# Initial setup

We have provided a simple Docker setup for you, which will start a
PostgreSQL instance populated with the assignment data. You don't have
to use it, but you might find it convenient. If you decide to use
something else, make sure to include instructions on how to set it up.

You can execute the provided Dockerfile by running:

```bash
docker build -t ratestask .
```

This will create a container with the name *ratestask*, which you can
start in the following way:

```bash
docker run -p 0.0.0.0:5432:5432 --name ratestask ratestask
```

You can connect to the exposed Postgres instance on the Docker host IP address,
usually *127.0.0.1* or *172.17.0.1*. It is started with the default user `postgres` and `ratestask` password.

```bash
PGPASSWORD=ratestask psql -h 127.0.0.1 -U postgres
```

alternatively, use `docker exec` if you do not have `psql` installed:

```bash
docker exec -e PGPASSWORD=ratestask -it ratestask psql -U postgres
```

Keep in mind that any data written in the Docker container will
disappear when it shuts down. The next time you run it, it will start
with a clean state.


---------------------------------



