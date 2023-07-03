def is_leap_year(n):
    if((n%4==0 and n%100!=0) or n%400==0):
       print("Leap Year")
    else: print("NOT Leap Year")

year = int(input("Enter a Year : "))
is_leap_year(year)

