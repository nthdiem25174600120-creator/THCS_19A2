i = int(input("Nhập i: "))

s1 = 0
for t in range(1,i+1):
    s1 += i 

s2 = 1
for t in range(1,i):
    s2 *= i

s3 = 0
for t in range(1, i+1):
    s3 += ((-1)** (i+1))/i

s4 = 0
for k in range(0,i+1):
    s4 += k/ (k+2)

print("S1: ", s1)
print("S2: ", s2)
print("S3: ", s3 )
print("S4: ", s4)