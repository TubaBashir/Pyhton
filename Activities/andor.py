# Input experimental data
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
has_vip_pass = input("Do you have a VIP pass? (yes/no): ").lower() == "yes"
is_banned = input("Are you banned from the venue? (yes/no): ").lower() == "yes"

# Demonstrating AND / OR logic
# OR needs at least one condition to be True
# AND needs all conditions to be True
if (has_ticket or has_vip_pass) and not is_banned:
    print("Access Granted! Welcome to the event.")
else:
    print("Access Denied!")
