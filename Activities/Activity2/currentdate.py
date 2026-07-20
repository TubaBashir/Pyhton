from datetime import datetime

# 1. Fetch the exact current system date and time
now = datetime.now()
print("Raw Timestamp Object:", now)

# 2. Format into standard readable strings (using strftime)
# %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute, %S = Second
clean_format = now.strftime("%Y-%m-%d %H:%M:%S")
print("Standard Format     :", clean_format)

# 3. Format into a friendly human-readable style
friendly_format = now.strftime("%B %d, %Y at %I:%M %p")
print("Human-Friendly Style:", friendly_format)

# 4. Extract individual parts directly
print(f"Extracted components: Year={now.year}, Month={now.month}, Day={now.day}")
