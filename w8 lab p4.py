#luis rivera
#11/21/21

#problem 4 is a function in which it takes a leap year as a parameter and bring it back if its true and if its false it will not

def is_leap(year):
    leap = false

    if (year % 4 == 0) and (year % 100 != 0):
        leap = true
    elif (year % 100 == 0) and (year % 400 != 0):
        leap = false
    elif (year % 400 == 0):
        leap = "Yes this year is a leap year"
    else:
        leap = "No this year is not a leap year"

    return leap

year = int(input("Enter the year for it to determine: "))
print(is_leap(year))
        
