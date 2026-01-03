
# Project file directory
```
my-python-app/
├── Dockerfile            # Instructions on how to build the image
├── docker-compose.yml    # (Optional) Easier way to run the container
├── requirements.txt      # The manifest file. It serves as dependency management (e.g. List of  libraries (like Flask or Pandas))
├── .dockerignore         # Files Docker should ignore (like local caches)
└── src/                  # Your actual Python code lives here
    ├── main.py           # The entry point of the program
    └── utils.py          # All functions resides here
```

# Postgres SQL commands

To access the Postgres container terminal

``` Code
docker exec -it postgres-db psql -U user -d cryptodb
```
## 1. Meta-Commands (The Shortcuts)

These are specific to the psql terminal tool. Remember: No semicolon needed for these.

``` 
Command	Purpose
\dt	List all tables in the current database.
\d table_name	Describe a table (shows columns, types, and keys).
\l	List all databases on the server.
\c db_name	Connect to a different database.
\q	Quit the Postgres terminal.
\dn	List schemas (usually you'll just see "public").
```

## 2. Data Definition (DDL)
This is how you build the "structure" or "skeleton" of your data. These require a semicolon (;).
Create a Table
```SQL
CREATE TABLE bitcoin_prices (
    id SERIAL PRIMARY KEY,        -- Auto-incrementing ID
    price FLOAT NOT NULL,         -- Decimal numbers
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Auto-date/time
);
```

Delete a Table
```SQL
DROP TABLE bitcoin_prices;
```

## 3. Data Manipulation (DML)

This is how you interact with the actual data (the "meat").
Create (Insert)
```SQL
INSERT INTO bitcoin_prices (price) VALUES (64000.50);
```

Read (Select)
```SQL
SELECT * FROM bitcoin_prices;                 -- See everything
SELECT price FROM bitcoin_prices LIMIT 5;     -- See only the last 5
SELECT * FROM bitcoin_prices WHERE price > 60000; -- Filter results
```
Update
```SQL
UPDATE bitcoin_prices SET price = 65000 WHERE id = 1;
```

Delete
```SQL 
DELETE FROM bitcoin_prices WHERE id = 1;
```

## 4. Data Analysis (The "Next Level")

These are the queries that make your Python app useful.
Find the Average Price
```SQL 
SELECT AVG(price) FROM bitcoin_prices;
```

Count your Total Records
```SQL
SELECT COUNT(*) FROM bitcoin_prices;
```
Find the Highest and Lowest Prices
```SQL
SELECT MAX(price), MIN(price) FROM bitcoin_prices;
```
## 5. Information Schema (The "Secret" SQL)

If you forget the shortcut \dt, you can use this standard SQL to see your tables:
```SQL
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```