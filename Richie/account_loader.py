import pandas as pd
accounts_file_path = "output2.xlsx"  # Path to the Excel file containing account data

def load_accounts(file_path = accounts_file_path) -> pd.DataFrame:
    """
    Load account data from a CSV file and return it as a DataFrame.
    
    Args:
        file_path (str): The path to the CSV file containing account data.
        
    Returns:
        pd.DataFrame: A DataFrame containing the account data.
    """
    try:
        accounts_df = pd.read_excel(file_path)
        return accounts_df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
    except Exception as e:
        print(f"Error loading accounts: {e}")
        return []  # Return an empty list on error
    

if __name__ == "__main__":
    # Example usage
    file_path = "output1.xlsx"  # Replace with your actual file path
    accounts = load_accounts(file_path)
    print(accounts)  # Print the loaded accounts for verification