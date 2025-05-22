"""
Processes sales data from a CSV file.

This script reads 'sales.csv' located in the same directory,
fills missing values in 'Item' and 'Quantity' columns,
and prints the first 5 rows of the cleaned DataFrame.
"""
import pandas as pd

def clean_sales_data(csv_filepath="sales.csv"):
    """
    Reads sales data from a CSV file, cleans it, and returns a DataFrame.

    Args:
        csv_filepath (str): The path to the sales CSV file.
                            Defaults to 'sales.csv' in the current directory.

    Returns:
        pandas.DataFrame: The cleaned DataFrame, or None if an error occurs.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_filepath)

        # Fill missing 'Item' values with the string "null"
        df["Item"] = df['Item'].fillna("null")
        
        # Fill missing 'Quantity' values with 0
        df['Quantity'] = df['Quantity'].fillna(0)
        
        return df

    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Assuming 'sales.csv' is in the same directory as this script
    cleaned_df = clean_sales_data("sales.csv")

    if cleaned_df is not None:
        print("Cleaned Sales Data (First 5 rows):")
        print(cleaned_df.head())
