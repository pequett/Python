def is_year_leap(year):
    if year < 1582:
        return None
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
def days_in_month(year, month):
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        months_length[1] = 29
    if month < 1 or month > 12:
        return None
    return months_length[month-1]

def day_of_year(year, month, day):
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = 0
    d += day
    if is_year_leap(year):
        months_length[1] = 29
    if month < 1 or month > 12:
        return None
    if day < 1 or day > months_length[month-1]:
        return None
    if month > 1:
        for i in range(1, month):
            d += months_length[i - 1]
    
    return d
        

print(day_of_year(2024, 4, 4))
