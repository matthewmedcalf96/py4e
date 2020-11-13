# str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the
#colon character and then use the float function to convert the extracted
#string into a floating point number.
#str = 'X-DSPAM-Confidence: 0.8475'
#ipos = str.find(':')
#print(ipos)
#piece = str[ipos+2:]
#value = float(piece)
#print(value)
text = "X-DSPAM-Confidence:    0.8475";
ipos = str.find(':')
piece = str[ipos+2:]
value = float(piece)
print(value)
