#To check the day on particular date.

import calendar

def check_valid_date(date,month,year,leap):
    if leap:
        if month==2:
            if date<=29:
                return True
            else:
                return False
        else:
            if month<8:
                if month%2==1:
                    if date<=31:
                        return True
                    else:
                        return False
                else:
                    if date<=30:
                        return True
                    else:
                        return False
                            
            else:
                if month%2==1:
                    if date<=30:
                        return True
                    else:
                        return False
                else:
                    if date<=31:
                        return True
                    else:
                        return False
                        
    else:
        if month==2:
            if date<=28:
                return True
            else:
                return False
        else:
            if month<8:
                if month%2==1:
                    if date<=31:
                        return True
                    else:
                        return False
                else:
                    if date<=30:
                        return True
                    else:
                        return False
                            
            else:
                if month%2==1:
                    if date<=30:
                        return True
                    else:
                        return False
                else:
                    if date<=31:
                        return True
                    else:
                        return False
                
                    

def check_leap(year):
    if year%4==0 and year%100!=0:    
        return True
    elif year%400==0:
        return True
    else:
        return False


def get_day(day_index):
    list_of_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return list_of_days[day_index]
    

while(1):
    year=int(input("Enetr year (from 1970) : "))
    if year<1970:
        print("Enter a year from 1970")
    else:
        break
    
while(1):
    month=int(input("Enter the month : "))
    if month<=12 and month>0:
        break
    else:
        print("Enter a valid month (1-12) ")

leap=check_leap(year)

while(1):
    date=int(input("Enter the date : "))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("Enter valid date")
        
day_index=calendar.weekday(year,month,date)

day=get_day(day_index)
print(date,"/",month,"/",year, " falls on",day,".")
