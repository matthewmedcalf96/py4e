a = open('mbox-short.txt')

for line in a:
    line = line.rstrip()
    print('Line:' , line)
    if line == "" :
        print ('Skip Blank')
        continue
    wrds = line.split()
    print('Words:',wrds)
    #guardian
    #if len(wrds) < 1 :
        #continue
    if wrds[0] != 'From' :
        print('Ignore')
        continue
    print(wrds[2])
