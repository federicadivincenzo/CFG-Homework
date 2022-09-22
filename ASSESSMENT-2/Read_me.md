## ASSESSMENT 2
#### student: Federica Di Vincenzo

#### 1.	Python / SQL theory questions

1.	What is Thread and Multithreading?
> The tread is the process in which the program is executed. In multiple threading the program run on different threads switching quickly.
2.	What is Concurrency and Parallelism and what are the differences?
> Concurrency tasks run at the same time
> Parallelism tasks run in parallel process
3.	What is Garbage collector? How does it work?
> Garbage Collector cleans the memory by deleting no more used or unwanted object.
4.	What is Transaction Management in a relational database (give an example)?
> Transactional management keeps control of all the changes that happens in a database. For example in the ATM program we checked the balance of the client, if the withdrawal could be done, and if so, we decrease the balance of the amout of the withdrawal made and storing the new balance amount.
5.	What is an endpoint and what are the most common methods to interact with the API data source?
> The endpoint is the digital location from where the API get and send the information. Most common methods are GET - Get the info from the server, POST -> send info to server, PATCH -> edit an info, DELETE -> delete info
6.	What is data normalisation in SQL? Please provide an example (any) of a database restructuring using primary/foreign keys to maintain data integrity. 
> Data normalisation in SQL happens when we keep our data clean and organised to ensure data integrity. 
Example
```
CREATE TABLE Bookings (
    Booking_id int NOT NULL AUTO_INCREMENT,
    Time date NOT NULL,
    Customer_id int NOT NULL,
    PRIMARY KEY (Booking_id),
    FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
);
```

### 2.	Discuss Exception handling (4 pts) and debugging in Python (4 pts)

> We use execution handling to try if a code works and to prevent any error that we can collect with the except keyword. We use debugging to understand what is raising an error in our code by analysing line by line what is happening. 
> eg:
```
try: 
    transform_to_square(2)
except ValueError:
    print("Please insert a list of numbers") 
```

### 3.	Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
```
def transform_to_square(nums):
    new_list = list(map(lambda n: n * n, nums))
    new_list.sort()
    return new_list
```

Example Input: 

numbers = [1,2,3,5,6,8,9]

Example Output:

[1,4,9,25,36,65,81]

### 4.	Write tests for the newly created Sorted Squared Numbers function (in Q3). Provide a brief explanation for your test case options
> We import **unittest** and the function we want to test from the main file
> The first test check if the function return correctly the expected results testing on three numbers
```
    def transform_to_square_valid(self):
        expected = [1,4,9]
        actual = transform_to_square([1,2,3])
        self.assertEqual(expected, actual)
```

> Second test to check if raise error if a string is passed instead of a number
```
  def transform_to_square_invalid(self):
      while self.assertRaises(TypeError):
         transform_to_square(['string', 'string'])
```

> Third test to check if the function works when passing edge elements
```
  def transform_to_square_valid_edge(self):
        expected = [-1, 0.01, 0]
        actual = transform_to_square([1,0.0001,0])
        self.assertEqual(expected, actual)
```
### 5.	Agile methodology: name and describe any 2 of the main roles in a Scrum Agile team.

> **Scrum Master** is the lead of the agile team, he's responsible for ensuring that each team member has the right tool to proceed with the work planned, guide the team and is the point of contact for any issue or problem.
> **Team Member** : are the operational asset of the team as the developer. They are responsible for the creation of the product. 

### 6.	Discuss advantages and disadvantages of TDD (Test Driven Development):

> **Advantages** : is safer, because you only use code that is tested and safe to use. It easy to debug in case of future problem and is less likely to raise problem.
> **Disadvantages**: take more time to write, needs commitment by the whole team to write test frequently and not suitable for large and complex projects that needs to be developed fast

### 7.	What is a Python DB cursor? Provide an example 

> We use a cursor when we connect to an SQL database through Python code. We use a cursor to fetch the element we need in a database according to a query we write. 

**Example: we connect to a database**

```
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx
```

We create a cursor, and we use the cursor to execute the query and display the result we receive. If the fetch is True we can then close the cursor. We create a new cursor for each function and query.

```
def get_all_records():
    try:
        db_name = 'database_name'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM database_name.table"""
        cur.execute(query) # cursor execute the query
        result = cur.fetchall()   #cursor fetch all the results

        for i in result:
            print(i)
        cur.close()  #we close the cursor

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
```

8.	SQL EXERCISE [here](./SQL_assessment.sql) 
9.  TWO NUM SUM [here](./two_numbers.py) 