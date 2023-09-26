#Write a function to detect 13th Friday. The function can accept two parameters, and both will be numbers. The first parameter will be the number indicating the month, and the second will be the year in four digits. Your function should parse the parameters, and it must return True when the month contains a Friday with the 13th, else return False.
import datetime

def has_friday_13(month, year):
    try:
        # Create a date object for the 13th day of the given month and year
        date = datetime.date(year, month, 13)
        
        # Check if the day of the week for the 13th is Friday (4 for Friday)
        if date.weekday() == 4:
            return True
        else:
            return False
    except ValueError:
        # Handle invalid month or year
        return False

month = 9
year = 2023
result = has_friday_13(month, year)
if result:
    print(f'Yes, {month}/{year} has a Friday the 13th.')
else:
    print(f'No, {month}/{year} does not have a Friday the 13th.')
