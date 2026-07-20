import random
from datetime import datetime, timedelta

def generate_random_datetime(start_date, end_date):
    # Calculate the total time window in seconds
    time_difference = end_date - start_date
    total_seconds = int(time_difference.total_seconds())
    
    # Pick a random number of seconds within that window
    random_seconds = random.randint(0, total_seconds)
    
    # Add the random seconds back to the start date
    return start_date + timedelta(seconds=random_seconds)

# 1. Define your date boundary window
start = datetime(2020, 1, 1, 0, 0, 0)    # Jan 1, 2020, at midnight
end = datetime(2026, 12, 31, 23, 59, 59) # Dec 31, 2026, at 11:59 PM

# 2. Generate a random timestamp
random_timestamp = generate_random_datetime(start, end)

# 3. Format and print the result
print("🗓️  Raw Timestamp Object :", random_timestamp)
print("✨ Human-Friendly Format:", random_timestamp.strftime("%B %d, %Y at %I:%M %p"))
