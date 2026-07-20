from datetime import datetime

# 1. Get the current date and time
today = datetime.now()
print(f"Today's Date: {today.strftime('%Y-%m-%d')}\n")

# 2. Calculate the first day of the current month
# We keep the current year and month, but force the day to 1
first_day_month = today.replace(day=1)
print(f"🗓️  First Day of this Month: {first_day_month.strftime('%A, %B %d, %Y')}")

# 3. Calculate the first day of the current year
# We keep the current year, but force the month and day to 1
first_day_year = today.replace(month=1, day=1)
print(f"🎆 First Day of this Year: {first_day_year.strftime('%A, %B %d, %Y')}")
