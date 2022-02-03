print("enter a year to know wheather it is leap year or not:-")
year=int(input("enter a year:"))
if year%4==1:
    print("it is next year after leap year")
    if year%4==2:
        print("it is second next year after leap year")
        if year%4==3:
            print("it is year before leap year")
            if year%4==0:
                print("it is a leap year")