
def timeConversion(s):
    # Write your code here
    hour = int(s[:2])
    middle = s[2:-2]
    meridian = s[-2:]
    if ((meridian=="PM")):
        if(hour==12):
            return str(hour)+middle
        else:    
            hour += 12
            return str(hour)+middle
    else:
        if (hour==12):
            return "00"+middle
        else:
            return "0"+str(hour)+middle


s = "12:45:54PM"
print(timeConversion(s))        
    