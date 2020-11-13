num = 0
total = 0.0
while True :
    Value = input('Enter a Number: ')
    if Value == "done" :
            break
    try:
        fvalue = float(Value)
    except:
        print('Please Enter A Valid Number')
        continue
    num = num + 1
    total = total + fvalue
print(total , num , total/num)
