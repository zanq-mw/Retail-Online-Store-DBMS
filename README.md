# Retail Online Store DBMS

This is a a command line program used to manage a database for an online retail business selling apparel, footwear, and other accessories. This database contains information regarding what products are available, the specifics of these products, what orders have been, shipping information, customer information, etc.

Using this program, one can create all neccessary tables, populate the tables with data, make changes to the data (add, update, delete), query the data, and also drop all tables. It serves as a way to access the database without the user needing to use SQL queries.

## The Database

The database features 9 tables:

- **Product** contains data on the products available
- **ProductVariant** contains data on the specifics of the products in **Product**
- **Brand** contains data on the brands that the retail business carries
- **Category** contains data on the categories available (examples include Outerwear, Footwear, etc.)
- **Customer** contains data on the customers of the business, given that they have signed up with their email
- **Purchase** contains data on purchases made
- **PurchaseItem** contains data on the specific items of each purchase in **Purchase**
- **Shipping** contains data on the shipping information for each purchase in **Purchase**
- **Address** contains data on the addresses of each shipment in **Shipping**

Products would be categorized by their characteristics entered into the database such as its brand, name, a description of it, as well as tags to define it by. In order to purchase, a user would need to sign up and enter themselves into the database giving them a user ID and allowing them to collect and spend through purchases they make. Orders made are also entered into the database being given an order ID with information such as who, when, and where the order was made and is to be shipped to.

#### Entity-Relationship Diagram of the Database

![ER Diagram](images/erDiagram.jpg?raw=true)

## How to Run

An oracle database connection is needed to run this program. You must have the neccessary credentials to login to the connection as this will needed to be inputted in the config file.

Also, you will need to install [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html). Make note of where you unzip this file as you will need to input the path to the config file.

Clone this github repository to your computer

```bash
$ git clone https://github.com/zanq-mw/Retail-Online-Store-DBMS.git
```

Open the Retail-Online-Store-DBMS/dbManager/config.py file. It should look like this:

```python
lib_dir = ""
host=""
port=0
sid=''
user=""
password=""
```

You must populate the values for this file. The lib_dir variable should have the value of a string of the path to the Oracle Instant Client Folder.

The host, port, sid, user, and password variables refer to the host name, port number, SID, username, and password of the Oracle database respectively.

Run the Retail-Online-Store-DBMS/dbManager/main.py file to start the program.

```bash
$ python3 "{PATH TO FOLDER CONTAINING REPO}/Retail-Online-Store-DBMS/dbManager/main.py"
```

You can then use the application commands to interact the database.

```bash
   c = Create all tables
   d = Delete all tables
   p = Populate all tables
   q {table} = Query all entires of a table
   qspec {table} = Query specific row from a table
   add {table} = Add row to a table
   upd {table} = Update a row in a table
   del {table} = Delete row from a table
   quit = Quit application
```

Note: Wrap any input strings to the DB in single quotations, for ex:

```bash
> a Brand
> Enter values seperated by commas for...: 1, 'Name', 'CA'
```

## Example Interactions

#### Dropping, Creating, Populating, and Querying Tables

![](images/example1.png?raw=true)

#### Querying specific row from a table

![](images/example2.png?raw=true)

#### Add row to a table

![](images/example3.png?raw=true)

#### Update a row in a table

![](images/example4.png?raw=true)

#### Delete a row

![](images/example5.png?raw=true)
