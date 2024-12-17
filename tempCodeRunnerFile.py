import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection function using SQLAlchemy
def create_database_connection():
    # Replace with your correct username, password, and database name
    engine = create_engine('postgresql://postgres:khsbuPOSTGRE@1154@localhost:5432/mydatabase')
    return engine

# Load data into Pandas DataFrame
def load_data_to_dataframe():
    engine = create_database_connection()
    query = "SELECT * FROM messages;"  # Query to select all data from messages table
    df = pd.read_sql(query, engine)  # Load data into DataFrame using SQLAlchemy engine
    return df

# Perform ETL on the data
def perform_etl(df):
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Example transformation: filter messages after a certain timestamp
    df_filtered = df[df['timestamp'] > '2024-10-02 15:30:00'].copy()  # Using .copy() to avoid SettingWithCopyWarning

    # Example transformation: Add a new column using .loc
    df_filtered.loc[:, 'new_column'] = 'Transformed Data'

    return df_filtered

# Main function
if __name__ == "__main__":
    # Step 1: Load data from PostgreSQL
    messages_df = load_data_to_dataframe()

    # Step 2: Perform ETL (processing/transformation)
    transformed_df = perform_etl(messages_df)

    # Step 3: Display transformed data
    print(transformed_df)