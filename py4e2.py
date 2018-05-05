hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter Rate per Hour:")
r = float(rph)
if ((h < 0) or (r < 0)):
    print ("Please use positive numbers")
elif 0 < h <=40:
    print (h * r)
elif h > 40:
    print (40 * r + (h-40)*r*1.5)
