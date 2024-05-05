def online_count(statuses):
    if len(statuses) == 0:
        return None
    people_online = 0
    online_list = list(statuses.keys())
    for key in online_list:
        key.lower()
        if statuses[key] == "online":
            people_online += 1
    return people_online

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statuses))