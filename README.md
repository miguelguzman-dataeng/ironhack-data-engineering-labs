# Ironhack Data Engineering Labs

This repository contains my labs and practice work from the Ironhack Data Engineering bootcamp.

I use this repository to document my progress in Python, SQL, data processing, and future Data Engineering projects.


## Week 1 — Session 1: Python Basics

### File

- `ironhack_lab_script_day1.ipynb`

### Concepts Practiced

- Comments
- `print()` function
- Python execution flow
- Variables and assignment
- Data types: `int`, `float`, `str`, and `bool`
- Type casting with `int()`, `float()`, and `str()`
- Arithmetic operators
- Comparison operators
- Logical operators
- `input()` function
- f-strings and formatted output
- Basic debugging
- Simple billing calculations


## Week 1 — Session 2: Python Control Flow and Data Structures

### File

- `notebooks_lab_script_02.ipynb`

### Concepts Practiced

- `if`, `elif`, and `else` conditions
- Nested conditions and logical operators
- `for` and `while` loops
- Loop control with `break` and `continue`
- Lists, indexing, slicing, `insert()`, and `remove()`
- Tuples, unpacking, and immutability
- Sets and duplicate removal
- Dictionaries, key access, and value updates
- Looping through dictionaries with `.items()`
- Aggregation with running totals
- Finding maximum values using loops and conditions
- Choosing between lists, tuples, sets, and dictionaries
- Lists of dictionaries and nested dictionaries
- Mini-ETL workflow: filter, transform, aggregate, and report

### Mini-ETL Lab

The integrated exercise processes order records by:

- Filtering delivered orders
- Calculating total sales per customer
- Collecting unique product IDs
- Counting delivered orders
- Building a structured report with dictionaries and sets


## Week 1 — Session 3: Python Functions and NumPy

### File

- `notebooks_lab_script_03.ipynb`

### Concepts Practiced

- Defining and calling reusable functions
- Parameters and arguments
- Return values
- Default and optional arguments
- Simple validation inside functions
- Writing clear function names and docstrings
- Cleaning and normalizing strings
- Processing lists with reusable functions
- Returning multiple values from functions
- NumPy array creation and data types
- Array indexing and slicing
- Boolean masks and array filtering
- Vectorized NumPy operations
- NumPy aggregations: sum, min, max, and mean
- Replacing invalid values with `np.nan`
- Removing missing and invalid values
- Applying discounts with Boolean indexing
- Building summary dictionaries
- Final integrated sales ETL workflow

### Sales ETL Lab

The final integrated exercise processes raw daily sales data by:

- Converting a Python list into a NumPy array of floats
- Replacing negative and zero values with `np.nan`
- Removing missing and invalid values
- Applying discounts to sales above a configurable threshold
- Using default arguments for the threshold and discount rate
- Calculating total, count, mean, minimum, and maximum
- Returning structured results with reusable functions
- Printing a formatted sales summary
  
## Week 1 — Session 4: Pandas for Data Handling

### File

- `lab_script04.py`

### Data Files

- `customers.csv`
- `orders.csv`
- `products.json`
- `orders.xlsx`

### Generated Output Files

- `sales_report.csv`
- `sales_report.json`
- `city_category_report.csv`

### Concepts Practiced

- Creating pandas `Series` and `DataFrame` objects
- Creating DataFrames from Python dictionaries
- Reading CSV files with `pd.read_csv()`
- Reading Excel worksheets with `pd.read_excel()`
- Reading JSON files with `pd.read_json()`
- Inspecting datasets with `head()`, `tail()`, `shape`, `info()`, and `describe()`
- Selecting single and multiple columns
- Filtering rows with Boolean conditions
- Detecting missing values with `isnull()`
- Replacing missing values with `fillna()`
- Removing incomplete rows with `dropna()`
- Renaming columns with `rename()`
- Creating derived columns
- Calculating values with 18% tax
- Sorting rows with `sort_values()`
- Grouping and aggregating data with `groupby()` and `agg()`
- Calculating totals, averages, and order counts
- Merging customer, order, and product datasets
- Performing SQL-style left joins with `pd.merge()`
- Exporting cleaned results to CSV and JSON
- Building a complete mini ETL workflow

### Mini ETL Lab

The integrated exercise processes customer, order, and product data by:

- Reading data from CSV and JSON files
- Merging orders with customer information
- Adding product category information
- Replacing missing cities and categories with `Unknown`
- Creating an `amount_with_tax` column
- Grouping results by city and category
- Calculating total sales, average order value, and order count
- Sorting the report by total sales
- Exporting the final result to `city_category_report.csv`
  



## Week 1 — Session 5: SQL Basics Lab 5
### File

- `sql_basics_lab_5.sql`

### Concepts Practiced

- Creating tables with `CREATE TABLE`
- Defining columns and data types
- Using `PRIMARY KEY`
- Using `FOREIGN KEY`
- Creating relationships between tables
- Inserting data with `INSERT INTO`
- Selecting data with `SELECT`
- Selecting specific columns
- Counting rows with `COUNT()`
- Removing duplicate results with `DISTINCT`
- Filtering data with `WHERE`
- Using comparison operators
- Filtering ranges with `BETWEEN`
- Searching text patterns with `LIKE`
- Sorting results with `ORDER BY`
- Using aggregate functions:
  - `AVG()`
  - `MAX()`
  - `MIN()`
  - `COUNT()`
- Grouping data with `GROUP BY`
- Filtering grouped results with `HAVING`
- Connecting tables with `JOIN`
- Keeping all rows from one table with `LEFT JOIN`
- Updating existing data with `UPDATE`
- Deleting rows with `DELETE`
- Using aliases with `AS`
- Writing SQL comments to explain queries

### Database Structure

The lab uses two connected tables:

- `Departments`
- `Employees`

The tables are connected through the `DepartmentID` column.

```text
Departments.DepartmentID
            ↑
            │
Employees.DepartmentID
## Goal



## WEEK 2 — SESSION 1: Data Engineering Fundamentals

### File

* `week_2_session_1_data_engineering_fundamentals.docx`

### Concepts Practiced

* Understanding the complete Data Engineering pipeline lifecycle
* Identifying source, ingestion, storage, processing, serving, and monitoring components
* Classifying systems as **OLTP** or **OLAP**
* Choosing between **batch**, **micro-batch**, and **streaming** processing
* Understanding **ETL** versus **ELT**
* Understanding **schema-on-write** versus **schema-on-read**
* Mapping different source types:

  * Relational databases
  * CSV files
  * REST APIs
  * Application logs
  * Mobile and web events
  * NoSQL databases
* Designing Bronze, Silver, and Gold data layers
* Understanding the difference between a **Data Lake** and a **Data Warehouse**
* Selecting ingestion tools such as:

  * Apache Airflow
  * Apache NiFi
  * Apache Kafka
  * Airbyte
  * Debezium
  * Filebeat
* Selecting processing tools such as:

  * Apache Spark
  * Spark Structured Streaming
  * Apache Flink
  * Python and Pandas
  * dbt
* Designing a daily batch pipeline from PostgreSQL to a Data Warehouse
* Using Parquet as a columnar file format
* Partitioning data by date
* Writing SQL to calculate daily revenue per product
* Designing a high-volume clickstream pipeline
* Enriching streaming events with user-profile data
* Using five-minute sliding windows
* Handling late and out-of-order events with watermarks
* Understanding at-least-once and exactly-once processing
* Planning retries, monitoring, alerts, and data-quality checks
* Understanding the small-files problem and file compaction

### Labs Completed

1. Identify pipeline components from a scenario
2. Classify systems as OLTP or OLAP
3. Classify processing as Batch or Streaming
4. Choose between ETL and ELT
5. Map sources to ingestion, storage, processing, and serving
6. Design a batch e-commerce orders pipeline
7. Design a streaming clickstream pipeline
8. Choose ingestion tools for APIs, files, and logs


# Week 2 — Data Engineering Fundamentals

This week focused on core Data Engineering concepts, including relational and NoSQL databases, schema design, normalization, data lake architecture, query performance, partitioning, and file formats.

The goal of these sessions was to understand how data is stored, modeled, processed, and optimized in real Data Engineering systems.

---

## Session 2 — Relational and NoSQL Database Fundamentals

### Topics covered

- Relational databases
- NoSQL databases
- ACID
- BASE
- Primary keys
- Foreign keys
- Referential integrity
- Document databases
- Key-value databases
- Column-family databases
- Graph databases
- Eventual consistency

### Practical exercises

- Created relational tables with SQLite
- Used primary and foreign keys
- Joined employees with departments
- Simulated an ACID transaction rollback
- Created flexible document-style product data
- Simulated a key-value cache
- Simulated eventual consistency
- Computed friends-of-friends using a graph structure

### Main takeaway

Relational and NoSQL databases solve different problems.

Relational databases are strong for structured data, relationships, transactions, and consistency.

NoSQL databases are useful when flexibility, scalability, high write throughput, or relationship traversal is more important.

---

## Session 3 — Schema Design, Normalization, and Denormalization

### Topics covered

- Entities and attributes
- Primary keys and foreign keys
- One-to-many relationships
- Many-to-many relationships
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- OLTP schema design
- Denormalization
- Star schemas
- Fact tables
- Dimension tables
- Grain
- ETL mapping
- Slowly Changing Dimension Type 2
- Query performance trade-offs

### Practical exercises

- Identified entities from a flat e-commerce CSV
- Designed relationships between Customer, Order, Product, and OrderItem
- Converted repeating groups into atomic rows
- Flattened nested product data using Python
- Removed partial and transitive dependencies
- Designed a normalized OLTP schema
- Designed a denormalized reporting table
- Created a star schema
- Defined fact table grain
- Sketched an ETL transformation
- Modeled customer history using SCD Type 2
- Compared denormalization strategies for reporting performance

### Main takeaway

Good schema design depends on the purpose of the system.

OLTP systems usually benefit from normalized schemas because they reduce duplication and protect data integrity.

Analytics systems often use denormalized models such as star schemas because they simplify reporting and improve query performance.

---

## Session 4 — Data Lake, Data Warehouse, and Lakehouse Architecture

### Topics covered

- Data Lake
- Data Warehouse
- Lakehouse
- Schema-on-read
- Schema-on-write
- Bronze layer
- Silver layer
- Gold layer
- Separation of compute and storage
- Metadata
- Data catalogs
- Data governance

### Architecture flow

```text
Data Sources
↓
Bronze
Raw / original data
↓
Silver
Cleaned / standardized / validated data
↓
Gold
Business-ready data
↓
Dashboards / Analytics / Reporting


Session 5 — Query Performance, Storage Layout, and Data Formats
Topics covered
Full table scans
Indexes
Query plans
Filtering early
Selecting only required columns
Partitioning
Partition pruning
Small-files problem
File compaction
CSV
Parquet
Avro
ORC
Row-oriented storage
Columnar storage
Compression
Analytical storage design
Practical exercises
Used EXPLAIN QUERY PLAN
Compared query behavior before and after creating an index
Compared filtering in Python with filtering and aggregation in SQL
Designed year/month partition layouts
Combined multiple small CSV files
Compared common Data Engineering file formats
Created an Avro-style schema
Created a partitioned folder structure using Python
Proposed improvements for analytical storage performance
Main takeaway

Query performance depends heavily on how data is stored and accessed.

Important optimization ideas include:

avoid unnecessary full table scans
use indexes when appropriate
filter data early
select only required columns
partition data based on common query patterns
avoid excessive small files
use columnar formats such as Parquet for analytical workloads


The goal of this repository is to build a strong foundation in Data Engineering step by step.

This is the beginning of my transition into Data Engineering, with a focus on clean code, consistent practice, reusable functions, data transformation, and professional growth.
