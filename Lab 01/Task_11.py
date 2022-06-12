import math

x = int(input())


def to_year_months_days(d):
    years = math.floor(d / 365)
    d = d % 365
    months = math.floor(d / 30)
    days = d % 30
    return str(years) + " years, " + str(months) + " months and " + str(days)+" days"


print(to_year_months_days(x))
