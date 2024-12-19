bins=list(input("Enter any binary number:"))
bins.reverse()
dec=[]
sums=0
for i in range(len(bins)):
    if bins[i]=='0':
        pass
    elif bins[i]=='1':
        dec.append(2**i)
for x in range(len(dec)):
    sums=sums+dec[x]
print("Your binary number in decimal is:",sums)

