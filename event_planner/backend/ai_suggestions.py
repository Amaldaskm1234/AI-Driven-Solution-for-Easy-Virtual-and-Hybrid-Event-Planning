def suggest_schedule(event_type):
    event_type = event_type.lower()

    if "wedding" in event_type:
        return [
            "Venue Setup - 9:00 AM",
            "Guest Welcome - 11:00 AM",
            "Wedding Ceremony - 12:30 PM",
            "Lunch - 2:00 PM",
            "Reception - 6:00 PM"
        ]
    elif "webinar" in event_type or "virtual" in event_type:
        return [
            "Login - 9:45 AM",
            "Intro Session - 10:00 AM",
            "Main Talk - 10:30 AM",
            "Q&A - 11:30 AM",
            "Closing - 12:00 PM"
        ]
    else:
        return [
            "Guest Check-in - 8:00 AM",
            "Opening Remarks - 9:00 AM",
            "Main Event - 10:00 AM",
            "Snacks - 1:00 PM",
            "Closing - 3:00 PM"
        ]
