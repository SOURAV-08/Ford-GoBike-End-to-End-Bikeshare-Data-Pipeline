import os
import pandas as pd

# 1. Load the cleaned data
folder_path = os.path.dirname(os.path.abspath(__file__))
clean_file = os.path.join(folder_path, "clean_bike_data.csv")

print("Loading cleaned dataset...")
df = pd.read_csv(clean_file)

print("\n=============================================")
print("          FORD GOBIKE KEY INSIGHTS           ")
print("=============================================\n")

# Insight 1: High-Level Metrics
total_trips = len(df)
avg_duration = df['duration_min'].mean()
print(f"📊 Total Successful Trips Analyzed: {total_trips:,}")
print(f"⏱️ Average Trip Duration: {avg_duration:.2f} minutes\n")

# Insight 2: User Types (Subscribers vs. Customers)
print("👥 User Type Breakdown:")
user_counts = df['user_type'].value_counts()
user_pct = df['user_type'].value_counts(normalize=True) * 100
for user, count in user_counts.items():
    print(f"   - {user}: {count:,} ({user_pct[user]:.1f}%)")
print("")

# Insight 3: Peak Hours of the Day (Top 5 Busiest Hours)
print("⏰ Top 5 Peak Hours for Bike Rentals:")
peak_hours = df['start_hour'].value_counts().head(5)
for hour, count in peak_hours.items():
    # Convert 24h to 12h format for presentation readability
    am_pm = "PM" if hour >= 12 else "AM"
    display_hour = hour if hour <= 12 else hour - 12
    if display_hour == 0: display_hour = 12
    print(f"   - {display_hour} {am_pm}: {count:,} trips")
print("")

# Insight 4: Busiest Days of the Week
print("📅 Weekly Demand Patterns (Busiest to Quietest):")
peak_days = df['start_day_of_week'].value_counts()
for day, count in peak_days.items():
    print(f"   - {day}: {count:,} trips")
print("")

# Insight 5: Top 5 Busiest Start Stations
print("📍 Top 5 Most Popular Start Stations:")
top_stations = df['start_station_name'].value_counts().head(5)
for station, count in top_stations.items():
    print(f"   - {station}: {count:,} trips")
print("\n=============================================")