from datetime import datetime

year = int(input("Please enter your year of birth :"))
current_year= datetime.now().year

print ( f'You are {current_year-year} years old')