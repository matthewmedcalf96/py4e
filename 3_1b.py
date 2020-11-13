hours=input('Enter Hours:')
wage=input('Enter Wage:')
try:
    a = float(hours)
    b = float(wage)
except:
    print("Please Enter Nuemeric input")
    quit()
    
if a > 40 :
    reg = a * b
    ovt = (a - 40) * ( b* .5)
    xp = reg + ovt
else:
    xp = a * b
print("XYZ Pay:",xp)
