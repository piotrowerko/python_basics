# https://www.codewars.com/kata/56fac4cfda8ca6ec0f001746/train/python

def day_and_time(mins):
    days = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }
    full_weeks = abs(mins) // (7 * 24 * 60)
    trimed_mins = abs(mins) - full_weeks * 24 * 7 * 60
    days_left = trimed_mins // (24 * 60)
    pure_minutes = trimed_mins % (24 * 60)
    
    hours_for_return = pure_minutes // 60
    if hours_for_return < 10:
        hours_for_return = f'0{hours_for_return}'
    mins_for_return = pure_minutes - (hours_for_return * 60)
    
    for day in days.keys():
        if days_left == days[day]:
            give_day = day
    
    return f'{give_day} {hours_for_return}:{mins_for_return}'


def day_and_time(mins):
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    minutes_in_week = 7 * 24 * 60
    minutes_in_day = 24 * 60
    minutes_in_hour = 60
    weeks, rest_minutes = divmod(abs(mins), minutes_in_week)
    if mins < 0:
        rest_minutes = minutes_in_week - rest_minutes
    number_of_day, rest = divmod(rest_minutes, minutes_in_day)
    hour, minutes = divmod(rest, minutes_in_hour)
    return f"{days.get(number_of_day)} {hour:02d}:{minutes:02d}"

from datetime import timedelta, datetime
def day_and_time(mins):
    return "{:%A %H:%M}".format(datetime(2017, 1, 1) + timedelta(minutes = mins))

def day_and_time(mins):
    dow = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    return "{} {:02d}:{:02d}".format(dow[(mins // 1440) % 7], (mins // 60) % 24, mins % 60)

def main():
    mins = 90059
    print(day_and_time(mins))


if __name__ == '__main__':
    main()