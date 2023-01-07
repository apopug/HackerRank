def is_leap(year):
    leap = False
    
    # Write your logic here
    # evenly divide by 4 is leap or not evenly then not leap
    if year%4 == 0:
        leap = True
        # evenly divide
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
        
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))
