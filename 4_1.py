def computepay(hours, rate) :
    #print ("Hours & Rate", hours, rate)
    if hours > 40 :
        reg = hours * rate
        ovt = (hours - 40) * ( rate* .5)
        pay = reg + ovt
    else:
        pay = hours * rate
        #print("Returning",pay)
    return pay
c = input("Enter Hours: ")
d= input("Enter rate: ")
a = float(c)
b = float(d)
pay = computepay(a, b)

print("Pay:",pay)
