import sqlite3
import pandas as pd

# List of database file paths (from 2015 to 2024)
database_paths = [
    "/path/to/daily_data_frames_2015.db",
    "/path/to/daily_data_frames_2016.db",
    "/path/to/daily_data_frames_2017.db",
    "/path/to/daily_data_frames_2018.db",
    "/path/to/daily_data_frames_2019.db",
    "/path/to/daily_data_frames_2020.db",
    "/path/to/daily_data_frames_2021.db",
    "/path/to/daily_data_frames_2022.db",
    "/path/to/daily_data_frames_2023.db",
    "/path/to/daily_data_frames_2024.db"
]

# Initialize an empty dataframe to hold all data
combined_df = pd.DataFrame()

# Load data from each database and append to the combined dataframe
for db_path in database_paths:
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM daily_data_frames", conn)
    combined_df = pd.concat([combined_df, df], ignore_index=True)
    conn.close()

# Save the combined data to a new SQLite database
combined_db_path = "/path/to/combined_daily_data_frames.db"
conn_combined = sqlite3.connect(combined_db_path)

# Write the combined dataframe to the new database
combined_df.to_sql("daily_data_frames", conn_combined, if_exists="replace", index=False)

# Close the connection to the combined database
conn_combined.close()

print("Data from all yearly databases has been combined and saved to combined_daily_data_frames.db")
