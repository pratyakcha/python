#
#  I am learning Python loops
# My first loops yay!
# Pratyakcha Upadhyay
#


def main():
    x = 0

    # define a while loop
    while(x < 7):
        print(x)
        x = x + 1

    #  define a for loop
    for x in range (5,10):
        print(x)



    # use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)

    # TODO: use the break and continue statements
    y = 7
    for x in range (5,10):
        if x == y:
            break
        if x % 2 == 0:
         continue
        print(x)


    # TODO: using the enumerate() function to get index 
    
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i, d in enumerate (days):
    print(i , d)

#if __name__ == "__main__":
main()
