text = "X-DSPAM-Confidence:    0.8475"
number = text[text.find('0') : ]

print (float(number))