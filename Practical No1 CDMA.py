import numpy as np
c1 = [1,1,1,1]
c2 = [1,-1,1,-1]
c3 = [1,1,-1,-1]
c4 = [1,-1,-1,1]
rc = []

print("Enter the Data Bits:- ", end='')

d1 = int(input("/nD1: "))
d2 = int(input("/nD2: "))
d3 = int(input("/nD3: "))
d4 = int(input("/nD4: "))

r1 = np.multiply(c1, d1)
r2 = np.multiply(c2, d2)
r3 = np.multiply(c3, d3)
r4 = np.multiply(c4, d4)

resultant_channel = r1+r2+r3+r4;
print("Resultant_Channel", resultant_channel)
channel = int(input("Enter the Station to listen for C1=1, C2=2, C3=3, C4=4 : "))

if channel == 1:
    rc = c1

elif channel == 2:
    rc = c2

elif channel == 3:
    rc = c3

elif channel == 4:
    rc = c4

inner_product = np.multiply(resultant_channel, rc)

print("Inner Product", inner_product)
res1 = sum(inner_product)

data = res1/len(inner_product)
print("Data Bit that was sent",data)


