def add_time(start, duration, starting_day=""):
    # Parse start time
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute + dur_hour * 60 + dur_minute

    # Calculate new time and days later
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // (24 * 60)

    # Determine AM or PM
    meridian = "PM" if new_hour >= 12 else "AM"

    # Convert to 12-hour clock format
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12

    # Determine days later string
    days_later_str = ""
    if days_later == 1:
        days_later_str = " (next day)"
    elif days_later > 1:
        days_later_str = f" ({days_later} days later)"

    # Determine the day of the week
    if starting_day:
        starting_day_index = week_days.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_later) % 7
        new_day = f", {week_days[new_day_index]}"
    else:
        new_day = ""

    new_time = f"{new_hour}:{new_minute:02d} {meridian}{new_day}{days_later_str}"

    return new_time

# Define the week_days list outside the function
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
