#
# My first file
#Pratyakcha Upadhyay
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    myfile = open("textfile.txt", "w+")
    myfile = open("textfile.txt", "a+")

    
    # Open the file for appending text to the end
  


    # write some lines of data to the file
    for i in range(10):
        myfile.write("I will write this line again 10 times\n")
    
    # close the file when done
    # myfile.close()
    
    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r")
    if myfile.mode == 'r':
        contents = myfile.read()
        print(contents)
        fl = myfile.readlines()
        for x in fl:
            print(x)
    
if __name__ == "__main__":
    main()
