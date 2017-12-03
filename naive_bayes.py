import sys
import math

print("this is a naive bayes optimal classifier program")
n=raw_input("enter the total no of instance:\t")

nop=raw_input("enter the total number of positive instance:\t")
non=raw_input("enter the total number of negative instance:\t")
total_pos= float(nop)/float(n)
total_neg= float(non)/float(n)

outlook_sunny_pos=2/float(nop)
#print(outlook_sunny_pos)
outlook_sunny_neg=3/float(non)

temp_cool_pos=3/float(nop)
temp_cool_neg=1/float(non)

humidity_high_pos=3/float(nop)
himidity_high_neg=2/float(non)

wind_strong_pos=3/float(nop)
wind_strong_neg=3/float(non)

vmp=total_pos*outlook_sunny_pos*total_pos*humidity_high_pos*wind_strong_pos

print(vmp)

vmn=total_neg*outlook_sunny_neg*temp_cool_neg*himidity_high_neg*wind_strong_neg

print(vmn)

Vmp=(float(vmp)/float(vmp+vmn))

print(Vmp)

Vmn=(float(vmn)/float(vmn+vmp))

print(Vmn)
