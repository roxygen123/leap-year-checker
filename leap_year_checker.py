year = input("year you need to check:")
year_number = int(year)


def leap_year_checker():
    if year_number % 4 == 0:
        print(year_number,"it's a leap year")
    else: 
        print(year_number,"it's not a leap year")
leap_year_checker()
