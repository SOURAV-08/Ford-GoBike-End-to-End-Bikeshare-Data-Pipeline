import os
import glob
import zipfile
import pandas as pd

# 1. Get the current folder where this script lives
folder_path = os.path.dirname(os.path.abspath(__file__))
print(f"Working directory: {folder_path}")

# 2. Look for any zip files and extract them automatically
zip_files = glob.glob(os.path.join(folder_path, "*.zip"))
for zip_file in zip_files:
    print(f"Extracting: {os.path.basename(zip_file)}...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(folder_path)

# 3. Now find all the extracted CSV files
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Safety check: Ignore the master file if it already exists
all_files = [f for f in all_files if "master_bike_data.csv" not in f]
print(f"Found {len(all_files)} CSV files to merge.")

if len(all_files) == 0:
    print("\n❌ Error: Still no CSV files found. Ensure the zip file is in this exact folder!")
    exit()

# 4. Read and merge the CSV files
li = []
for filename in all_files:
    print(f"Reading: {os.path.basename(filename)}")
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

print("Merging all files together...")
merged_df = pd.concat(li, axis=0, ignore_index=True)

print(f"\n✅ Success! The dataset has {merged_df.shape[0]} rows and {merged_df.shape[1]} columns.")
print("\nHere are the columns in your dataset:")
print(merged_df.columns.tolist())

# 5. Save the master file
output_file = os.path.join(folder_path, "master_bike_data.csv")
merged_df.to_csv(output_file, index=False)
print(f"\nSaved master file as: {output_file}")