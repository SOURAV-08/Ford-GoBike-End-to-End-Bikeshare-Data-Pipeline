import os
import pandas as pd
import numpy as np

# 1. Get the current folder path
folder_path = os.path.dirname(os.path.abspath(__file__))
master_file = os.path.join(folder_path, "master_bike_data.csv")

print("Loading master dataset (this might take a few seconds)...")
df = pd.read_csv(master_file)

print("\n--- Starting Data Cleaning ---")

# 2. Convert start_time and end_time to actual DateTime objects
print("Converting time columns to datetime...")
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

# 3. Create new time features for deep analysis
print("Extracting time features (hour, day, month)...")
df['start_hour'] = df['start_time'].dt.hour
df['start_day_of_week'] = df['start_time'].dt.day_name()
df['start_month'] = df['start_time'].dt.strftime('%B')

# 4. Convert duration from seconds to minutes for better readability
print("Calculating duration in minutes...")
df['duration_min'] = df['duration_sec'] / 60

# 5. Handle missing values in user demographics safely
print("Handling missing values...")
df['member_gender'] = df['member_gender'].fillna('Unknown')

# Calculate age if birth year exists, else set to NaN
# (Assuming data is around 2018-2019 based on the file name)
df['member_age'] = 2019 - df['member_birth_year']

# 6. Filter out extreme anomalies (e.g., trips over 8 hours or negative durations)
print("Filtering out data anomalies...")
initial_rows = len(df)
df = df[(df['duration_min'] > 1) & (df['duration_min'] < 480)]
final_rows = len(df)
print(f"Removed {initial_rows - final_rows} anomalous or ultra-short trips.")

# 7. Review the cleaned dataset structure
print("\n✅ Data Cleaning Complete!")
print(f"Cleaned dataset rows: {df.shape[0]}")
print(f"New total columns: {df.shape[1]}")
print("\nNew columns added for analysis:")
print(['start_hour', 'start_day_of_week', 'start_month', 'duration_min', 'member_age'])

# 8. Save the polished, clean data for our final steps
clean_file = os.path.join(folder_path, "clean_bike_data.csv")
print(f"\nSaving cleaned dataset to: {clean_file}...")
df.to_csv(clean_file, index=False)
print("Saved successfully!")