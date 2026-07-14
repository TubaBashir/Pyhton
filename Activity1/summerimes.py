import time

# Get details about the local time
local_time_info = time.localtime()

# Check the tm_isdst flag (1 = Summer Time/DST, 0 = Standard Time, -1 = Unknown)
if local_time_info.tm_isdst == 1:
    print("Your system is currently on Summer Time (Daylight Saving Time).")
else:
    print("Your system is currently on Standard Time (Winter Time).")
    
# Print your timezone names
print(f"Timezone abbreviations: {time.tzname}")