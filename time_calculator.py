def add_time(start, duration, day=""):
    # Days of the week list
    days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    
    # Parsing the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    
    # Parsing the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))
    
    # Calculate the new minutes and handle overflow to hours
    new_minute = start_minute + duration_minute
    extra_hour = new_minute // 60
    new_minute = new_minute % 60
    
    # Calculate the new hours and handle AM/PM and overflow to days
    new_hour = start_hour + duration_hour + extra_hour
    total_days = new_hour // 24
    new_hour = new_hour % 12
    
    # Handle the case where the hour is 0 (which should be 12 in a 12-hour format)
    if new_hour == 0:
        new_hour = 12

    # Determine the new period (AM/PM)
    period_switches = (start_hour + (duration_hour + extra_hour)) // 12
    if period == "PM" and (period_switches % 2 == 1):
        period = "AM"
        total_days += 1
    elif period == "AM" and (period_switches % 2 == 1):
        period = "PM"
    elif period == "PM" and (period_switches % 2 == 0):
        period = "PM"
    elif period == "AM" and (period_switches % 2 == 0):
        period = "AM"
    
    # Handle days later calculation
    total_days += (start_hour + (duration_hour % 12)) // 24
    
    # Determine the new day of the week
    if day:
        day_index = (days_of_week.index(day.lower()) + total_days) % 7
        new_day = days_of_week[day_index].capitalize()
    
    # Construct the result string
    result = f"{new_hour}:{new_minute:02d} {period}"
    if day:
        result += f", {new_day}"
    if total_days == 1:
        result += " (next day)"
    elif total_days > 1:
        result += f" ({total_days} days later)"
    print(result)
    return result

# Testing the function
add_time('11:55 AM', '3:12')
