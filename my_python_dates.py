#
# Pratyakcha Upadhyay
# Learning Python
#
from datetime import datetime
from datetime import date
from datetime import time



def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today=datetime.today()
    print("Today's date is:", today)


    # TODO: print out the date's individual components
    print("Date Components:", today.day, today.month, today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday number:", today.weekday())
    days = ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]
    print("which is a ", days[today.weekday()])
    
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today1 = datetime.now()
    print(today1)
    
    # TODO: Get the current time

    t = datetime.time(datetime.now())
    print("The current time is", t)

 

  
if __name__ == "__main__":
    main()
  