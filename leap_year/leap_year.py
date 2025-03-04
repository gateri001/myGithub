print("welcome!!, this program is used to check if a particular year is a leap year or not")
year = int(input("enter any year\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")
    
        