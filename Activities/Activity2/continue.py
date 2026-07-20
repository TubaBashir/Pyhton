restricted_ids = ["ID-03", "ID-05"]
user_database = ["ID-01", "ID-02", "ID-03", "ID-04", "ID-05"]

for user_id in user_database:
    if user_id in restricted_ids:
        continue  # Silently skip updating restricted records
        
    print(f"⚙️ Updating Profile: {user_id}")
