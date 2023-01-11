create_tables_qs = [
    """CREATE TABLE Brand (
        brandId int PRIMARY KEY,
        brandName varchar(255) UNIQUE NOT NULL,
        countryOfOrigin char(2) NOT NULL
    )""",
    """CREATE TABLE Category (
        categoryId int PRIMARY KEY,
        categoryName varchar(255) UNIQUE NOT NULL,
        parentCategoryId int
    )""",
    """CREATE TABLE Customer (
        customerId int PRIMARY KEY,
    email varchar(255) UNIQUE NOT NULL,
    pwd varchar(255) NOT NULL,
    firstName varchar(255) NOT NULL,
        lastName varchar(255) NOT NULL
    )""",
    """CREATE TABLE Product (
        productId int PRIMARY KEY,
        productName varchar(255) UNIQUE NOT NULL,
        productDesc varchar(500) NOT NULL,
        gender varchar(10) NOT NULL,
        categoryId int NOT NULL REFERENCES Category(categoryId),
        brandId int NOT NULL REFERENCES Brand(brandId)
    )""",
    """CREATE TABLE ProductVariant (
        productVariantId int PRIMARY KEY,
        productId int NOT NULL REFERENCES Product(productId),
        colour varchar(20) NOT NULL,
        sizing varchar(10) NOT NULL,
        stock int NOT NULL,
        price float NOT NULL
    )""",
    """CREATE TABLE Purchase (
        purchaseId int PRIMARY KEY,
        customerId int NOT NULL REFERENCES Customer(customerId),
        email varchar(50) NOT NULL,
        total float NOT NULL,
        status varchar(50) NOT NULL,
        dateOfPurchase DATE NOT NULL
    )""",
    """CREATE TABLE PurchaseItem (
        purchaseId int REFERENCES Purchase(purchaseId),
        productVariantId int NOT NULL REFERENCES ProductVariant(productVariantId),
        quantity int NOT NULL,
        PRIMARY KEY (purchaseId, productVariantId)
    )""",
    """CREATE TABLE Address (
        zipCode varchar(8) PRIMARY KEY,	
        streetNumber int NOT NULL,
        streetName varchar(30) NOT NULL,
        city varchar(30) NOT NULL,
        region char(2) NOT NULL,
        country char(2) NOT NULL
    )""",
    """CREATE TABLE Shipping (
        shippingId int PRIMARY KEY,
        purchaseId int REFERENCES Purchase(purchaseId),
        recipientFirstName varchar(30) NOT NULL,
        recipientLastName varchar(30) NOT NULL,
        zipCode varchar(8) NOT NULL REFERENCES Address(zipCode),
        trackingNumber varchar(20) UNIQUE NOT NULL
    )""",
    ]
    
drop_tables_qs = [
    """DROP TABLE Brand CASCADE CONSTRAINTS""",
    """DROP TABLE Category CASCADE CONSTRAINTS""",
    """DROP TABLE Customer CASCADE CONSTRAINTS""",
    """DROP TABLE Product CASCADE CONSTRAINTS""",
    """DROP TABLE ProductVariant CASCADE CONSTRAINTS""",
    """DROP TABLE Purchase CASCADE CONSTRAINTS""",
    """DROP TABLE PurchaseItem CASCADE CONSTRAINTS""",
    """DROP TABLE Address CASCADE CONSTRAINTS""",
    """DROP TABLE Shipping CASCADE CONSTRAINTS"""
    ]

populate_tables_qs = [
    #-- Brands -------------------------------------------------------

    """INSERT INTO Brand
    VALUES (01, 'Crocs', 'US')""",
    """INSERT INTO Brand (brandId, brandName, countryOfOrigin)
    VALUES (02, 'Nike', 'US')""",
    """INSERT INTO Brand (brandId, brandName, countryOfOrigin)
    VALUES (03, 'Roots', 'CA')""",
    """INSERT INTO Brand (brandId, brandName, countryOfOrigin)
    VALUES (04, 'Gucci', 'IT')""",
    
    #-- Categories -------------------------------------------------------

    """INSERT INTO Category
    VALUES (01, 'Footwear', NULL)""",
    """INSERT INTO Category
    VALUES (02, 'Sandals', 01)""",
    """INSERT INTO Category
    VALUES (03, 'Basketball Shoes', 01)""",
    """INSERT INTO Category
    VALUES (04, 'Tops', NULL)""",
    """INSERT INTO Category
    VALUES (05, 'T-Shirts', 04)""",

    #-- Customers -------------------------------------------------------

    """INSERT INTO Customer
    VALUES (01, 'doubleP@gmail.com', 'IAmSpidey', 'Peter', 'Parker')""",
    """INSERT INTO Customer
    VALUES (02, 'thor.odinson@gmail.com', 'LokiSucks', 'Thor', 'Odinson')""",
    """INSERT INTO Customer
    VALUES (03, 'cap.america@gmail.com', 'IronMansBFF', 'Steve', 'Rogers')""",
    """INSERT INTO Customer
    VALUES (04, 'auntBae@gmail.com', 'RIPme', 'May', 'Parker')""",

    #-- Products -------------------------------------------------------

    """INSERT INTO Product
    VALUES (
    01, 
    'Crocs Women`s Classic Cog', 
    'The irreverent go-to comfort shoe that you`re sure to fall deeper in love with day after day.',
    'Women',
    02,
    01
    )""",
    """INSERT INTO Product
    VALUES (
    02, 
    'Nike LeBron 19 Basketball Shoes', 
    'Harness the fierce energy of LeBron on the court with the Nike LeBron XIX.',
    'Men',
    03,
    02
    )""",
    """INSERT INTO Product
    VALUES (
    03, 
    'Organic Original Kanga Hoodie', 
    'The Original Kanga Hoodie is super-soft and made for everyday.',
    'Unisex',
    04,
    03
    )""",
    """INSERT INTO Product
    VALUES (
    04, 
    'Oversize washed T-shirt with Gucci logo', 
    'Alessandro Michele brings the Gucci logo to the forefront, inspired by vintage prints from the eighties.',
    'Unisex',
    05,
    04
    )""",

    #-- Product Variants  ----------------------------------------------------

    #-- Crocs slippers variants
    """INSERT INTO ProductVariant
    VALUES (01, 01, 'White', '7 (US)', 50, 47.99)""",
    """INSERT INTO ProductVariant
    VALUES (02, 01, 'Purple', '6 (US)', 47, 37.99)""",
    """INSERT INTO ProductVariant
    VALUES (11, 01, 'Blue', '6 (US)', 47, 37.99)""",
    #-- Nike basketball shoe variants
    """INSERT INTO ProductVariant
    VALUES (03, 02, 'White', '8 (US)', 0, 195.99)""",
    """INSERT INTO ProductVariant
    VALUES (04, 02, 'Red', '9 1/2 (US)', 21, 195.99)""",
    #-- Roots sweater variants
    """INSERT INTO ProductVariant
    VALUES (05, 03, 'Grey', 'S', 3, 94)""",
    """INSERT INTO ProductVariant
    VALUES (06, 03, 'Grey', 'M', 0, 94)""",
    """INSERT INTO ProductVariant
    VALUES (07, 03, 'Grey', 'L', 16, 94)""",
    #-- Gucci shirt variants
    """INSERT INTO ProductVariant
    VALUES (08, 04, 'White', 'S', 32, 720)""",
    """INSERT INTO ProductVariant
    VALUES (09, 04, 'White', 'M', 0, 720)""",
    """INSERT INTO ProductVariant
    VALUES (10, 04, 'White', 'L', 45, 720)""",

    #-- Purchases -------------------------------------------------------
    #-- Peter Parker purchased Crocs
    """INSERT INTO Purchase
    VALUES (01, 01, 'doubleP@gmail.com', 102.16, 'Shipped', TO_DATE('2022-09-27', 'YYYY-MM-DD'))""",
    """INSERT INTO PurchaseItem
    VALUES (01, 01, 1)""",
    """INSERT INTO PurchaseItem
    VALUES (01, 02, 1)""",

    #-- Thor purchased Nike and Crocs
    """INSERT INTO Purchase
    VALUES (02, 02, 'thor.odinson@gmail.com', 318.67, 'Delivered', TO_DATE('2022-10-03', 'YYYY-MM-DD'))""",
    """INSERT INTO PurchaseItem
    VALUES (02, 03, 1)""",
    """INSERT INTO PurchaseItem
    VALUES (02, 02, 2)""",

    #-- Captain America purchased Crocs and Gucci shirt
    """INSERT INTO Purchase
    VALUES (03, 03, 'cap.america@gmail.com', 867.83, 'Placed', TO_DATE('2022-11-11', 'YYYY-MM-DD'))""",
    """INSERT INTO PurchaseItem
    VALUES (03, 01, 1)""",
    """INSERT INTO PurchaseItem
    VALUES (03, 08, 1)""",

    #-- Peter Parker purchased Roots and Crocs
    """INSERT INTO Purchase
    VALUES (04, 01, 'doubleP@gmail.com', 372.89, 'Delivered', TO_DATE('2022-11-12', 'YYYY-MM-DD'))""",
    """INSERT INTO PurchaseItem
    VALUES (04, 01, 1)""",
    """INSERT INTO PurchaseItem
    VALUES (04, 05, 2)""",
    """INSERT INTO PurchaseItem
    VALUES (04, 06, 1)""",

    #-- Addresses -------------------------------------------------------

    """INSERT INTO Address
    VALUES (
    10001,
    20, 
    'Ingram Street',
    'New York City', 
    'NY',
    'US'  
    )""",
    """INSERT INTO Address
    VALUES (
    20002,
    16, 
    'Ocean Drive',
    'Miami City',
    'FL',
    'US'
    )""",
    """INSERT INTO Address
    VALUES (
    'M2F8S1',
    32, 
    'Dundas Street',
    'Toronto', 
    'ON',
    'CA' 
    )""", 

    #-- Shipping -------------------------------------------------------

    """INSERT INTO Shipping
    VALUES (
    01,
    01, 
    'Peter', 
    'Parker',
    10001,
    'dwlla83dmwlt77t24ua9'
    )""",
    """INSERT INTO Shipping
    VALUES (
    02,
    02, 
    'Thor', 
    'Odinson',
    20002, 
    'dwllawebgft77t24ua9'
    )""",
    """INSERT INTO Shipping
    VALUES (
    03,
    03, 
    'Steve', 
    'Rogers', 
    'M2F8S1', 
    'yo830m9e6jk4n6jls539'
    )""",
    """INSERT INTO Shipping
    VALUES (
    04,
    04, 
    'Peter', 
    'Parker',  
    10001, 
    'e3nzvievudelu5ku7uf4'
    )"""
    
    ]
