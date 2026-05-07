def add_time(start, duration,start_day=None):
    #start_time split into period, minutes and hour.
    start_time,period = start.split()
    start_hour, start_minute = start_time.split(":")
    
    #duration_time split into minutes and hour
    duration_hour, duration_minute = duration.split(":")
    
    #Changes strings into int
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)
    
    #Conditions for AM and PM
    if period == "PM" and start_hour != 12:
        start_hour +=12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    #Calculation
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    
    #Calculation for days_later
    days_later = new_hour // 24
    new_hour = new_hour % 24
    
    #Condition if total minute is greater than 60.
    if new_minute >= 60:
        new_hour += new_minute // 60
        new_minute += new_minute % 60
    
    #Condition for starting days
    if start_day:
        days = ["Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "sunday"]
        start_day = start_day.capitalize()
        day_index = days.index(start_day)
        
        new_day_index = day_index + days_later
        new_day_index = new_day_index % 7
        new_day = days[new_day_index]
    
    #Condition for new AM or PM
    if new_hour >= 12:
        new_period = "PM"
    else:
        new_period = "AM"
    
    
    new_hour = new_hour % 12
    
    #Condition after AM and PM for hours
    if new_hour == 0:
        new_hour = 12
    
    #To make minutes into 00 format
    new_minute = str(new_minute).zfill(2)
    
    #Converting new time into string
    new_time = f"{new_hour}:{new_minute} {new_period}"
    
    #Conditions for days later
    if start_day:
        new_time += f", {new_day}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f", ({days_later} days later)"
    

    return new_time

def main():
    
    start = input("Add time in AM or PM (ex: 3:00 AM): ")
    duration = input("Add Duration (ex: 10:02): ")
    start_day = input("Add starting day of the week: ")
    
    print(add_time(start, duration, start_day))
    
main()