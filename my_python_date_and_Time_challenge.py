# Pratyakcha Upadhyay
# Learning Python
#

import calendar
def count_days(year, month, whichday):
    # Get the number of days in the given month
    weeklist = calendar.monthcalendar(year, month)
    # Initialize a counter for the occurrences 
    count = 0   
    for week in weeklist:
    # Check if the day matches the given day
        if week[whichday] != 0:
            count += 1
    return count


print("--Day counter program--\n")

run = True
while(run):
    try:
        print("Which day of the week do you want to count?")
        print("0: Monday")
        print("1: Tuesday")
        print("2: Wednesday")
        print("3: Thursday")
        print("4: Friday")
        print("5: Saturday")
        print("6: Sunday")
        print("Or 'exit' to quit")

        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)

        yearstr = input("Enter year: ")
        year = int(yearstr)

        monthstr = input("Enter month: ")
        month = int(monthstr)

        result = count_days(year, month, day)
        print("There are " + str(result) + " of those days in the month and year specified")
        print("-----------\n")
    except Exception as e:
        print(e)
        print("Sorry, that's not valid input")