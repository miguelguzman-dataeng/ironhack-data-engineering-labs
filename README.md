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

## Goal

The goal of this repository is to build a strong foundation in Data Engineering step by step.

This is the beginning of my transition into Data Engineering, with a focus on clean code, consistent practice, reusable functions, data transformation, and professional growth.
