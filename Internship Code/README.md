# Python Scripts for Internship Code

This directory contains Python scripts related to data processing and other operations.

## `main.py` - Sales Data Processor

**Purpose:**
The `main.py` script is designed to read a CSV file named `sales.csv`, perform basic data cleaning, and then display the head of the processed data.

**Cleaning Steps:**
1.  Fills missing values in the "Item" column with the string "null".
2.  Fills missing values in the "Quantity" column with the integer 0.

**Setup & Usage:**
1.  **Dependencies:** This script requires the `pandas` library. You can install it using pip:
    ```bash
    pip install pandas
    ```
2.  **Place `sales.csv`:** Make sure you have a file named `sales.csv` in this `Internship Code/` directory. The script reads the file from this relative location.
3.  **Run the script:** Execute the script from within the `Internship Code/` directory using:
    ```bash
    python main.py
    ```
    The script will print the first 5 rows of the cleaned DataFrame to the console. If `sales.csv` is not found, it will print an error message.

## `listOperations.py` - List Operations Module

**Purpose:**
The `listOperations.py` file is currently a placeholder module intended to house various functions for list manipulation. It contains an example list and a sample function.

**Usage:**
This module can be imported into other Python scripts if needed, and its functions can be called. It can be expanded with more list processing utilities.
